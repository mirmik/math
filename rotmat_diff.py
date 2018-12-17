#!/usr/bin/env python3
#coding: utf-8

from sympy import *

x,y,z,a = symbols("x y z a")

M = Matrix([
	[	cos(a)+(1-cos(a))*x**2,		(1-cos(a))*x*y-(sin(a))*z,  (1-cos(a))*x*z+(sin(a)*y)	],
	[	(1-cos(a))*y*x+(sin(a))*z, 	cos(a)+(1-cos(a))*y**2, 	(1-cos(a))*y*z-(sin(a)*x)	],
	[	(1-cos(a))*z*x-(sin(a))*y, 	(1-cos(a))*z*y+(sin(a))*x,	cos(a)+(1-cos(a))*z**2		]
])

DM = diff(M, a)

pprint(DM)