#!/usr/bin/env python3

import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt

x = numpy.linspace(6, 8, 1000)
y = 4**(x**2 - 14*x + 50)

plt.plot(x, y)
plt.show()