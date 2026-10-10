"""Negative cases protect evidence and identity boundaries of the reference fixture."""
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate import validate_fixture, validate_expected_semantics
from verify_release import REPOSITORY, COMPONENT_BASE_PATH, validate_manifest, verify_components, verify_discovery


class FixtureTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'examples/assertions.example.json').read_text())
        self.raw = (ROOT / 'examples/synthetic-source.txt').read_bytes()
        self.schema = json.loads((ROOT / 'schemas/assertion-fixture.schema.json').read_text())

    def check(self):
        validate_fixture(self.data, self.raw, self.schema)
        validate_expected_semantics(self.data)

    def test_documented_examples_pass(self):
        self.check()

    def test_changed_source_bytes_fail(self):
        self.raw += b'Changed after extraction.\n'
        with self.assertRaisesRegex(ValueError, 'digest mismatch'):
            self.check()

    def test_wrong_quote_fails(self):
        self.data['assertions'][0]['evidence'][0]['selector']['quote'] = 'Invented quotation'
        with self.assertRaisesRegex(ValueError, 'Quote/selector'):
            self.check()

    def test_out_of_range_selector_fails(self):
        self.data['assertions'][0]['evidence'][0]['selector']['end'] = 99999
        with self.assertRaisesRegex(ValueError, 'out of range'):
            self.check()

    def test_missing_evidence_fails(self):
        self.data['assertions'][0]['evidence'] = []
        with self.assertRaises(ValidationError):
            self.check()

    def test_boolean_is_not_vote_count(self):
        self.data['assertions'][0]['value']['value'] = True
        with self.assertRaises(ValidationError):
            self.check()

    def test_synthetic_example_cannot_be_marked_for_public_fact_view(self):
        self.data['assertions'][0]['publication']['eligible_for_civic_fact_view'] = True
        with self.assertRaises(ValidationError):
            self.check()

    def test_duplicate_assertion_id_fails(self):
        self.data['assertions'][1]['assertion_id'] = self.data['assertions'][0]['assertion_id']
        with self.assertRaisesRegex(ValueError, 'Duplicate assertion'):
            self.check()

    def test_collapsed_vote_fails(self):
        self.data['assertions'][1]['context_refs']['vote'] = 'urn:example:vote:1'
        with self.assertRaisesRegex(ValueError, 'Vote identity'):
            self.check()

    def test_wrong_treatment_fails(self):
        self.data['assertions'][1]['context_refs']['treatment'] = 'urn:example:treatment:agenda-inclusion'
        with self.assertRaisesRegex(ValueError, 'Wrong treatment'):
            self.check()

    def test_lost_condition_fails(self):
        self.data['assertions'][2]['meaning']['conditions'] = ['receipt of grant']
        with self.assertRaisesRegex(ValueError, 'Conditions lost'):
            self.check()

    def test_receipt_inferred_from_approval_fails(self):
        self.data['assertions'][2]['value']['value'] = 'grant_received'
        with self.assertRaisesRegex(ValueError, 'converted to execution/receipt'):
            self.check()

    def test_negated_topic_cannot_be_affirmed(self):
        self.data['assertions'][3]['meaning']['polarity'] = 'affirmative'
        with self.assertRaisesRegex(ValueError, 'Negation lost'):
            self.check()

    def test_negated_topic_does_not_create_project(self):
        self.data['assertions'][3]['context_refs']['matter'] = 'urn:example:matter:invented'
        with self.assertRaisesRegex(ValueError, 'turned into a project'):
            self.check()


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'doc.txt').write_text('Synthetic release fixture\n')
        (self.root / 'publication-files.json').write_text(json.dumps({'files':['doc.txt', 'publication-files.json']}))
        components = []
        for rel in ['doc.txt', 'publication-files.json']:
            raw = (self.root / rel).read_bytes()
            components.append({'path':rel, 'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest(), 'media_type':'text/plain'})
        self.manifest = {'release_id':'test-only', 'status':'candidate', 'contract_version':'test-only', 'ontology_profile':{}, 'source_revision':'a'*40, 'built_at':'2026-10-10T00:00:00Z', 'repository':REPOSITORY, 'component_base_path':COMPONENT_BASE_PATH, 'compatibility':{}, 'components':components, 'evaluation_refs':[], 'migration_refs':[], 'previous_release':None, 'license_status':'test fixture only'}

    def test_local_inventory_passes(self):
        self.assertEqual(verify_components(self.manifest, self.root), 2)

    def test_tampered_component_fails(self):
        (self.root / 'doc.txt').write_text('Tampered!')
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            verify_components(self.manifest, self.root)

    def test_duplicate_path_fails(self):
        self.manifest['components'].append(copy.deepcopy(self.manifest['components'][0]))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            validate_manifest(self.manifest)

    def test_traversal_path_fails(self):
        self.manifest['components'][0]['path'] = '../private.txt'
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            validate_manifest(self.manifest)

    def test_floating_source_ref_fails(self):
        self.manifest['source_revision'] = 'main'
        with self.assertRaisesRegex(ValueError, 'full commit'):
            validate_manifest(self.manifest)

    def test_internal_archive_fails(self):
        self.manifest['components'][0]['path'] = 'internal/archive.zip'
        with self.assertRaisesRegex(ValueError, 'Nonpublic'):
            validate_manifest(self.manifest)

    def test_inventory_omission_fails(self):
        self.manifest['components'].pop()
        with self.assertRaisesRegex(ValueError, 'public inventory'):
            verify_components(self.manifest, self.root)

    def test_wrong_registry_fails(self):
        self.manifest['repository'] = 'https://example.invalid/untrusted'
        with self.assertRaisesRegex(ValueError, 'Unexpected repository'):
            validate_manifest(self.manifest)

    def test_manifest_cannot_inventory_itself(self):
        self.manifest['components'][0]['path'] = 'releases/test-only/manifest.json'
        with self.assertRaisesRegex(ValueError, 'Self-referential'):
            validate_manifest(self.manifest)

    def test_discovery_digest_mismatch_fails(self):
        directory = self.root / 'releases/test-only'
        directory.mkdir(parents=True)
        (directory / 'manifest.json').write_text(json.dumps(self.manifest))
        discovery = {'repository':REPOSITORY, 'component_base_path':COMPONENT_BASE_PATH, 'discovery_revision':1, 'channels':{'candidate':{'release_id':'test-only', 'status':'candidate', 'published_at':'2026-10-10T00:00:00Z', 'manifest_url':'https://raw.githubusercontent.com/gitbrainlab/gitbrainlab.github.io/' + 'b'*40 + '/specs/civicspec/releases/test-only/manifest.json', 'manifest_sha256':'0'*64}, 'stable':None}}
        (self.root / '.well-known').mkdir()
        (self.root / '.well-known/civicspec.json').write_text(json.dumps(discovery))
        with self.assertRaisesRegex(ValueError, 'Manifest digest mismatch'):
            verify_discovery(self.root)


if __name__ == '__main__':
    unittest.main()
