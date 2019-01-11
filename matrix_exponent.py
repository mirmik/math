#!/usr/bin/env python3
#coding: utf-8

from sympy import *
from sympy.matrices import *

var("a b c d")

A = Matrix([[2,-1,1], 
			[0,3,-1],
			[2,1,3]]) # собственная матрица

pprint(A.exp())
pprint(A.inv().exp())