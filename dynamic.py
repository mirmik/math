#!/usr/bin/env python3

import sympy

sympy.var("m mx my mz fx fy fz j11 j12 j13 j21 j22 j23 j31 j32 j33")

J = sympy.Matrix([
	[j11,j12,j13],
	[j21,j22,j23],
	[j31,j32,j33]
])

M = sympy.Matrix([
	[   mx],
	[   my],
	[   mz],
])

dwdt = J*M

dSdt = sympy.Matrix([
	[0, -dwdt[2], dwdt[1]],
	[dwdt[2], 0, -dwdt[0]],
	[-dwdt[1], dwdt[0], 0]
])

sympy.pprint(dSdt)