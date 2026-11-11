"""Report real on-disk SQLite bytes, counts and WAL/SHM; no size extrapolation."""
import argparse,json,pathlib,sqlite3
def measure(root):
 root=pathlib.Path(root);shards=sorted(root.glob('shard_*.sqlite'))
 if not shards:return {'status':'no_database','database_bytes':0,'entities':0,'statements':0,'names':0,'shards':0}
 out={'status':'ok','shards':len(shards),'entities':0,'statements':0,'names':0,'database_bytes':0,'file_bytes':0,'files':[]}
 for p in shards:
  c=sqlite3.connect(f'file:{p}?mode=ro',uri=True);counts={}
  for table in ('entities','statements','names'):
   exists=c.execute('SELECT 1 FROM sqlite_master WHERE type="table" AND name=?',(table,)).fetchone()
   counts[table]=c.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0] if exists else 0
   out[table]+=counts[table]
  out['database_bytes']+=c.execute('PRAGMA page_count').fetchone()[0]*c.execute('PRAGMA page_size').fetchone()[0];c.close()
  related=[x for x in (p,p.with_name(p.name+'-wal'),p.with_name(p.name+'-shm')) if x.exists()]
  size=sum(x.stat().st_size for x in related);out['file_bytes']+=size
  out['files'].append({'shard':p.name,'bytes':size,**counts})
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('db');a=p.parse_args();print(json.dumps(measure(a.db),ensure_ascii=False,indent=2))
