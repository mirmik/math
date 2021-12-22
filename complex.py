#!/usr/bin/env python3

import sympy

def complex_symplify(A):
	while True:
		last_A = A
		A = A.subs(i*j, k)
		A = A.subs(j*k, i)
		A = A.subs(k*i, j)
		A = A.subs(j*i, -k)
		A = A.subs(k*j, -i)
		A = A.subs(i*k, -j)
		if A == last_A:
			break
	return A


sympy.var("x y z w a b")

i=sympy.Symbol('i', commutative=False)
j=sympy.Symbol('j', commutative=False)
k=sympy.Symbol('k', commutative=False)

A = (w+z*k)*(a*i+b*j)*(w-z*k)
A = sympy.expand(A)
print(A)
A = complex_symplify(A)
print(A)
A = sympy.simplify(A)
print(A)