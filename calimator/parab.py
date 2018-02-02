from sympy import *
from sympy.plotting import plot3d, plot3d_parametric_surface 
from sympy.plotting import plot3d, plot_parametric 
import math
import numpy as np
import matplotlib.pyplot as pplot 

from sympy.utilities.lambdify import lambdify
from stl import mesh

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

p1 = (
	(gamma * xmpsi / gmpsi * xp2) * (1-b) 
	+ (aepsi * xp2 * sin(gamma) + bepsi * yp2 * (1-cos(gamma)))*b + pj1
)
p1 = simplify(p1)

Na = 200
angles = [t * 2 * math.pi / 360 / Na * 106 for t in range(0,Na+1)]
#angles = [0, pi/16]

N = int(200)
a = (np.arange(0,N+1) - N/2) * 90/360*2*math.pi/N

#arr = []
#for an in angles:
#	pplot.polar(a, [p1.subs(gamma, an).evalf(subs={psi: t}) for t in a], label='{}'.format(an))

#pplot.legend()
#pplot.show()


points = []
for i in range(0, len(angles)):
	ex = p1.subs(gamma, angles[i])
	func = lambdify(psi, ex, 'numpy') # returns a numpy-ready function
	rads = func(a)
	xs = rads*np.cos(a)
	ys = rads*np.sin(a)
	arr = np.column_stack((xs,ys,[i*2]*len(xs)))
	points.append(arr)


k = 0;
cube = mesh.Mesh(np.zeros((len(points)-1) * (len(a)-1) * 2, dtype=mesh.Mesh.dtype))
for i in range(0,len(points) - 1):
	for j in range(N-1):
#for i in range(1):
#	for j in range(2):
		cube.vectors[k][0] = points[i][j]
		cube.vectors[k][1] = points[i][j + 1]
		cube.vectors[k][2] = points[i+1][j]
		k+=1
		cube.vectors[k][2] = points[i][j+1]
		cube.vectors[k][1] = points[i+1][j]
		cube.vectors[k][0] = points[i+1][j + 1]
		k+=1
		pass

cube.save("mesh.stl")