"""Verify a repository-local release inventory. No network fetch or adoption."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath

REPOSITORY = 'https://github.com/gitbrainlab/gitbrainlab.github.io'
RAW_PREFIX = 'https://raw.githubusercontent.com/gitbrainlab/gitbrainlab.github.io/'
COMPONENT_BASE_PATH = 'specs/civicspec'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_path(value):
    require(isinstance(value, str) and re.fullmatch(r'[A-Za-z0-9_.\-/]+', value) is not None, 'Invalid component path')
    p = PurePosixPath(value)
    require(not p.is_absolute() and p.as_posix() == value and all(x not in {'.', '..', ''} for x in p.parts), 'Unsafe component path')
    return value


def validate_manifest(manifest):
    for key in ['release_id', 'status', 'contract_version', 'ontology_profile', 'source_revision', 'built_at', 'repository', 'component_base_path', 'compatibility', 'components', 'evaluation_refs', 'migration_refs', 'previous_release', 'license_status']:
        require(key in manifest, f'Missing manifest field: {key}')
    require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', manifest['release_id']) is not None, 'Invalid release ID')
    require(manifest['status'] in {'candidate', 'stable'}, 'Invalid release status')
    require(manifest['repository'] == REPOSITORY, 'Unexpected repository')
    require(manifest['component_base_path'] == COMPONENT_BASE_PATH, 'Unexpected component base path')
    require(re.fullmatch(r'[0-9a-f]{40}', manifest['source_revision']) is not None, 'Source revision must be a full commit SHA')
    require(datetime.fromisoformat(manifest['built_at'].replace('Z', '+00:00')).tzinfo is not None, 'Build time needs a timezone')
    components = manifest['components']
    require(isinstance(components, list) and 0 < len(components) <= 1000, 'Invalid component count')
    paths, size = set(), 0
    for c in components:
        path = safe_path(c['path'])
        require(path not in paths, 'Duplicate component path')
        require(not path.startswith(('.git/', '.venv/', 'internal/')) and '__pycache__' not in path.split('/'), 'Nonpublic component path')
        require(path != '.well-known/civicspec.json' and not re.fullmatch(r'releases/[^/]+/manifest.json', path), 'Self-referential release inventory')
        require(type(c['bytes']) is int and 0 <= c['bytes'] <= 2_000_000, 'Invalid component byte count')
        require(re.fullmatch(r'[0-9a-f]{64}', c['sha256']) is not None, 'Invalid component digest')
        require(isinstance(c['media_type'], str) and '/' in c['media_type'], 'Invalid media type')
        paths.add(path)
        size += c['bytes']
    require(size <= 10_000_000, 'Reference inventory exceeds size budget')
    return paths


def verify_components(manifest, root):
    paths = validate_manifest(manifest)
    root = root.resolve()
    for c in manifest['components']:
        p = root / c['path']
        require(not p.is_symlink() and p.resolve().is_relative_to(root), 'Component escapes root or is a symlink')
        raw = p.read_bytes()
        require(len(raw) == c['bytes'], f'Byte count mismatch: {c["path"]}')
        require(hashlib.sha256(raw).hexdigest() == c['sha256'], f'Digest mismatch: {c["path"]}')
    allowlist = json.loads((root / 'publication-files.json').read_text())['files']
    require(len(allowlist) == len(set(allowlist)) and set(allowlist) == paths, 'Manifest differs from public inventory')
    return len(paths)


def verify_discovery(root):
    d = json.loads((root / '.well-known/civicspec.json').read_text())
    require(d['repository'] == REPOSITORY, 'Unexpected registry repository')
    require(d['component_base_path'] == COMPONENT_BASE_PATH, 'Unexpected registry path')
    require(type(d['discovery_revision']) is int and d['discovery_revision'] > 0, 'Invalid discovery revision')
    entry = d['channels']['candidate']
    require(entry is not None, 'No candidate is advertised')
    require(entry['status'] == 'candidate', 'Candidate channel status mismatch')
    require(datetime.fromisoformat(entry['published_at'].replace('Z', '+00:00')).tzinfo is not None, 'Publication time needs a timezone')
    require(re.fullmatch(r'[0-9a-f]{64}', entry['manifest_sha256']) is not None, 'Invalid manifest digest')
    rel = safe_path(f'releases/{entry["release_id"]}/manifest.json')
    pattern = re.escape(RAW_PREFIX) + r'[0-9a-f]{40}/' + re.escape(COMPONENT_BASE_PATH + '/' + rel)
    require(re.fullmatch(pattern, entry['manifest_url']) is not None, 'Manifest URL is not pinned to the configured repository')
    raw = (root / rel).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == entry['manifest_sha256'], 'Manifest digest mismatch')
    m = json.loads(raw)
    require(m['release_id'] == entry['release_id'] and m['status'] == entry['status'], 'Release/channel mismatch')
    return m


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--manifest', type=Path, help='Verify a local manifest directly, without the discovery pointer')
    args = parser.parse_args()
    m = json.loads(args.manifest.read_text()) if args.manifest else verify_discovery(args.root)
    count = verify_components(m, args.root)
    print(f'PASS: {m["release_id"]}: {count} local components match source {m["source_revision"]}.')
    print('This verifies bytes and pointer consistency, not registry authority, remote availability, or adoption.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
