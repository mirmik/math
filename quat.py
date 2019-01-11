#!/usr/bin/env python3
#coding: utf-8

import sympy
from sympy import *

q0,q1,q2,q3,v0,v1,v2=sympy.symbols("q0 q1 q2 q3 v0 v1 v2")
i, j, k = symbols("i j k", commutative=0)

ss = sympy.expand((q0+q1*i+q2*j+q3*k)*(v0*i+v1*j+v2*k)*(q0-q1*i-q2*j-q3*k))

ss = ss.subs(i**3, -i).subs(j**3, -j).subs(k**3, -k)
ss = ss.subs(i**2, -1).subs(j**2, -1).subs(k**2, -1)
ss = ss.subs(i*j*k, -1)
ss = ss.subs(i*j, k).subs(j*i,-k).subs(j*k, i).subs(k*j,-i).subs(k*i, j).subs(i*k,-j)

ss = ss.subs(i**3, -i).subs(j**3, -j).subs(k**3, -k)
ss = ss.subs(i**2, -1).subs(j**2, -1).subs(k**2, -1)
ss = ss.subs(i*j*k, -1)
ss = ss.subs(i*j, k).subs(j*i,-k).subs(j*k, i).subs(k*j,-i).subs(k*i, j).subs(i*k,-j)

#ss = sympy.collect(ss, syms=(v0*i, v0*j, v0*k, v1*i, v1*j, v1*k, v2*i, v2*j, v2*k))
#ss = ss.subs(q0**2 + q1**2 + q2**2 + q3**2, 1)
#ss = expand(ss)
#pprint(ss)
#ss = ss.subs(i**2, -1).subs(j**2, -1).subs(k**2, -1)

pprint(sympy.collect(ss, syms=(i,j,k)))
print(sympy.collect(ss, syms=(i,j,k)))

print(ss.collect((i,j,k)).coeff(i).collect((v0,v1,v2)))
print(ss.collect((i,j,k)).coeff(j).collect((v0,v1,v2)))
print(ss.collect((i,j,k)).coeff(k).collect((v0,v1,v2)))

