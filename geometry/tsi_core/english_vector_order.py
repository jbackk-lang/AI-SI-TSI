from english_vector_command import EnglishVectorCommand
from torch import nn
class EnglishVectorOrder(EnglishVectorCommand):
 def __init__(self):
  super().__init__();self.output=nn.Linear(64,2)
