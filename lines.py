#!/usr/bin/env python3
#coding: utf-8

from sympy import *

x1, y1, z1, o1, p1, s1, t1, x2, y2, z2, o2, p2, s2, t2 = symbols("x1, y1, z1, o1, p1, s1, t1, x2, y2, z2, o2, p2, s2, t2")

s = sqrt(
		((x1 + o1 * t1) - (o2 * t2))**2 +
		((y1 + p1 * t1) - (p2 * t2))**2 +
		((z1 + s1 * t1) - (s2 * t2))**2
	)

d1 = diff(s,t1)
d2 = diff(s,t2)

slv = solve((d1,d2, Eq(o1**2+p1**2+s1**2,1)),(t1,t2))

print(s)
print()
print(d1)
print()
print(d2)
print()
print(slv)