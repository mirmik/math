#!/usr/bin/env python3
#coding: utf-8

from sympy import *
from sympy.matrices import *
import mpmath

var("v v_z x c x_z T_1 T_2 t g T ksi a b D D1 D2 DD E1 E2 DDD DD1 DD2")

def matrix_discretization(A,B,Step):
	_A = (A * Step).exp()
	_B = A.inv() * (Matrix([[1,0],[0,1]]) - _A) * B
	return (_A,_B)


A = Matrix([[0,1], 
			[-a, -b]]) # собственная матрица

B = Matrix([[0],[-1]]) # входная матрица


pprint(A)
pprint(B)

Ad, Bd = matrix_discretization(A,B,t)

Ad = Ad.subs({
	sqrt(-4*a+b**2)/2:	D
})
Ad = Ad.subs({
	-D-b/2:				D1, 
	D-b/2:				D2
})
Ad = Ad.subs({
	-1/D2 + 1/D1 : 		DD
})

Ad = Ad.subs({
	D1 * D2 * DD : DDD,
	D1 * DD : DD1,
	D2 * DD : DD2
})

pprint(Ad)

Bd = Bd.subs({
	sqrt(-4*a+b**2)/2:	D
})
Bd = Bd.subs({
	-D-b/2:				D1, 
	D-b/2:				D2
})
Bd = Bd.subs({
	-1/D2 + 1/D1 : 		DD
})

Bd = Bd.subs({
	D1 * D2 * DD : DDD,
	D1 * DD : DD1,
	D2 * DD : DD2
})

pprint(Bd)