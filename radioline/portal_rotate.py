#!/usr/bin/env python3

from sympy import *
from sympy.algebras.quaternion import Quaternion

import sys

var("q0 q1 q2 q3 p0 p1 p2 p3 i j k x y z yz xz psi phi")

#Q = Quaternion(q0, 0, 0, q3)
#P = Quaternion(p0, p1, 0, 0)
Q = Quaternion(q0, 0, 0, q3)
P = Quaternion(p0, p1, 0, 0)
Qs = conjugate(Q)
Ps = conjugate(P)

#pprint(Qs)
R = P*Q
ee = (R)*Quaternion(0,0,1,0)*conjugate(R)
#a = (P)*Quaternion(0,0,1,0)*conjugate(P)
e = ee.a + ee.b * i + ee.c * j + ee.d * k

#pprint(simplify(a))
pprint(simplify(e))

#eee = solve(Eq(2*p1*sqrt(1-p1), z), (p1))
#pprint(eee)

#pprint(solve(Eq(4*q0**4 - 4*yz*q0**2 - xz**2), (q0)))

Q = Quaternion(cos(phi/2), x*sin(phi/2), y*sin(phi/2), 0)
P = Quaternion(cos(psi/2), 0, 0, sin(psi/2))

e = Q*P

ee = e * (Quaternion(0,1,0,0)) * conjugate(e)

#e = ee.a + ee.b * i + ee.c * j + ee.d * k

#pprint(ee)
#print()
#pprint(e)
from sympy.simplify.fu import *

print("qw:")
pprint(simplify(e.a))
print("qx:")
pprint(simplify(e.b))
print("qy:")
pprint(simplify(e.c))
print("qz:")
pprint(simplify(e.d))

print("x:")
pprint(simplify(ee.b))
print("y:")
pprint(
	trigsimp(
	collect(expand(ee.c), syms=[sin(psi/2)*cos(psi/2), 2*x*y*sin(phi/2)**2])))
print("z:")
pprint(simplify(ee.d))
