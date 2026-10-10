"""Reproduce preservation tests offline, and action probes with a verified text cache.

No model is called. Source-derived labels are single-assistant annotations.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path
from controlled_english_guard import validate_rewrite
from controlled_english_v1 import classify as v1, historical_classify
from controlled_english_v2 import classify as v2
from controlled_english_v3 import classify as v3

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'evaluations/controlled-english-2026-10-10'


def mutate(ledger,field):
    changed=copy.deepcopy(ledger)
    value=changed[field]
    changed[field]=[] if isinstance(value,list) else {} if isinstance(value,dict) else 'synthetic_wrong_value'
    return changed


def run(texts=None):
    fields=json.loads((DATA/'protocol.json').read_text())['mutation_fields']
    actions=[]; mutations=[]; controls=[]; summaries={}
    for split in ['development','reserved','validation2']:
        cases=json.loads((DATA/(split+'-cases.json')).read_text())
        for c in cases:
            original=c['ledger']
            for version in ['v1','v2','v3']:
                for kind in ['unchanged','wording_only']:
                    changed=copy.deepcopy(original)
                    if kind=='wording_only':changed['wording']='Alternative prose is outside this mechanical guard; it requires semantic review.'
                    errors=validate_rewrite(original,changed,version)
                    controls.append({'case_id':c['case_id'],'split':split,'version':version,'kind':kind,'rejected':bool(errors)})
                for field in fields:
                    if not original.get(field):continue
                    errors=validate_rewrite(original,mutate(original,field),version)
                    mutations.append({'case_id':c['case_id'],'split':split,'version':version,'field':field,'synthetic_error':True,'detected':bool(errors),'errors':errors})
            if texts is not None:
                text=texts[c['case_id']]
                # All development cases have one evidence record; joining is declared
                # here so an expanded dataset cannot silently alter its text binding.
                if len(original['evidence'])!=1:raise ValueError('Multiple evidence spans need a declared joining adapter')
                expected_digest=original['evidence'][0]['selected_text_sha256']
                if hashlib.sha256(text.encode()).hexdigest()!=expected_digest:
                    raise ValueError('Text cache does not match evidence selector: '+c['case_id'])
                for version,fn in [('historical',historical_classify),('v1',v1),('v2',v2),('v3',v3)]:
                    pred=fn(text);group=c['group']
                    result=group if group in ['outside_classifier_scope','unresolved_source'] else 'correct' if pred==c['expected_action'] else 'abstain' if pred=='abstain' else 'incorrect'
                    actions.append({'case_id':c['case_id'],'split':split,'version':version,'group':group,'expected':c['expected_action'],'observed':pred,'result':result})
        s={'cases':len(cases),'label_groups':dict(collections.Counter(c['group'] for c in cases)),'preservation':{},'actions':{}}
        for version in ['v1','v2','v3']:
            mm=[x for x in mutations if x['split']==split and x['version']==version]
            cc=[x for x in controls if x['split']==split and x['version']==version]
            s['preservation'][version]={'mutations':len(mm),'detected':sum(x['detected'] for x in mm),'missed':sum(not x['detected'] for x in mm),'valid_controls':len(cc),'false_rejections':sum(x['rejected'] for x in cc),'by_field':{f:{'total':sum(x['field']==f for x in mm),'detected':sum(x['field']==f and x['detected'] for x in mm)} for f in fields}}
        if texts is not None:
            for version in ['historical','v1','v2','v3']:
                aa=[x for x in actions if x['split']==split and x['version']==version]
                s['actions'][version]={g:dict(collections.Counter(x['result'] for x in aa if x['group']==g)) for g in s['label_groups']}
        summaries[split]=s
    return {'method':'deterministic_action_probe_and_synthetic_semantic_mutation_test','model_calls':0,'independent_gold':False,'summaries':summaries,'action_results':actions,'mutation_results':mutations,'control_results':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--text-cache',type=Path)
    p.add_argument('--output',type=Path)
    a=p.parse_args();texts=json.loads(a.text_cache.read_text()) if a.text_cache else None
    result=run(texts)
    if a.output:a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'mode':'source_verified_actions_and_offline_preservation' if texts else 'offline_preservation_only','summaries':result['summaries']},indent=2))


if __name__=='__main__':main()
