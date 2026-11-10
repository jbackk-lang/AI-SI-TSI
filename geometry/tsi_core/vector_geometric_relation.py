import torch
from geometry_numeric import safe_cosine
from torch import nn
from vector_relation_readout import VectorRelationReadout
class VectorGeometricRelation(VectorRelationReadout):
 """Learned residual relation from numerical geometry, no comparison rules at inference."""
 def __init__(self,core,old_head_state,feature_mean,feature_std):
  super().__init__(core);self.relation_head.load_state_dict(old_head_state)
  for p in self.relation_head.parameters():p.requires_grad_(False)
  self.geometry_head=nn.Sequential(nn.Linear(4,32),nn.Tanh(),nn.Linear(32,96));nn.init.zeros_(self.geometry_head[-1].weight);nn.init.zeros_(self.geometry_head[-1].bias)
  self.register_buffer('feature_mean',feature_mean.clone());self.register_buffer('feature_std',feature_std.clone().clamp_min(1e-6))
 @staticmethod
 def geometry(left,right):
  if left.shape != right.shape:
   raise ValueError('Geometry vectors must have identical shapes')
  if not torch.isfinite(left).all() or not torch.isfinite(right).all():
   raise ValueError('Geometry vectors must be finite')
  ln=left.norm(dim=-1);rn=right.norm(dim=-1)
  dot=(left*right).sum(-1)
  cos,_=safe_cosine(left,right)
  cos=cos.squeeze(-1)
  return torch.stack([ln,rn,dot,cos],-1)
 def relation_vector(self,left,right):
  old=super().relation_vector(left,right).detach();features=(self.geometry(left,right)-self.feature_mean)/self.feature_std
  return old+self.geometry_head(features)
