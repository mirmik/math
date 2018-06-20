#!/usr/bin/python
#coding: utf-8

import numpy as np
import random

A = np.array([

	[  6, 0, 1],
	[  6, 1, 1],
	[  6, 2, 1],
	[  6, 3, 1],
	[  6, 4, 1],
	[  6, 5, 1],

	[  0, 0, 1],
	[  0, 1, 1],
	[  0, 2, 1],
	[  0, 3, 1],
	[  0, 4, 1],
	[  0, 5, 1],
	
	[  1, 0, 1],
	[  1, 1, 1],
	[  1, 2, 1],
	[  1, 3, 1],
	[  1, 4, 1],
	[  1, 5, 1],

	[  2, 0, 1],
	[  2, 1, 1],
	[  2, 2, 1],
	[  2, 3, 1],
	[  2, 4, 1],
	[  2, 5, 1],

	[  3, 0, 1],
	[  3, 1, 1],
	[  3, 2, 1],
	[  3, 3, 1],
	[  3, 4, 1],
	[  3, 5, 1],

	[  4, 0, 1],
	[  4, 1, 1],
	[  4, 2, 1],
	[  4, 3, 1],
	[  4, 4, 1],
	[  4, 5, 1],

	[  5, 0, 1],
	[  5, 1, 1],
	[  5, 2, 1],
	[  5, 3, 1],
	[  5, 4, 1],
	[  5, 5, 1],
])

T = 0.02

Y = np.array([
	6.25 + 12 + random.uniform(-T, T),
	6.50 + 12 + random.uniform(-T, T),
	6.75 + 12 + random.uniform(-T, T),
	7.00 + 12 + random.uniform(-T, T),
	7.25 + 12 + random.uniform(-T, T),
	7.50 + 12 + random.uniform(-T, T),

	0.25 + random.uniform(-T, T),
	0.50 + random.uniform(-T, T),
	0.75 + random.uniform(-T, T),
	1.00 + random.uniform(-T, T),
	1.25 + random.uniform(-T, T),
	1.50 + random.uniform(-T, T),
	
	3.25 + random.uniform(-T, T),
	3.50 + random.uniform(-T, T),
	3.75 + random.uniform(-T, T),
	4.00 + random.uniform(-T, T),
	4.25 + random.uniform(-T, T),
	4.50 + random.uniform(-T, T),

	6.25 + random.uniform(-T, T),
	6.50 + random.uniform(-T, T),
	6.75 + random.uniform(-T, T),
	7.00 + random.uniform(-T, T),
	7.25 + random.uniform(-T, T),
	7.50 + random.uniform(-T, T),

	6.25 + 3 + random.uniform(-T, T),
	6.50 + 3 + random.uniform(-T, T),
	6.75 + 3 + random.uniform(-T, T),
	7.00 + 3 + random.uniform(-T, T),
	7.25 + 3 + random.uniform(-T, T),
	7.50 + 3 + random.uniform(-T, T),

	6.25 + 6 + random.uniform(-T, T),
	6.50 + 6 + random.uniform(-T, T),
	6.75 + 6 + random.uniform(-T, T),
	7.00 + 6 + random.uniform(-T, T),
	7.25 + 6 + random.uniform(-T, T),
	7.50 + 6 + random.uniform(-T, T),

	6.00 + 9 + random.uniform(-T, T),
	6.00 + 9 + random.uniform(-T, T),
	6.00 + 9 + random.uniform(-T, T),
	6.00 + 9 + random.uniform(-T, T),
	6.00 + 9 + random.uniform(-T, T),
	6.00 + 9 + random.uniform(-T, T),

])

At = A.transpose()
AA = At.dot(A)
AAinv = np.linalg.inv(AA)
AAinv_x_t = AAinv.dot(At)
AAinv_x_t_x_y = AAinv.dot(At).dot(Y)


print("At =")
print(At)
print("AA =")
print(AA)
print("AAinv =")
print(AAinv)
print("AAinv * At =")
print(AAinv_x_t)
print("AAinv * At * y =")
print(AAinv_x_t_x_y)

print()

res = np.array([3,0.25,0.25])

v = np.array([ 0, 0, 0])

for i, x in enumerate(A):

	p = v.dot(x)
	y = Y[i]#

	e = y - p

	v = v + e / x.dot(x) * x
	#print("r:{} new v:{}".format(r,v))
	print("{}, {}".format(v, p))
	#print("should be zero: {}".format((v - res).dot(x)))
	if ((i % 6) == 5): print()
