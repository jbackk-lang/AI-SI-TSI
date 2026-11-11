"""Compare lexical retrieval with a real H512 READ gate on held-out Wikidata."""
import argparse
import bz2
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
import unicodedata

import torch

SOURCE = "https://dumps.wikimedia.org/wikidatawiki/entities/20261109/wikidata-20261109-all.json.bz2"
PREFIX_SHA = "a42bb6e48c2d3f914082382bf3142004419245b2eb21c10ffd58e9a163b27a80"
CHECKPOINTS = {
    "h512.pt": "23e7c2f208129776705ea075f855c1afd5d26caf2bd7f1620fdae96b16c48851",
    "null_gate_75.pt": "a1541e9d69858769b62f4dea3365cbde7579bb61f56936abde38f9fbb286a57f",
}
# Fixed before inference. Expected values come from the held-out dump records.
CASES = (
    ("W jakim kraju jest avenue des Champs-Élysées?", "avenue des Champs-Élysées", "P17", "Q550", ["Q142"]),
    ("What kind of entity is hydrogen?", "hydrogen", "P31", "Q556", ["Q11344", "Q2313842"]),
    ("What is The Intouchables?", "The Intouchables", "P31", "Q595", ["Q11424"]),
    ("Gdzie urodził się Nicolaus Copernicus?", "Nicolaus Copernicus", "P19", "Q619", ["Q47554"]),
    ("Where was Neil Young born?", "Neil Young", "P19", "Q633", ["Q172"]),
    ("What kind of entity is Po?", "Po", "P31", "Q643", ["Q4022"]),
    ("W jakim kraju jest Rennes?", "Rennes", "P17", "Q647", ["Q142"]),
    ("What is the capital of Vanuatu?", "Vanuatu", "P36", "Q686", ["Q37806"]),
    ("What is the capital of IL?", "IL", "P36", None, "ambiguous"),
    ("What kind of entity is Belgium?", "Belgium", "P31", None, "unknown_entity"),
    ("Where was hydrogen born?", "hydrogen", "P19", None, "unknown_property"),
    ("What is the capital of Rennes?", "Rennes", "P36", None, "unknown_property"),
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_question(text):
    # Match the preprocessing used by the stage 036 READ gate.
    decomposed = unicodedata.normalize("NFKD", text.casefold().replace("ł", "l"))
    plain = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", plain).split())


def load_model(src):
    for name, expected in CHECKPOINTS.items():
        if sha(src / name) != expected:
            raise ValueError(f"Unexpected checkpoint hash: {name}")
    sys.path.insert(0, str(src.resolve()))
    from language import LANGUAGE_OPERATORS
    from network import TSINetwork
    from word_vector_geometry_core import WordVectorGeometryCore

    base = torch.load(src / "null_gate_75.pt", map_location="cpu", weights_only=True)
    reader = TSINetwork(width=96)
    reader.load_state_dict(base["weights"], strict=True)
    model = WordVectorGeometryCore(reader.eval(), expansion_width=512)
    checkpoint = torch.load(src / "h512.pt", map_location="cpu", weights_only=True)
    weights = checkpoint["weights"]
    expected_missing = {key for key in model.state_dict() if key.startswith("memory.")}
    loaded = model.load_state_dict(weights, strict=False)
    if loaded.unexpected_keys or set(loaded.missing_keys) != expected_missing:
        raise ValueError(f"Unexpected model keys: {loaded}")
    return model.eval(), LANGUAGE_OPERATORS


def run(prefix, src, output):
    from search import WikiSearch

    if sha(prefix) != PREFIX_SHA:
        raise ValueError("Unexpected Wikidata prefix")
    torch.set_num_threads(2)
    model, operators = load_model(src)
    output.mkdir(exist_ok=False)
    with bz2.open(prefix, "rt", encoding="utf-8") as stream:
        if next(stream).strip() != "[":
            raise ValueError("Unexpected dump header")
        entities = {}
        for line in stream:
            row = json.loads(line.strip().removesuffix(","))
            if re.fullmatch(r"Q[1-9][0-9]*", row["id"]):
                entities.setdefault(row["id"], row)
            if len(entities) == 300:
                break
    training_free_reference = list(entities)[:50]
    held_out = dict(itertools.islice(entities.items(), 50, 300))
    if len(held_out) != 250 or set(held_out).intersection(training_free_reference):
        raise AssertionError("Expected 250 disjoint QIDs")
    sample = output / "sample.json"
    sample.write_text("[\n" + ",\n".join(json.dumps(row, ensure_ascii=False)
                      for row in held_out.values()) + "\n]\n", encoding="utf-8")
    db = WikiSearch(output / "db")
    try:
        imported = db.import_stream(sample, source=SOURCE)
    finally:
        db.close()
    if imported["entities"] != 250 or imported["invalid_lines"]:
        raise AssertionError(imported)

    db = WikiSearch(output / "db")
    rows = []
    try:
        for question, label, pid, qid, expected in CASES:
            if qid:
                source_values = {
                    c["mainsnak"]["datavalue"]["value"]["id"]
                    for c in held_out[qid]["claims"][pid]
                    if c["rank"] != "deprecated" and c["mainsnak"]["snaktype"] == "value"
                }
                if source_values != set(expected):
                    raise AssertionError((qid, pid, source_values, expected))
            model_input = normalize_question(question)
            with torch.inference_mode():
                logits = model([model_input])[0][0]
                prob = torch.softmax(logits, dim=-1)
                if not torch.isfinite(prob).all() or len(prob) != len(operators):
                    raise ValueError("Invalid H512 logits")
                index = int(prob.argmax())
                operator = operators[index]
            gated = db.answer(label, pid) if operator == "READ" else {"status": "gate_abstention"}
            baseline = db.answer(label, pid)
            row = {"question": question, "label": label, "pid": pid, "expected_qid": qid,
                   "expected": expected, "model_input": model_input,
                   "operator": operator, "confidence": float(prob[index])}
            for name, answer in (("baseline", baseline), ("gated", gated)):
                status = answer["status"]
                values = sorted({value["id"] for value in answer.get("values", [])})
                correct = (status == "found" and answer["qid"] == qid and values == sorted(expected)
                           if qid else status != "found")
                row[name] = {"status": status, "qid": answer.get("qid"), "values": values,
                             "candidates": answer.get("candidates", []),
                             "evidence": answer.get("evidence", []), "correct": correct}
            if not qid and baseline["status"] != expected:
                raise AssertionError((question, expected, baseline))
            if expected == "ambiguous" and set(baseline["candidates"]) != {"Q801", "Q1204"}:
                raise AssertionError(baseline)
            rows.append(row)
    finally:
        db.close()

    metrics = {}
    for name in ("baseline", "gated"):
        metrics[name] = {
            "correct": sum(row[name]["correct"] for row in rows),
            "total": len(rows),
            "answerable_correct": sum(row[name]["correct"] for row in rows if row["expected_qid"]),
            "answerable_total": sum(row["expected_qid"] is not None for row in rows),
            "abstentions": sum(row[name]["status"] != "found" for row in rows),
            "unanswerable_correct": sum(row[name]["correct"] for row in rows if not row["expected_qid"]),
            "unanswerable_total": sum(row["expected_qid"] is None for row in rows),
        }
    return {
        "stage": 42, "dump_date": "2026-11-09", "license": "CC0-1.0", "source": SOURCE,
        "prefix_sha256": PREFIX_SHA, "sample_sha256": sha(sample),
        "sample": "Distinct QIDs 51–300 in dump order, disjoint from stage 041",
        "import": imported, "checkpoints": CHECKPOINTS, "h512_inference": True,
        "h512_training": False, "retention_measured": False, "torch_version": torch.__version__,
        "operators": dict(Counter(row["operator"] for row in rows)), "metrics": metrics,
        "rows": rows,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prefix", type=Path)
    parser.add_argument("checkpoint_src", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    result = run(args.prefix, args.checkpoint_src, args.output)
    report = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    (args.output / "result.json").write_text(report, encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "rows"},
                     ensure_ascii=False, indent=2))
