#!/usr/bin/env python3
#coding: utf-8

from sympy import *
import evalcache

var("beta q(0:3) l1 l2 z r x y z")

eq1 = Eq(r, l1 + l2*cos(q2))
eq2 = Eq(beta, q1+l2*sin(q2)/l1)

slv = solve([eq1,eq2], [q1,q2])
slv0 = slv[0]

h = sqrt(x**2 + y**2)

pprint(Eq(q0, atan2(y,x)))
pprint(Eq(q1, slv0[0].subs({beta:atan2(z, h), r:sqrt(z**2+h**2)})))
pprint(Eq(q2, slv0[1].subs({beta:atan2(z, h), r:sqrt(z**2+h**2)})))
