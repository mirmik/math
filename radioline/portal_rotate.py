#!/usr/bin/env python3

from sympy import *
from sympy.algebras.quaternion import Quaternion

var("q0 q3 p0 p1 i j k x y z")

Q = Quaternion(q0, 0, 0, q3)
P = Quaternion(p0, p1, 0, 0)
Qs = conjugate(Q)
Ps = conjugate(P)

pprint(Qs)

ee = Q*P*Quaternion(0,0,0,1)*Ps*Qs
e = ee.a + ee.b * i + ee.c * j + ee.d * k

pprint(simplify(e))

res = solve(
	(
		Eq(ee.b, x), Eq(ee.c, y), Eq(ee.d, z),
		Eq(x**2 + y**2 + z**2, 1),
		Eq(p0**2 + p1**2, 1),
		Eq(q0**2 + q3**2, 1),
	),
	(p1, q3)
)

pprint(res)