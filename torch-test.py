#!/usr/bin/env python3

import torch
import math
import matplotlib.pyplot as plt

# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 3)
y = torch.sin(x)

# For this example, the output y is a linear function of (x, x^2, x^3), so
# we can consider it as a linear layer neural network. Let's prepare the
# tensor (x, x^2, x^3).
p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)

print(x)
print(x.unsqueeze(-1))