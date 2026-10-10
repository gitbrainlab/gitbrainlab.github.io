"""Preservation guard between a source-anchored ledger and its derived ledger.

This is an input/output invariant checker. It is not a truth oracle, a prose
parser, an evidence-entailment checker, or an ASD-STE100 conformance checker.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def profile(version):
    return json.loads((ROOT / 'profiles/controlled-english' / (version + '.json')).read_text())


def validate_rewrite(original, candidate, version='v1'):
    rules = profile(version)
    errors = []
    for field in rules['required_claim_fields']:
        if field not in candidate:
            errors.append('missing:' + field)
    for field in rules['nonempty_claim_fields']:
        if not candidate.get(field):
            errors.append('empty:' + field)
    for field in rules['protected_on_rewrite']:
        if original.get(field) != candidate.get(field):
            errors.append('changed:' + field)
    if rules.get('reject_unknown_claim_fields'):
        for field in set(candidate) - set(rules['allowed_claim_fields']):
            errors.append('unknown:' + field)
    return sorted(set(errors))
