"""Offline checks for this public reference toolkit; not a civic extractor."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def validate_fixture(data, raw, schema):
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(data)
    text = raw.decode('utf-8')
    digest = hashlib.sha256(raw).hexdigest()
    ids = [a['assertion_id'] for a in data['assertions']]
    require(len(ids) == len(set(ids)), 'Duplicate assertion ID')
    for a in data['assertions']:
        for e in a['evidence']:
            require(e['source_sha256'] == digest, 'Source digest mismatch')
            require(e['representation_sha256'] == digest, 'Representation digest mismatch')
            require(e['source_version_id'] == 'urn:example:source:' + digest, 'Source version identity mismatch')
            require(e['representation_id'] == 'urn:example:text:' + digest, 'Representation identity mismatch')
            s = e['selector']
            require(0 <= s['start'] < s['end'] <= len(text), 'Selector out of range')
            require(text[s['start']:s['end']] == s['quote'], 'Quote/selector mismatch')
            require(e['source_version_id'] in a['lineage']['derived_from'], 'Missing source lineage')


def validate_expected_semantics(data):
    """Check only the four documented synthetic cases, not arbitrary civic truth."""
    by_id = {a['assertion_id']: a for a in data['assertions']}
    require(set(by_id) == {f'urn:example:assertion:{i}' for i in range(1, 5)}, 'Unexpected fixture assertion set')
    one, two, conditional, negative = [by_id[f'urn:example:assertion:{i}'] for i in range(1, 5)]
    require(one['context_refs']['matter'] == two['context_refs']['matter'], 'Votes must share a matter')
    for i, a, count, treatment in [(1, one, 6, 'agenda-inclusion'), (2, two, 4, 'ordinance-passage')]:
        ctx = a['context_refs']
        require(ctx['vote'] == a['subject_ref'] == f'urn:example:vote:{i}', 'Vote identity collapsed or mislinked')
        require(ctx['treatment'] == 'urn:example:treatment:' + treatment, 'Wrong treatment for vote')
        require(a['predicate_id'] == 'vote.yes_count' and a['value']['kind'] == 'count' and a['value']['value'] == count, 'Wrong vote count/predicate')
        require(a['meaning']['polarity'] == 'affirmative', 'Wrong vote polarity')
    require(conditional['predicate_id'] == 'ext:contract.addendum_approval', 'Conditional approval predicate lost')
    require(conditional['value']['value'] == 'approved_conditionally', 'Approval converted to execution/receipt')
    require(set(conditional['meaning']['conditions']) == {'receipt of grant', 'decision to proceed with project'}, 'Conditions lost')
    require(negative['meaning']['polarity'] == 'negative' and negative['value']['value'] == 'negated', 'Negation lost')
    require('matter' not in negative['context_refs'], 'Negated topic turned into a project')


def validate_research(root):
    manifest = load_json(root / 'research/baseline-manifest.json')
    for f in manifest['files']:
        path = root / 'research/2026-09-07' / f['path']
        raw = path.read_bytes()
        require(len(raw) == f['bytes'], f'Research byte count changed: {path}')
        require(hashlib.sha256(raw).hexdigest() == f['sha256'], f'Research bytes changed: {path}')
    return len(manifest['files'])


def heading_ids(text):
    result, counts = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'[`*_]', '', title).lower()
        slug = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.add(slug if not n else f'{slug}-{n}')
    return result


def validate_links(root):
    count = 0
    # Historical files intentionally reference artifacts outside the selected subset.
    for p in root.rglob('*.md'):
        if any(part in {'.git', '.venv', '__pycache__'} for part in p.parts):
            continue
        if 'research/2026-09-07/' in p.as_posix():
            continue
        content = p.read_text(encoding='utf-8')
        content = re.sub(r'```.*?```', '', content, flags=re.S)
        for raw_target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            target = raw_target.split(' "')[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            path = (p.parent / unquote(parsed.path)).resolve() if parsed.path else p
            require(path.is_relative_to(root.resolve()), f'Link escapes repository: {p}: {target}')
            require(path.exists(), f'Missing local link: {p}: {target}')
            if parsed.fragment and path.suffix == '.md':
                require(unquote(parsed.fragment) in heading_ids(path.read_text()), f'Missing heading: {p}: {target}')
            count += 1
    return count


def main():
    files = list(ROOT.rglob('*.json'))
    for p in files:
        if any(part in {'.git', '.venv', '__pycache__'} for part in p.parts):
            continue
        load_json(p)
    fixture = load_json(ROOT / 'examples/assertions.example.json')
    schema = load_json(ROOT / 'schemas/assertion-fixture.schema.json')
    validate_fixture(fixture, (ROOT / 'examples/synthetic-source.txt').read_bytes(), schema)
    validate_expected_semantics(fixture)
    baseline_count = validate_research(ROOT)
    links = validate_links(ROOT)
    spec = (ROOT / 'docs/specification.md').read_text()
    require(len(re.findall(r'^## ', spec, re.M)) == 23, 'Expected 23 specification sections')
    for i in range(1, 15):
        require(f'CS-{i:02d}' in spec, f'Missing core invariant CS-{i:02d}')
    print(f'PASS: JSON/schema; 4 synthetic assertions and selectors; fixture semantics; {baseline_count} retained research hashes; {links} local links; 23 specification sections.')
    print('Scope: reference toolkit only. No extractor, real-source accuracy, legal compliance, or SHACL execution was tested.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
