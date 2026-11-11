"""Name retrieval over WikiMemory SQLite shards; deterministic lexical baseline, not H512."""
import re
from wikimemory import WikiMemory,norm
class WikiSearch(WikiMemory):
 def __init__(self,root,shards=4):
  super().__init__(root,shards)
  for c in self.conns:
   c.execute('CREATE TABLE IF NOT EXISTS names(qid TEXT,lang TEXT,kind TEXT,name TEXT,name_norm TEXT,PRIMARY KEY(qid,lang,kind,name))')
   c.execute('CREATE INDEX IF NOT EXISTS names_norm ON names(name_norm)')
 def ingest(self,obj,source='wikidata-dump',languages=('pl','en')):
  n=super().ingest(obj,source,languages);qid=obj.get('id','')
  if not re.fullmatch(r'Q[1-9][0-9]*',qid):return n
  c=self.shard(qid);c.execute('DELETE FROM names WHERE qid=?',(qid,))
  for lang in languages:
   label=obj.get('labels',{}).get(lang)
   if isinstance(label,dict) and label.get('value'):
    s=label['value'];c.execute('INSERT OR IGNORE INTO names VALUES(?,?,?,?,?)',(qid,lang,'label',s,norm(s)))
   for alias in obj.get('aliases',{}).get(lang,[]):
    if isinstance(alias,dict) and alias.get('value'):
     s=alias['value'];c.execute('INSERT OR IGNORE INTO names VALUES(?,?,?,?,?)',(qid,lang,'alias',s,norm(s)))
  return n
 def search(self,query,limit=10):
  q=norm(query)
  if not q:return []
  hits=[]
  for c in self.conns:
   for qid,lang,kind,name in c.execute('SELECT qid,lang,kind,name FROM names WHERE name_norm=?',(q,)):
    hits.append({'qid':qid,'language':lang,'kind':kind,'matched_name':name,'score':2 if kind=='label' else 1})
  hits.sort(key=lambda x:(-x['score'],x['qid'],x['language']))
  return hits[:limit]
 def answer(self,name,pid):
  hits=self.search(name)
  if not hits:return {'status':'unknown_entity','query':name,'evidence':[]}
  qids=sorted({x['qid'] for x in hits if x['score']==hits[0]['score']})
  if len(qids)!=1:return {'status':'ambiguous','query':name,'candidates':qids,'evidence':[]}
  result=self.lookup(qids[0],pid)
  if result['status']!='found':return {'status':'unknown_property','qid':qids[0],'property':pid,'evidence':[]}
  return {'status':'found','qid':qids[0],'property':pid,'values':[x['value'] for x in result['statements']],'evidence':[{'source':x['source'],'qid':qids[0],'pid':pid,'revision':result['revision']} for x in result['statements']]}
