#!/usr/bin/env python3

import sys
from sympy import *

v=var("x0 x1 x2 x3 v0 v1 v2 a d t0 t1 t2 t3 t01 t12 t23")

if len(sys.argv) > 1 and sys.argv[1] == "reducted":
	t23 = t01
	v0 = 0
	v2 = 0
	
t0 = 0

x0 = 0
x3 = 1

#t3 = 1
#v1 = 1

equations = [
	Eq(x1, x0 + v0*t01 + a*t01**2/2),
	Eq(x2, x1 + v1*t12),
	Eq(x3, x2 + v1*t23 + d*t23**2/2),
	Eq(v1, v0 + a * t01),
	Eq(v2, v1 + d * t23),

	Eq(t1 - t0, t01),
	Eq(t2 - t1, t12),
	Eq(t3 - t2, t23)
]

#slv = solve(equations, [x1,x2,t1,t2,v1,t12,a,d], dict=True)
slv = solve(equations, [x1,x2,t1,t2,t3,t12,a,d], dict=True)
print("size of slv vector:", len(slv))
if (len(slv) != 1):
	raise Exception("size of slv vector is not one")

slv = { k : simplify(v) for k,v in slv[0].items() }

#pprint(slv)

for k,v in slv.items():
	print(k,":", v)