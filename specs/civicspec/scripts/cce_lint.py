"""Advisory requirement-registry lint, not a complete STE or grammar checker."""
import json
import re
from pathlib import Path


def lint(registry):
    errors=[];warnings=[];seen=set()
    for row in registry['requirements']:
        rid=row['id'];text=row['text']
        if rid in seen:errors.append(rid+':duplicate_id')
        seen.add(rid)
        if not re.fullmatch(r'CCE-\d{2}',rid):errors.append(rid+':invalid_id')
        keywords=re.findall(r'\b(?:MUST NOT|SHOULD NOT|MUST|SHOULD|MAY)\b',text)
        if len(keywords)!=1:errors.append(rid+':one_normative_keyword_required')
        if not re.match(r'The (author|extractor|renderer|publisher|evaluator|curator|consumer)\b',text):errors.append(rid+':explicit_role_required')
        if len(text.split())>20:warnings.append(rid+':over_20_words_review_meaning_before_shortening')
        if not row.get('verification'):errors.append(rid+':verification_scope_required')
    return {'requirements':len(seen),'errors':errors,'warnings':warnings,'scope':'IDs, selected explicit roles, keyword count and advisory whitespace word count only'}


if __name__=='__main__':
    p=Path(__file__).resolve().parents[1]/'profiles/controlled-english/requirements.json'
    result=lint(json.loads(p.read_text()));print(json.dumps(result,indent=2));raise SystemExit(bool(result['errors']))
