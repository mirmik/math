#!/usr/bin/env python3
#coding: utf-8

import numpy

arr = numpy.matrix([
	[1,0.5,0,1],
	[-0.5,1,0,1],
	[0,0,1,1],
	[0,0,0,1],
])


print(numpy.linalg.inv(arr))