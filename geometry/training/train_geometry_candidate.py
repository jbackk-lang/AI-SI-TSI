import torch,json,hashlib
from pathlib import Path
from language_vector_geometry import relation_features
R=Path(__file__).parent;torch.set_num_threads(1);torch.manual_seed(20261110)
def batch(n,seed):
 g=torch.Generator().manual_seed(seed);label=torch.arange(n)%4
 a=torch.randn(n,16,generator=g,dtype=torch.float64);a=a/torch.linalg.vector_norm(a,dim=-1,keepdim=True)
 u=torch.randn(n,16,generator=g,dtype=torch.float64);u=u-(u*a).sum(-1,keepdim=True)*a;u=u/torch.linalg.vector_norm(u,dim=-1,keepdim=True)
 c=torch.where(label[:,None]==0,torch.ones(n,1),torch.where(label[:,None]==2,-torch.ones(n,1),torch.zeros(n,1))).double()
 b=c*a+torch.sqrt((1-c*c).clamp_min(0))*u
 b[label==3]=0
 scales=torch.pow(10.,-12+24*torch.rand(n,1,generator=g,dtype=torch.float64));a=a*scales;b=b*scales
 f=relation_features(a,b)
 x=torch.cat([f['cosine'],f['cosine_valid'].double(),f['relative_length']],-1)
 return x.float(),label
x,y=batch(4096,101);xt,yt=batch(1024,991)
net=torch.nn.Sequential(torch.nn.Linear(3,24),torch.nn.Tanh(),torch.nn.Linear(24,4));opt=torch.optim.Adam(net.parameters(),lr=.01)
for step in range(160):
 opt.zero_grad();loss=torch.nn.functional.cross_entropy(net(x),y);loss.backward();opt.step()
with torch.no_grad():pred=net(xt).argmax(-1);acc=float((pred==yt).float().mean());per=[int(((pred==yt)&(yt==i)).sum()) for i in range(4)]
report={'scope':'isolated geometric relation classifier candidate, not TSI active core','train_samples':4096,'holdout_samples':1024,'accuracy':acc,'correct_per_class_out_of_256':per,'steps':160,'seed':20261110}
torch.save({'state_dict':net.state_dict(),'report':report},R/'geometry_candidate.pt');(R/'geometry_training_report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
