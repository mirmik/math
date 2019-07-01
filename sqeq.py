#!/usr/bin/env python3

import sympy

sympy.var("x t v0 x0 a")

res = sympy.solve(sympy.Eq(x, x0 + v0*t + a*t**2/2), (t))

sympy.pprint(res)