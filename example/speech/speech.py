import torch
from torch import nn
import IStudio as iv

studio = iv.AIStudio("pytorch")

model = nn.Sequential()
model.add_module('W0', nn.Linear(8, 16))
model.add_module('tanh', nn.Tanh())
model.add_module('W1', nn.Linear(16, 1))

x = torch.randn(1,8)

studio.RecordGraphDef(model(x), "speech", dict(list(model.named_parameters()) + [('x', x)]))
