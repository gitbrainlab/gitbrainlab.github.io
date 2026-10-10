"""Fetch or reuse public source versions and reconstruct the exact evaluated spans.

Archives and text caches belong outside the repository. Remote changes fail closed.
Use --allow-network only for a deliberate retrieval; offline cache reuse is default.
"""
import argparse
import concurrent.futures
import hashlib
import io
import json
from pathlib import Path
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'evaluations/controlled-english-2026-10-10'
SPLITS=['development','reserved','validation2']
MAX_BYTES=12_000_000


def digest(data):return hashlib.sha256(data).hexdigest()


def load_sources():
    return {s['source_id']:s for split in SPLITS for s in json.loads((DATA/(split+'-sources.json')).read_text())}


def materialize(cache,allow_network=False):
    sources=load_sources();cache.mkdir(parents=True,exist_ok=True)
    def retrieve(source):
        path=cache/(source['sha256']+'.bin')
        if not path.exists():
            if not allow_network:raise ValueError('Missing cached source '+source['source_id'])
            if urllib.parse.urlparse(source['url']).scheme!='https':raise ValueError('HTTPS required')
            req=urllib.request.Request(source['url'],headers={'User-Agent':'CivicSpec evaluation source verification'})
            with urllib.request.urlopen(req,timeout=40) as response:
                if urllib.parse.urlparse(response.url).scheme!='https':raise ValueError('Insecure redirect')
                raw=response.read(MAX_BYTES+1)
            if len(raw)>MAX_BYTES:raise ValueError('Source exceeds configured size budget')
            if digest(raw)!=source['sha256']:raise ValueError('Remote source changed: '+source['source_id'])
            path.write_bytes(raw)
        raw=path.read_bytes()
        if digest(raw)!=source['sha256']:raise ValueError('Cached source hash mismatch: '+source['source_id'])
        return source['source_id'],raw
    raw_sources=dict(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(retrieve,sources.values()))
    texts={};checks=[]
    for split in SPLITS:
        for case in json.loads((DATA/(split+'-cases.json')).read_text()):
            e=case['ledger']['evidence'][0];raw=raw_sources[e['source_id']];selector=e['selector'];source=sources[e['source_id']]
            if source['kind']=='asr_reader':
                segments=json.loads(raw)['segs']
                if 'segment_indices' in selector:
                    text=' '.join(segments[i][1] for i in selector['segment_indices'])
                else:
                    start,end=selector['start_index'],selector['end_index_exclusive']
                    if not 0<=start<end<=len(segments):raise ValueError('Invalid segment bounds')
                    text='\n'.join(x[1] for x in segments[start:end])
            elif source['kind']=='official_pdf':
                import pypdf
                if pypdf.__version__!='6.10.0':raise ValueError('Replay requires pypdf==6.10.0')
                page=pypdf.PdfReader(io.BytesIO(raw)).pages[selector['page']-1].extract_text()
                start,end=selector['char_start'],selector['char_end']
                if not 0<=start<end<=len(page):raise ValueError('Invalid page text bounds')
                text=page[start:end]
            else:raise ValueError('Unsupported representation')
            if digest(text.encode())!=e['selected_text_sha256']:raise ValueError('Selector/representation drift: '+case['case_id'])
            texts[case['case_id']]=text
            checks.append({'case_id':case['case_id'],'source_id':e['source_id'],'source_bytes_verified':True,'selected_text_verified':True,'audio_verified':False})
    return texts,{'source_versions_verified':len(raw_sources),'cases_verified':len(checks),'checks':checks,'text_encoding':'UTF-8','pdf_adapter':'pypdf 6.10.0 extract_text; one-based page; zero-based end-exclusive Python Unicode offsets','transcript_adapter':'original segs order; development joins with space; reserved sets join with newline','truth_verified':False}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cache-dir',type=Path,required=True)
    p.add_argument('--text-cache',type=Path,required=True)
    p.add_argument('--receipt',type=Path,required=True)
    p.add_argument('--allow-network',action='store_true')
    a=p.parse_args()
    if a.cache_dir.resolve().is_relative_to(ROOT):raise ValueError('Keep source archives outside the specification tree')
    texts,receipt=materialize(a.cache_dir,a.allow_network)
    a.text_cache.write_text(json.dumps(texts,indent=2)+'\n');a.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='checks'}))


if __name__=='__main__':main()
