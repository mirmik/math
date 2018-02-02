from sympy import *
from sympy.plotting import plot3d, plot3d_parametric_surface 
from sympy.plotting import plot3d, plot_parametric 
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
yj1q = (xright + re) * tan(psi) - re * sin(psi) #+ y0
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

#exs = [
#	p1.subs(gamma, 0),
#	p1.subs(gamma, pi / 16),
#	p1.subs(gamma, pi / 8),
#	p1.subs(gamma, pi / 4),
#	p1.subs(gamma, math.pi/2),
#	p1.subs(gamma, pi / 4 * 3),
#	p1.subs(gamma, 106/360*2*math.pi)
#]

angles = [0, pi/16, pi/8, pi/4, pi/2, 106*gr]

#plot_parametric(p1*cos(psi), p1*sin(psi), (gamma, 0, 106*gr), (psi, -45*gr, 45*gr))
#plot_parametric(exs[0]*cos(psi), exs[0]*sin(psi), (psi, -math.pi/4, math.pi/4))

N = 20
a = (np.arange(0,N+1) - N/2) * 90/360*2*math.pi/N
#b = [[exs[i].evalf(subs={psi: t}) for t in a] for i in range(0, len(exs))]

#ax = pplot.subplot(111, polar=True)

arr = []
for an in angles:
	pplot.polar(a, [p1.subs(gamma, an).evalf(subs={psi: t}) for t in a], label='{}'.format(an))
	#arr.append(a)
	#arr.append([p1.subs(gamma, an).evalf(subs={psi: t}) for t in a])
	#arr.append
#
#pplot.polar(
#	*arr
#)
pplot.legend()
pplot.show()




