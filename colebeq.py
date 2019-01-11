#!/usr/bin/env python3

import sympy

sympy.var("v v_z x x_z T_1 T_2 t g T ksi a b c d e p r s u uz pz rz sz")

#eq_x = sympy.Eq(v, (x-x_z)/t)
#eq_y = sympy.Eq(T_1*T_2*(v-v_z)/t+T_1*v+x, g)
#eq_v2 = sympy.Eq(T**2*(v-v_z)/t+2*T*ksi*v+x, g)

eq_p = sympy.Eq(a*(p-pz)/t+p, g)

sympy.pprint(eq_p)

ret = sympy.solve([eq_p], [p])
print("P:")
sympy.pprint(ret[p])

print("*******************")
print()

eq_p = sympy.Eq(r, (p-pz)/t)
eq_r = sympy.Eq(a*(r-rz)/t+b*r+p, g)

sympy.pprint(eq_p)
sympy.pprint(eq_r)

ret = sympy.solve([eq_p, eq_r], [p, r])
print("P:")
sympy.pprint(ret[p])
sympy.pprint(ret[p].subs({a:1, b:0, t:0.1}))
print("R:")
sympy.pprint(ret[r])
sympy.pprint(ret[r].subs({a:1, b:0, t:0.1}))

print("*******************")
print()

eq_p = sympy.Eq(r, (p-pz)/t)
eq_r = sympy.Eq(s, (r-rz)/t)
eq_s = sympy.Eq(a*(s-sz)/t+b*s+c*r+p, g)

sympy.pprint(eq_p)
sympy.pprint(eq_r)
sympy.pprint(eq_s)

ret = sympy.solve([eq_p, eq_r, eq_s], [p, r, s])
print("P:")
sympy.pprint(ret[p])
print("R:")
sympy.pprint(ret[r])
print("S:")
sympy.pprint(ret[s])


print("*******************")
print()

eq_p = sympy.Eq(r, (p-pz)/t)
eq_r = sympy.Eq(s, (r-rz)/t)
eq_s = sympy.Eq(u, (s-sz)/t)
eq_u = sympy.Eq(a*(u-uz)/t+b*u+c*s+d*r+p, g)

sympy.pprint(eq_p)
sympy.pprint(eq_r)
sympy.pprint(eq_s)
sympy.pprint(eq_u)

ret = sympy.solve([eq_p, eq_r, eq_s, eq_u], [p, r, s, u])
print("P:")
sympy.pprint(ret[p])
print("R:")
sympy.pprint(ret[r])
print("S:")
sympy.pprint(ret[s])
print("U:")
sympy.pprint(ret[u])