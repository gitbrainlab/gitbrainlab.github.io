import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from cce_backtest import run
from cce_lint import lint
from controlled_english_guard import validate_rewrite
from cce_typed_guard import validate_typed_rewrite
from controlled_english_v3 import classify

DATA=ROOT/'evaluations/controlled-english-2026-10-10'


class ControlledEnglishTests(unittest.TestCase):
    def test_frozen_versions_and_labels_have_not_changed(self):
        for name in ['freeze-v1.json','freeze-v2.json','freeze-v3.json']:
            receipt=json.loads((DATA/name).read_text())
            for rel,expected in receipt['files'].items():
                self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),expected,rel)
        for split,name in [('reserved','freeze-reserved-labels.json'),('validation2','freeze-validation2-labels.json')]:
            receipt=json.loads((DATA/name).read_text())
            self.assertEqual(hashlib.sha256((DATA/(split+'-cases.json')).read_bytes()).hexdigest(),receipt['sha256'])

    def test_cases_validate_against_evaluation_schema(self):
        from jsonschema import Draft202012Validator
        schema=json.loads((ROOT/'schemas/controlled-english-ledger.schema.json').read_text())
        validator=Draft202012Validator(schema)
        for split in ['development','reserved','validation2']:
            for case in json.loads((DATA/(split+'-cases.json')).read_text()):
                self.assertEqual(list(validator.iter_errors(case['ledger'])),[],case['case_id'])

    def test_offline_replay_matches_recorded_preservation_results(self):
        actual=run();expected=json.loads((DATA/'results-final.json').read_text())
        for split in actual['summaries']:
            self.assertEqual(actual['summaries'][split]['preservation'],expected['summaries'][split]['preservation'])
        self.assertEqual(actual['action_results'],[],'Offline run must not invent action execution')

    def test_preservation_detects_nested_condition_and_quantity_changes(self):
        cases=json.loads((DATA/'development-cases.json').read_text())
        c=next(x['ledger'] for x in cases if x['case_id']=='D03')
        changed=copy.deepcopy(c);changed['conditions'][0]['resolution']='satisfied'
        self.assertIn('changed:conditions',validate_rewrite(c,changed,'v3'))
        c=next(x['ledger'] for x in cases if x['case_id']=='D05')
        changed=copy.deepcopy(c);changed['quantities']['money.role']='payment_completed'
        self.assertIn('changed:quantities',validate_rewrite(c,changed,'v3'))

    def test_prose_only_contradiction_is_explicitly_outside_guard(self):
        c=json.loads((DATA/'development-cases.json').read_text())[0]['ledger']
        changed=copy.deepcopy(c);changed['wording']='The payment is independently verified.'
        self.assertEqual(validate_rewrite(c,changed,'v3'),[])

    def test_typed_guard_rejects_boolean_number_and_string_substitutions(self):
        c=json.loads((DATA/'development-cases.json').read_text())[0]['ledger']
        for original,replacement in [(0,False),(1,True),(1,'1'),(1,1.0)]:
            ledger=copy.deepcopy(c);ledger['quantities']={'value':original}
            changed=copy.deepcopy(ledger);changed['quantities']['value']=replacement
            self.assertIn('changed:quantities',validate_typed_rewrite(ledger,changed))
        self.assertEqual(validate_typed_rewrite(c,copy.deepcopy(c)),[])

    def test_known_future_hearing_failure_is_not_hidden(self):
        # Synthetic regression demonstrating the real J032 failure class.
        text='We will schedule the public hearing once the preliminary budget is set.'
        self.assertEqual(classify(text),'schedule_public_hearing')
        results=json.loads((DATA/'results-final.json').read_text())['action_results']
        row=next(x for x in results if x['case_id']=='J032' and x['version']=='v3')
        self.assertEqual(row['result'],'incorrect')

    def test_requirement_registry_is_well_formed(self):
        r=json.loads((ROOT/'profiles/controlled-english/requirements.json').read_text())
        self.assertEqual(lint(r)['errors'],[])
        changed=copy.deepcopy(r);changed['requirements'][0]['text']+=' The extractor MUST publish.'
        self.assertTrue(lint(changed)['errors'])

    def test_splits_do_not_share_source_municipalities(self):
        sets=[]
        for split in ['development','reserved','validation2']:
            sources=json.loads((DATA/(split+'-sources.json')).read_text())
            sets.append({x['municipality'] for x in sources})
        for a in range(3):
            for b in range(a):self.assertFalse(sets[a]&sets[b])


if __name__=='__main__':unittest.main()
