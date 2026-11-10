"""Isolated, opt-in learned geometry relation classifier for TSI."""
from pathlib import Path
import hashlib
import torch
from language_vector_geometry import relation_features

EXPECTED_SHA = "c253c857486a7b5eb248b8f254956f5c565445f3445b8ea79ff15d6a9e3c7343"
LABELS = ('parallel','orthogonal','opposite','undefined')

def classify_geometry(left,right):
    a=torch.as_tensor(left,dtype=torch.float64).reshape(1,-1)
    b=torch.as_tensor(right,dtype=torch.float64).reshape(1,-1)
    if a.shape!=b.shape or a.shape[-1]!=16 or not torch.isfinite(a).all() or not torch.isfinite(b).all():
        raise ValueError('Expected two finite 16-dimensional vectors')
    f=relation_features(a,b)
    x=torch.cat([f['cosine'],f['cosine_valid'].to(torch.float64),f['relative_length']],dim=-1).float()
    path=Path(__file__).with_name('geometry_candidate.pt')
    if hashlib.sha256(path.read_bytes()).hexdigest()!=EXPECTED_SHA:
        raise ValueError('Geometry checkpoint SHA mismatch')
    cp=torch.load(path,map_location='cpu',weights_only=True)
    net=torch.nn.Sequential(torch.nn.Linear(3,24),torch.nn.Tanh(),torch.nn.Linear(24,4))
    net.load_state_dict(cp['state_dict'],strict=True)
    net.eval()
    with torch.no_grad():
        probs=net(x).softmax(-1)[0]
    return {'relation':LABELS[int(probs.argmax())], 'probabilities':probs.tolist(),
            'verified':False,'scope':'synthetic 16D candidate; not validated for general TSI vectors'}
