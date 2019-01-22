#!/usr/bin/env python3
#coding: utf-8

from sympy import *
import evalcache

lazy = evalcache.Lazy(".evalcache")
solve = lazy(solve)

var("beta q(0:3) l1 l2 z r x y h z q1q2")

#eq1 = Eq(r, sqrt(l2*sin(q2))**2 + (l1+l2*cos(q2))**2)
#eq2 = Eq(beta, q1+atan2(l2*sin(q2), l1+l2*cos(q2)))

#slv = solve([eq1,eq2], [q1,q2])
#slv0 = slv[0]

#h = sqrt(x**2 + y**2)

#pprint(Eq(q0, atan2(y,x)))
#pprint(Eq(q1, slv0[0].subs({beta:atan2(z, h), r:sqrt(z**2+h**2)})))
#pprint(Eq(q2, slv0[1].subs({beta:atan2(z, h), r:sqrt(z**2+h**2)})))

eq1 = Eq(h, sin(q1)*l1 + sin(q1q2)*l2)
eq2 = Eq(z, cos(q1)*l1 + cos(q1q2)*l2)

slv = solve([eq1, eq2], [q1, q1q2])

pprint(slv.unlazy())
pprint(slv[0].unlazy())

print("slv[0]:")
pprint(slv[0][0].unlazy())
pprint(slv[0][1].unlazy())

print("slv[1]:")
pprint(slv[1][0].unlazy())
pprint(slv[1][1].unlazy())

print("slv[bb]:")
pprint(slv[0][1].unlazy().factor())
pprint(slv[1][1].unlazy().factor())
