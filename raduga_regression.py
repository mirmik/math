#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as plt 

t = numpy.array([-30,-20,-10,0,10,20,30])
x = numpy.array([-29.9861, -19.9885, -9.9908, 0,9.9978, 19.9971, 30.002])

#t = t[:6]
#x = x[:6]

t = t
x = x

y = (0.0013*2/3)*t

plt.plot(t,x-t)
plt.show()