"""Import and verify a bounded sample from an official Wikidata dump prefix."""
import argparse
import bz2
import hashlib
import itertools
import json
import re
from pathlib import Path

from measure import measure
from search import WikiSearch

SOURCE = "https://dumps.wikimedia.org/wikidatawiki/entities/20261109/wikidata-20261109-all.json.bz2"
CHECKS = (
    ("Q8", "P31", "Q141800263"),
    ("Q45", "P36", "Q597"),
    ("Q23", "P31", "Q5"),
)


def run(prefix, output):
    output.mkdir(exist_ok=False)
    sample = output / "sample.json"
    with bz2.open(prefix, "rt", encoding="utf-8") as stream:
        if next(stream).strip() != "[":
            raise ValueError("Expected start of a Wikidata JSON dump")
        rows = {}
        for line in itertools.islice(stream, 1000):
            row = json.loads(line.strip().removesuffix(","))
            qid = row["id"]
            if re.fullmatch(r"Q[1-9][0-9]*", qid):
                rows[qid] = row
            if len(rows) == 50:
                break
        if len(rows) != 50:
            raise ValueError("Expected 50 distinct items")
    sample.write_text("[\n" + ",\n".join(json.dumps(row, ensure_ascii=False)
                      for row in rows.values()) + "\n]\n", encoding="utf-8")
    root = output / "db"
    db = WikiSearch(root)
    try:
        imported = db.import_stream(sample, source=SOURCE)
    finally:
        db.close()
    if imported["entities"] != 50 or imported["invalid_lines"]:
        raise AssertionError(imported)

    checks = []
    db = WikiSearch(root)
    try:
        for qid, pid, expected in CHECKS:
            row = rows[qid]
            raw_values = {
                json.dumps(claim["mainsnak"]["datavalue"]["value"], sort_keys=True)
                for claim in row["claims"][pid]
                if claim["rank"] != "deprecated" and claim["mainsnak"]["snaktype"] == "value"
            }
            found = db.lookup(qid, pid)
            actual_values = {json.dumps(item["value"], sort_keys=True)
                             for item in found["statements"]}
            label = row["labels"]["en"]["value"]
            answer = db.answer(label, pid)
            ids = sorted(json.loads(value)["id"] for value in actual_values)
            evidence = {"qid": qid, "pid": pid, "source": SOURCE,
                        "revision": row["lastrevid"]}
            if (found["status"] != "found" or actual_values != raw_values
                    or expected not in ids or found["entity_source"] != SOURCE
                    or found["revision"] != evidence["revision"]
                    or answer["status"] != "found" or answer["qid"] != qid
                    or {json.dumps(value, sort_keys=True) for value in answer["values"]} != raw_values
                    or not answer["evidence"] or any(item != evidence for item in answer["evidence"])):
                raise AssertionError((qid, pid, expected, found, answer))
            checks.append({**evidence, "label": label, "values": ids, "expected": expected})
        if db.answer("tsi stage041 absent probe 9dc831", "P31")["status"] != "unknown_entity":
            raise AssertionError("Missing name must abstain")
    finally:
        db.close()
    sizes = measure(root)
    if sizes["entities"] != len(rows):
        raise AssertionError(sizes)
    result = {
        "stage": 41, "source": SOURCE, "dump_date": "2026-11-09", "license": "CC0-1.0",
        "prefix_bytes": prefix.stat().st_size,
        "prefix_sha256": hashlib.sha256(prefix.read_bytes()).hexdigest(),
        "sample_sha256": hashlib.sha256(sample.read_bytes()).hexdigest(),
        "sample_selection": "First 50 distinct QIDs in dump order",
        "real_wikidata_entities": len(rows), "import": imported, "sqlite": sizes,
        "checks_after_reopen": checks, "unknown_entity_abstention": True,
        "h512_inference": False, "h512_training": False,
    }
    report = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    (output / "result.json").write_text(report, encoding="utf-8")
    print(report, end="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prefix", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    run(args.prefix, args.output)
