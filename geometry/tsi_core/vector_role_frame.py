import torch
from torch import nn
class VectorRoleFrame(nn.Module):
 """Neural retrieval using supplied role context, not inferred payload categories."""
 def __init__(self):
  super().__init__();self.keys=nn.Embedding(3,16);self.queries=nn.Embedding(3,16)
 def forward(self,payloads,roles,query):
  logits=(self.keys(roles)*self.queries(query)[:,None,:]).sum(-1)/4
  weights=logits.softmax(-1);return (weights[:,:,None]*payloads).sum(1),logits
