"""Synthetic fixtures, NOT authentic Wikidata; tests real database and retrieval."""
import json,tempfile,pathlib
from search import WikiSearch
def entity(qid,label,aliases,pid,value):
 return {'id':qid,'lastrevid':1,'labels':{'pl':{'value':label}},'aliases':{'pl':[{'value':a} for a in aliases]},'claims':{pid:[{'rank':'normal','mainsnak':{'snaktype':'value','datatype':'string','datavalue':{'value':value}}}]}}
rows=[entity('Q900000001','Obiekt Alfa',['Pierwszy obiekt'],'P900','wartosc alfa'),entity('Q900000002','Obiekt Beta',['Drugi obiekt'],'P900','wartosc beta'),entity('Q900000003','Obiekt Gamma',['Wspolna nazwa'],'P900','wartosc gamma'),entity('Q900000004','Obiekt Delta',['Wspolna nazwa'],'P900','wartosc delta')]
with tempfile.TemporaryDirectory() as t:
 root=pathlib.Path(t);dump=root/'fixture.json';dump.write_text('[\n'+',\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n]',encoding='utf-8')
 db=WikiSearch(root/'db');imp=db.import_stream(dump)
 cases=[('Obiekt Alfa','P900','found'),('pierwszy obiekt','P900','found'),('OBIEKT BETA','P900','found'),('Wspolna nazwa','P900','ambiguous'),('Obiekt Alfa','P901','unknown_property'),('Nieistniejacy','P900','unknown_entity'),('Obiekt Gamma','P900','found'),('Obiekt Delta','P900','found')]
 results=[{'query':q,'property':p,'expected':expected,'actual':db.answer(q,p)['status']} for q,p,expected in cases]
 db.close();db=WikiSearch(root/'db');persistent=db.answer('Obiekt Alfa','P900')['status']=='found';db.close()
 assert all(r['expected']==r['actual'] for r in results) and persistent
 output={'stage':39,'dataset':'4 artificial test fixtures; NOT Wikidata facts','entities_imported_from_real_wikidata':0,'fixture_entities':imp['entities'],'tests_passed':sum(r['expected']==r['actual'] for r in results),'tests_total':len(results),'persistent':persistent,'h512_training':False,'h512_inference':False,'results':results}
 (pathlib.Path(__file__).parent/'result.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(output,ensure_ascii=False,indent=2))
