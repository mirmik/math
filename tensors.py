#!/usr/bin/env python3

import sympy

sympy.var("xy yz xz a11 a12 a13 a22 a23 a33 r11 r12 r13 r21 r22 r23 r31 r32 r33 a R r M F")



J = sympy.Matrix([
	[a11,a12,a13],
	[a12,a22,a23],
	[a13,a23,a33]])

RR = sympy.Matrix([
	[sympy.cos(a),-sympy.sin(a),0],
	[sympy.sin(a),sympy.cos(a),0],
	[0,0,1]])

W = sympy.Matrix([
	[0,xy,-xz],
	[-xy,0,yz],
	[xz,-yz,0]])


W2 = sympy.Matrix([
	[0,xy,0],
	[-xy,0,0],
	[0,0,0]])

#sympy.pprint(sympy.simplify(R.inv()*W*R))



Q = sympy.Matrix([
	[R,r],
	[0,1]])

G = sympy.Matrix([
	[M, 0],
	[F, 0]])

sympy.pprint(Q*G)