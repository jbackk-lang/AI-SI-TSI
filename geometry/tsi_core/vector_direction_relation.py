import torch
from torch import nn
from vector_scale_relation import VectorScaleInvariantRelation
from vector_geometric_relation import VectorGeometricRelation
class VectorDirectionRelation(nn.Module):
 def __init__(self):
  super().__init__();self.network=nn.Sequential(nn.Linear(4,32),nn.Tanh(),nn.Linear(32,96))
 def forward(self,left,right):
  a,b=VectorScaleInvariantRelation.normalize_pair(left,right);return self.network(VectorGeometricRelation.geometry(a,b))
