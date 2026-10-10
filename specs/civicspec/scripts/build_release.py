"""Build a candidate manifest from a reviewed explicit public inventory."""
import argparse
import hashlib
import json
import mimetypes
from pathlib import Path

from verify_release import REPOSITORY, COMPONENT_BASE_PATH, safe_path, validate_manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-revision', required=True)
    parser.add_argument('--built-at', required=True)
    parser.add_argument('--release-id', required=True)
    parser.add_argument('--contract-version', default='0.1.0-rc.1')
    parser.add_argument('--previous-release')
    parser.add_argument('--evaluation-ref', action='append', default=[])
    parser.add_argument('--migration-ref', action='append', default=[])
    parser.add_argument('--compatibility-note', default='Initial public candidate; fixture schema only. No production ontology conformance or bot adoption implied.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    safe_path(args.release_id)
    if '/' in args.release_id:
        raise ValueError('Release ID must be one path segment')
    destination = root / 'releases' / args.release_id / 'manifest.json'
    if destination.exists():
        raise ValueError('Refusing to overwrite a release manifest; use a new release ID')
    inventory = json.loads((root / 'publication-files.json').read_text())['files']
    components = []
    for rel in inventory:
        safe_path(rel)
        path = root / rel
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('Component escapes repository')
        raw = path.read_bytes()
        components.append({'path': rel, 'media_type': mimetypes.guess_type(rel)[0] or 'text/plain', 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
    baseline = root / 'research/baseline-manifest.json'
    manifest = {
        'release_id': args.release_id, 'status': 'candidate',
        'scope': 'experimental_specification_and_reference_toolkit',
        'contract_version': args.contract_version,
        'ontology_profile': {'id': 'layered_v5_replay', 'baseline_date': '2026-09-07', 'inventory_path': 'research/baseline-manifest.json', 'inventory_sha256': hashlib.sha256(baseline.read_bytes()).hexdigest()},
        'repository': REPOSITORY, 'component_base_path': COMPONENT_BASE_PATH, 'source_revision': args.source_revision, 'built_at': args.built_at,
        'compatibility': {'production_contract': False, 'supported_consumer_contracts': ['civicspec-github-discovery-v1'], 'requires_explicit_candidate_opt_in': True, 'breaking_changes': [], 'note': args.compatibility_note},
        'components': components, 'evaluation_refs': ['docs/validation.md'] + args.evaluation_ref, 'migration_refs': args.migration_ref, 'previous_release': args.previous_release,
        'license_status': 'No project license selected; see LICENSE_STATUS.md.'
    }
    validate_manifest(manifest)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    print(destination.relative_to(root))
    print('manifest_sha256=' + hashlib.sha256(destination.read_bytes()).hexdigest())
    print('Verify the supplied source revision actually contains these bytes before publishing its channel pointer.')


if __name__ == '__main__':
    main()
