import torch
from torch import nn
class VectorRelationReadout(nn.Module):
 """Two entity vectors -> learned third relation vector; existing core stays frozen."""
 def __init__(self,core):
  super().__init__();self.core=core
  for p in core.parameters():p.requires_grad_(False)
  self.relation_head=nn.Sequential(nn.Linear(2*core.expansion_width,96),nn.Tanh(),nn.Linear(96,96));nn.init.zeros_(self.relation_head[-1].weight);nn.init.zeros_(self.relation_head[-1].bias)
 def train(self,mode=True):super().train(mode);self.core.eval();return self
 def relation_vector(self,left,right):
  if left.shape!=right.shape or left.ndim!=2 or left.shape[-1]!=96:raise ValueError('Expected two Bx96 entityvectors')
  if not torch.isfinite(left).all() or not torch.isfinite(right).all():raise ValueError('Nonfinite entities')
  with torch.no_grad():_,h=self.core.expansion_context(torch.stack([left,right],1));features=torch.cat([h[-2],h[-1]],-1)
  return self.relation_head(features)
