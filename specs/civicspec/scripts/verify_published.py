"""Check the discovery pointer against pinned component bytes in local Git history."""
import subprocess
import tempfile
from pathlib import Path

from verify_release import COMPONENT_BASE_PATH, validate_manifest, verify_components, verify_discovery


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = verify_discovery(root)
    validate_manifest(manifest)
    revision = manifest['source_revision']
    with tempfile.TemporaryDirectory(prefix='civicspec-release-') as directory:
        snapshot = Path(directory)
        for component in manifest['components']:
            rel = component['path']
            raw = subprocess.run(['git', 'show', f'{revision}:{COMPONENT_BASE_PATH}/{rel}'], cwd=root, check=True, capture_output=True).stdout
            destination = snapshot / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
        count = verify_components(manifest, snapshot)
    print(f'PASS: discovery and {count} components at pinned Git revision {revision}.')
    print('No consumer adoption or remote availability is implied.')


if __name__ == '__main__':
    main()
