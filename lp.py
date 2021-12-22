#!/usr/bin/env python3

import numpy


A = numpy.array([
	[0, 0, 2, 0, 0 ,0],
	[2, 0, 0, 0 ,0 ,0],
	[1, 1, 1, 0, 0, 0],
	[1 ,0 ,0, 1, 0, 0],
	[0 ,1, 0, 0, 1, 0],
	[0, 0, 1, 0, 0, 1]
])

A = numpy.array([
	[0, 0, 2, 2],
	[2, 0, 0, 2],
	[1, 1, 1, 1]
])

b = numpy.array([1, 0.5, 1]).transpose()

x = numpy.linalg.solve(A, b)

print(x)