"""SQLite-sharded Wikidata truthy-statement importer; no synthetic facts or weight training."""
import argparse,bz2,gzip,hashlib,json,sqlite3,pathlib,unicodedata,re

def norm(s):
 return re.sub(r'\s+',' ',unicodedata.normalize('NFC',str(s)).casefold()).strip()

class WikiMemory:
 def __init__(self,root,shards=4):
  self.root=pathlib.Path(root);self.root.mkdir(parents=True,exist_ok=True);self.shards=shards;self.conns=[]
  for i in range(shards):
   c=sqlite3.connect(self.root/f'shard_{i:02}.sqlite')
   c.execute('PRAGMA journal_mode=WAL')
   c.execute('CREATE TABLE IF NOT EXISTS entities(qid TEXT PRIMARY KEY,label TEXT,description TEXT,source TEXT,revision INTEGER)')
   c.execute('CREATE TABLE IF NOT EXISTS statements(qid TEXT,pid TEXT,value TEXT,datatype TEXT,source TEXT,PRIMARY KEY(qid,pid,value))')
   c.execute('CREATE INDEX IF NOT EXISTS stmt_qid_pid ON statements(qid,pid)')
   c.execute('CREATE INDEX IF NOT EXISTS entity_label ON entities(label)')
   self.conns.append(c)
 def shard(self,qid):return self.conns[int(hashlib.sha256(qid.encode()).hexdigest()[:8],16)%self.shards]
 def ingest(self,obj,source='wikidata-dump',languages=('pl','en')):
  qid=obj.get('id','')
  if not re.fullmatch(r'Q[1-9][0-9]*',qid):return 0
  def lang_value(field):
   d=obj.get(field,{})
   for lang in languages:
    if isinstance(d.get(lang),dict):return d[lang].get('value','')
   return ''
  c=self.shard(qid);rev=int(obj.get('lastrevid') or 0)
  c.execute('INSERT INTO entities VALUES(?,?,?,?,?) ON CONFLICT(qid) DO UPDATE SET label=excluded.label,description=excluded.description,source=excluded.source,revision=excluded.revision',(qid,lang_value('labels'),lang_value('descriptions'),source,rev))
  n=0
  for pid,claims in obj.get('claims',{}).items():
   if not re.fullmatch(r'P[1-9][0-9]*',pid):continue
   for claim in claims:
    if claim.get('rank')=='deprecated':continue
    snak=claim.get('mainsnak',{})
    if snak.get('snaktype')!='value':continue
    dv=snak.get('datavalue')
    if not isinstance(dv,dict):continue
    val=dv.get('value')
    if val is None:continue
    val=json.dumps(val,ensure_ascii=False,sort_keys=True,separators=(',',':'))
    c.execute('INSERT OR IGNORE INTO statements VALUES(?,?,?,?,?)',(qid,pid,val,snak.get('datatype',''),source));n+=1
  return n
 def import_stream(self,path,limit=None,source=None):
  path=pathlib.Path(path)
  opener=bz2.open if path.suffix=='.bz2' else gzip.open if path.suffix=='.gz' else open
  n=0;statements=0;errors=0
  with opener(path,'rt',encoding='utf-8') as f:
   for line in f:
    line=line.strip().rstrip(',')
    if not line or line in ('[',']'):continue
    try: obj=json.loads(line)
    except json.JSONDecodeError:errors+=1;continue
    if not isinstance(obj,dict):continue
    statements+=self.ingest(obj,source or f'wikidata-dump:{path.name}');n+=1
    if n%1000==0:self.commit()
    if limit and n>=limit:break
  self.commit();return {'entities':n,'statements_seen':statements,'invalid_lines':errors,'shards':self.shards}
 def commit(self):
  for c in self.conns:c.commit()
 def lookup(self,qid,pid=None):
  if not re.fullmatch(r'Q[1-9][0-9]*',qid):return {'status':'invalid_id'}
  c=self.shard(qid);entity=c.execute('SELECT label,description,source,revision FROM entities WHERE qid=?',(qid,)).fetchone()
  if entity is None:return {'status':'unknown','qid':qid,'statements':[]}
  if pid is not None and not re.fullmatch(r'P[1-9][0-9]*',pid):return {'status':'invalid_property'}
  sql='SELECT pid,value,datatype,source FROM statements WHERE qid=?'+(' AND pid=?' if pid else '')
  rows=c.execute(sql,(qid,pid) if pid else (qid,)).fetchall()
  return {'status':'found' if rows else 'no_statements','qid':qid,'label':entity[0],'description':entity[1],'entity_source':entity[2],'revision':entity[3],'statements':[{'property':p,'value':json.loads(v),'datatype':d,'source':s} for p,v,d,s in rows]}
 def close(self):
  self.commit()
  for c in self.conns:c.close()

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--dump',required=True);p.add_argument('--db',required=True);p.add_argument('--limit',type=int);p.add_argument('--shards',type=int,default=4);a=p.parse_args()
 db=WikiMemory(a.db,a.shards)
 try:print(json.dumps(db.import_stream(a.dump,a.limit),ensure_ascii=False))
 finally:db.close()
