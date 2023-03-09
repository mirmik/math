#!/usr/bin/env python3

import matplotlib.pyplot as plt
from scipy.special import softmax
import numpy as np
from pprint import pprint

x = np.linspace(0, 10, 100)
y = 1 - x

xy = list(zip(x, y))
xys = [softmax(xy) for xy in xy]

xs = [xy[0] for xy in xys]
ys = [xy[1] for xy in xys]

# Plot the softmax function
plt.plot(x, ys)
plt.show()