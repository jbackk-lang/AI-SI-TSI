"""Stage 044: separate question intent from evidence availability.

Deterministic baseline, NOT new H512 training/inference.
H512 operator is logged and is only decisive on unrecognized questions.
Entity name and property PID STILL come from an upstream parser.
"""
from __future__ import annotations
import re
import unicodedata
from typing import Any

FACT_PREFIXES = (
    'jakiego rodzaju obiektem',
    'do którego kraju należy',
    'w jakim miejscu przyszła na świat',
    'w jakim kraju jest',
    'gdzie urodził się',
    'where was',
    'what kind of entity is',
    'what is the capital of',
    'what is ',
)
LOGIC_EXPRESSIONS = frozenset({
    'a and b', 'a or b', 'not a', 'a implies b',
    'a oraz b', 'a lub b', 'nie a', 'a wtedy i tylko wtedy gdy b',
})

def normalized(text: str) -> str:
    return ' '.join(unicodedata.normalize('NFC', text).casefold().split()).rstrip('?.! ')

def detect_intent(question: str) -> str:
    q = normalized(question)
    if q in LOGIC_EXPRESSIONS:
        return 'logic'
    if any(q.startswith(p) for p in FACT_PREFIXES):
        return 'fact'
    return 'uncertain'

def decide(question: str, h512_operator: str | None = None) -> dict[str, Any]:
    intent = detect_intent(question)
    op = (h512_operator or '').upper()
    if intent == 'logic':
        action = 'not_wikimemory'
    elif intent == 'fact':
        action = 'lookup'
    elif op == 'READ':
        action = 'lookup_model_fallback'
    else:
        action = 'abstain_uncertain'
    return {
        'intent': intent,
        'action': action,
        'h512_operator_observed': h512_operator,
        'h512_overridden': intent == 'fact' and h512_operator is not None and op != 'READ',
        'policy_is_deterministic': True,
    }

def answer(db: Any, question: str, entity_label: str | None,
           property_id: str | None, h512_operator: str | None = None) -> dict[str, Any]:
    route = decide(question, h512_operator)
    if route['action'] == 'not_wikimemory':
        return {**route, 'status': 'not_wikimemory', 'evidence': []}
    if route['action'] == 'abstain_uncertain':
        return {**route, 'status': 'uncertain_intent', 'evidence': []}
    if not entity_label or not property_id or not re.fullmatch(r'P[1-9]\d*', property_id):
        return {**route, 'status': 'unresolved_key', 'evidence': []}
    return {**route, **db.answer(entity_label, property_id)}
