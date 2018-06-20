#!/usr/bin/python
#coding: utf-8

import numpy as np

A = np.array([
	[  0, 2, 1], 
	[  1, 3, 1], 
	[  2, 4, 1], 
	[  0, 5, 1], 
	[-10, 6, 1],
])

y = np.array = [0, 1, 2, 3, 4]

At = A.transpose()
AA = At.dot(A)
AAinv = np.linalg.inv(AA)
AAinv_x_t = AAinv.dot(At)
AAinv_x_t_x_y = AAinv.dot(At).dot(y)


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