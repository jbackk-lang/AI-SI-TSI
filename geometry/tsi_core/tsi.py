from pathlib import Path
import argparse,json,hashlib,torch
from network import TSINetwork,collate
LABELS=['prawda','fałsz','nieznane']
class TSI:
 def __init__(self,checkpoint=None):
  torch.set_num_threads(1);path=Path(checkpoint) if checkpoint else Path(__file__).parent/'artifacts/candidate_150.pt'
  cp=torch.load(path,map_location='cpu',weights_only=True);self.contract=cp['contract'];self.model=TSINetwork(width=cp['spec']['width'],max_name=self.contract['max_name'],max_facts=self.contract['max_facts']);self.model.load_state_dict(cp['weights']);self.model.eval();self.checkpoint_sha256=hashlib.sha256(path.read_bytes()).hexdigest()
 def reply(self,facts,query):
  if len(facts)>self.contract['max_facts']:raise ValueError('Too many facts for this frozen TSI contract')
  mapping={**{v:k for k,v in enumerate(LABELS)},'falsz':1};records=[(name,mapping[value] if isinstance(value,str) else value) for name,value in facts]
  with torch.inference_mode():logits,scores,attention=self.model(*collate([dict(facts=records,query=query)],self.contract['max_name']));p=logits.softmax(-1)[0]
  return dict(name='timderSI',short_name='TSI',answer=LABELS[int(p.argmax())],probabilities=dict(zip(LABELS,p.tolist())),memory_attention=attention[0].tolist(),verified=False,scope='structured facts and query name',checkpoint_sha256=self.checkpoint_sha256)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--facts',required=True,help='JSON list of [name,state]');parser.add_argument('--query',required=True);args=parser.parse_args();print(json.dumps(TSI().reply(json.loads(args.facts),args.query),ensure_ascii=False,indent=2))
