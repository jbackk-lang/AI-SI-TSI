"""Retrospective audit of archived stage 043 report; no H512 inference.
Usage: python audit_043.py path/to/stage043-result.json
"""
import json, sys
from pathlib import Path
from read_policy import decide

def audit(report):
    failures = report['newly_blocked_answers']
    retention = report['retention']
    observed = [{
        'question': row['question'],
        'before': row['before'],
        'after': row['after'],
        'policy_action': decide(row['question'], row['after'])['action'],
        'known_answerable': row['answerable'],
        'source_qid': row.get('qid'),
        'source_pid': row.get('pid'),
    } for row in failures + retention]
    return {
        'stage': 44,
        'mode': 'RETROSPECTIVE ANALYSIS of stage043 logged predictions; NOT new H512 inference or model training',
        'selection_warning': '21 cases are selected BECAUSE stage043 gated them incorrectly; not independent.',
        'newly_blocked_stage043_count': len(failures),
        'newly_blocked_explicit_fact_pattern_count': sum(x['policy_action'] == 'lookup' for x in observed[:len(failures)]),
        'retention_count': len(retention),
        'retention_explicit_fact_pattern_count': sum(x['policy_action'] == 'lookup' for x in observed[len(failures):]),
        'factual_answers_verified_by_stage044_database': 0,
        'checkpoint_stage043_executed': False,
        'actual_local_panel_changed': False,
        'test_full_pipeline_stage043_checkpoint': 'NOT RUN; requires local TSI-043.zip and real Wikidata DB',
        'observed': observed,
    }

if __name__ == '__main__':
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('stage043-result.json')
    result = audit(json.loads(source.read_text(encoding='utf-8')))
    print(json.dumps(result, ensure_ascii=False, indent=2))
