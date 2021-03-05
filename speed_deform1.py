#!/usr/bin/env python3

from sympy import *

var("x0 x1 x2 x3 x4 x5")
var("v0 v1 v2 v3 v4 v5")
var("b a1 a4 c Q R")
var("t t0 t1 t2 t3 t4 t5 t01 t12 t23 t34 t45")

t0 = 0

x0 = 0
x5 = 1

a0 = 0
a2 = 0
a3 = 0
a5 = 0

#v2 = 1
#v3 = 1
#v0 = 0
#v5 = 0
#v4 = v1
#v5 = v0

t01 = Q/2
t45 = R/2

equations = [
	Eq(t1 - t0, t01),
	Eq(t2 - t1, t12),
	Eq(t3 - t2, t23),
	Eq(t4 - t3, t34),
	Eq(t5 - t4, t45),
	Eq(t01, t12),
	Eq(t34, t45),

	Eq(a1, b * t01),
	Eq(a4,-c * t45),

	Eq(v1, v0 + a0*t01 + b*t01**2/2),
	Eq(v2, v1 + a1*t12 - b*t12**2/2),
	Eq(v3, v2 + a2*t23             ),
	Eq(v4, v3 + a3*t34 - c*t34**2/2),
	Eq(v5, v4 + a4*t45 + c*t45**2/2),
	
	Eq(x1, x0 + v0*t01 + a0*t01**2/2 + b*t01**3/6),
	Eq(x2, x1 + v1*t12 + a1*t12**2/2 - b*t12**3/6),
	Eq(x3, x2 + v2*t23 + a2*t23**2/2 + 0*t23**3/6),
	Eq(x4, x3 + v3*t34 + a3*t34**2/2 - c*t34**3/6),
	Eq(x5, x4 + v4*t45 + a4*t45**2/2 + c*t45**3/6),
]

#slv = solve(equations, [x1,x2,t1,t2,v1,t12,a,d], dict=True)
slv = solve(equations, [
	x1,x2,x3,x4,
	v1,v4,
	t1,t2,t3,t4,t5,
	t12,t23,t34,
	a1,a4,b,c
], dict=True)
print(slv[0])
#print(slv[1])
print("size of slv vector:", len(slv))

#slv = [slv[1]]
if (len(slv) != 1):
	raise Exception("size of slv vector is not one")

slv = { k : simplify(v) for k,v in slv[0].items() }

print(slv.keys())


for k,v in slv.items():
	print(k,":", v)

print(0 + v0*t + slv[b]*t**3/6)
print(v0 + slv[b]*t**2/2)
print(simplify(slv[x1] + slv[v1]*t + slv[a1]*t**2 - slv[b]*t**3/6))