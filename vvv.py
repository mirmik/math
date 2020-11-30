#!/usr/bin/env python3

from sympy import *

var("wx wy wz x y z ex ey ez")

e = Matrix([ex,ey,ez])
w = Matrix([wx,wy,wz])
r = Matrix([x,y,z])

rr = w.cross(w.cross(r))

pprint(e.cross(r))
pprint(rr.expand())