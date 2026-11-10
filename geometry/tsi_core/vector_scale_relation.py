import torch
from vector_geometric_relation import VectorGeometricRelation
class VectorScaleInvariantRelation(VectorGeometricRelation):
 """Common pair scaling preserves relative lengths; category remains learned NN output."""
 @staticmethod
 def normalize_pair(left,right):
  scale=((left.square().sum(-1)+right.square().sum(-1))+1e-24).sqrt().unsqueeze(-1)
  return left/scale,right/scale
 def relation_vector(self,left,right):
  a,b=self.normalize_pair(left,right)
  return super().relation_vector(a,b)
