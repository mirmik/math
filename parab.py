from sympy import *
import math
import numpy as np
import matplotlib.pyplot as pplot 

pj1, psi, y0, gamma, gr= symbols("pj1 psi y0 gamma gr")

F = 2500
xright = 625
re = 625
y0 = 1650

gr = 2*math.pi / 360
#gamma = pi / 2

xj1q = xright + re * (1 - cos(psi))
yj1q = (xright + re) * tan(psi) - re * sin(psi)
pj1 =  sqrt(xj1q**2 + yj1q**2)

pj2 = pj1 + y0 * sin(psi)
zj2 = (pj2**2)/4/F

asqrt = sqrt(pj2**2 + 4*F**2)

xp2 = 2*F / asqrt
yp2 = pj2 / asqrt
xp3 = yp2
yp3 = -xp2

xmpsi = 1295
gmpsi = 106 * gr
aepsi = 600 
bepsi = 125

b = 0.5*(1-cos(pi * gamma / gmpsi))

#print("pj2")
#pprint(pj2)
#print("zj2")
#pprint(zj2)
#print("xp2")
#pprint(xp2)
#print("yp2")
#pprint(yp2)
#print("xp3")
#pprint(xp3)
#print("yp3")
#pprint(yp3)


p1 = (
	(gamma * xmpsi / gmpsi * xp2) * (1-b) 
	+ (aepsi * xp2 * sin(gamma) + bepsi * yp2 * (1-cos(gamma)))*b + pj1
)
p1 = simplify(p1)

ex1 = p1.subs(gamma, 0)
#ex2 = p1.subs(gamma, pi / 4)
ex3 = p1.subs(gamma, math.pi/2)
#ex4 = p1.subs(gamma, pi / 4 * 3)
ex5 = p1.subs(gamma, 106/360*2*math.pi)

N = 200
a = (np.arange(0,N) - 100) * 90/360*2*math.pi/N
b1 = [pj1.subs(psi, t).evalf() for t in a] 
#b2 = [ex2.subs(psi, t).evalf() for t in a] 
b3 = [ex3.subs(psi, t).evalf() for t in a] 
#b4 = [ex4.subs(psi, t).evalf() for t in a] 
b5 = [ex5.subs(psi, t).evalf() for t in a] 
#
pplot.polar(
	a, b1, 
	#a, b2,
	a, b3,
	#a, b4,
	a, b5
)
pplot.show()




