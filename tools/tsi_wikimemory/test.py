"""Fixture tests of actual SQLite writes. Fixtures are NOT imported Wikimedia facts."""
import json,pathlib,tempfile
from wikimemory import WikiMemory
ROOT=pathlib.Path(__file__).resolve().parent
fixture=[{'id':'Q900000001','lastrevid':1,'labels':{'pl':{'value':'obiekt testowy A'}},'descriptions':{'pl':{'value':'testowy wpis'}},'claims':{'P31':[{'rank':'normal','mainsnak':{'snaktype':'value','datatype':'wikibase-item','datavalue':{'value':{'entity-type':'item','id':'Q900000002','numeric-id':900000002}}}}]}},{'id':'Q900000002','lastrevid':2,'labels':{'en':{'value':'test object B'}},'claims':{'P279':[{'rank':'deprecated','mainsnak':{'snaktype':'value','datatype':'string','datavalue':{'value':'deprecated'}}}],'P1476':[{'rank':'normal','mainsnak':{'snaktype':'value','datatype':'monolingualtext','datavalue':{'value':{'text':'test','language':'en'}}}}]}}]
with tempfile.TemporaryDirectory() as t:
 t=pathlib.Path(t);src=t/'fixture.json';src.write_text('[\n'+',\n'.join(json.dumps(x,ensure_ascii=False) for x in fixture)+'\n]',encoding='utf-8')
 db=WikiMemory(t/'db',4);stats=db.import_stream(src);a=db.lookup('Q900000001','P31');b=db.lookup('Q900000002');missing=db.lookup('Q999999999');db.close()
 reopened=WikiMemory(t/'db',4);persistent=reopened.lookup('Q900000001','P31')==a;reopened.close()
 assert stats['entities']==2 and stats['statements_seen']==2 and len(a['statements'])==1 and len(b['statements'])==1 and missing['status']=='unknown' and persistent
 result={'stage':38,'mode':'real SQLite sharded implementation; synthetic test FIXTURES only, not a simulated H512 experiment','fixture_entities':2,'fixture_statements':2,'persistent':persistent,'shard_count':4,'unknown_abstains':True,'deprecated_filtered':True,'real_wikidata_entities_imported':0,'checkpoint_weights_updated':False,'wikidata_download_attempt':'HTTPS DNS blocked in runtime','limitations':'Fixture records are intentionally artificial, not Wikipedia/Wikidata knowledge. No real Wikidata dump available in this environment; importer prepared but external ingestion not demonstrated. No H512 inference/training in this stage.'}
 (ROOT/'result.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps(result,ensure_ascii=False,indent=2))
