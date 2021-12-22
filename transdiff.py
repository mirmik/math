#!/usr/bin/env python3

import sympy

sympy.var("Rq Rb Rh rq rb rh SRh SLb drh drb")

Q = sympy.Matrix([[Rq, rq], [0, 1]])
B = sympy.Matrix([[Rb, rb], [0, 1]])
H = sympy.Matrix([[Rh, rh], [0, 1]])

dBdt = sympy.Matrix([[SLb*Rb, drb], [0,0]])
dHdt = sympy.Matrix([[Rh*SRh, drh], [0,0]])

dQdt = B*dHdt + dBdt*H

sympy.pprint(Q.transpose() * dQdt)