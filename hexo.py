#!/usr/bin/env python3
#coding: utf-8

from sympy import *
import evalcache

lazy = evalcache.Lazy(".evalcache")

solve = lazy(solve)

var("alpha beta q(0:3) l0 l1 l2 z r")

#M1 = Matrix([[cos(q1),-sin(q1)],[sin(q1),cos(q1)]])
#M2 = Matrix([[cos(q1),-sin(q1)],[sin(q1),cos(q1)]])

#ll = M1*Matrix([[0],[l0]]) + M2*M1*Matrix([[0],[l1]])

#pprint(ll)

eq0 = Eq(alpha, q0)
eq1 = Eq(r, l1 + l2*cos(q2))
eq2 = Eq(beta, q1+l2*sin(q2)/l1)

slv = solve([eq1,eq2], [q1,q2])
slv0 = slv[0]
slv1 = slv[1]
#slv2 = slv[2]

slv.unlazy()
slv0 = slv[0]

pprint(slv0.unlazy())
#pprint(slv0.unlazy())
#pprint(slv1.unlazy())
#pprint(slv0[0].unlazy())
#pprint(slv0[1].unlazy())
#pprint(slv1[0].unlazy())
#pprint(slv1[1].unlazy())
#pprint(slv2.unlazy())