import torch
from torch import nn
class VectorRelationComposition(nn.Module):
 """Learned qualitative composition; no relation rule table in inference."""
 def __init__(self):
  super().__init__();self.vector=nn.Sequential(nn.Linear(192,64),nn.Tanh(),nn.Linear(64,96));self.readout=nn.Linear(96,4)
 def forward(self,ab,bc):
  v=self.vector(torch.cat([ab,bc],-1));return v,self.readout(v)
