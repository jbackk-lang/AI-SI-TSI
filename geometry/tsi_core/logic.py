import torch
from torch import nn
OPERATORS=['NOT','AND','OR','XOR','IMPLIES','EQUIV']
class LearnedLogic(nn.Module):
 def __init__(self):
  super().__init__();self.operator=nn.Embedding(len(OPERATORS),8)
  self.evaluate=nn.Sequential(nn.Linear(14,64),nn.Tanh(),nn.Linear(64,64),nn.Tanh(),nn.Linear(64,3))
 def forward(self,left,right,operator):
  return self.evaluate(torch.cat([left,right,self.operator(operator)],-1))
