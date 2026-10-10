"""Guard implementation 1.1: preserve JSON types as well as field values.

Added during final implementation review, after the frozen corpus study.
The historical study continues to use its original frozen guard. This wrapper
closes Python's True == 1 / False == 0 equivalence for wording-only rewrites.
"""
import json
from controlled_english_guard import profile, validate_rewrite

IMPLEMENTATION_VERSION='cce-preservation-guard/1.1'


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)


def validate_typed_rewrite(original,candidate,version='v3'):
    errors=validate_rewrite(original,candidate,version)
    for field in profile(version)['protected_on_rewrite']:
        if canonical(original.get(field))!=canonical(candidate.get(field)):
            errors.append('changed:'+field)
    return sorted(set(errors))
