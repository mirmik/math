#!/usr/bin/python3

import ralgo
import sympy
import matplotlib.pyplot as plt 

sympy.var("s T ksi Ki Kp")

W = (Ki*1/s + Kp) * 1/s
W = W/(1+W) #* 1/s
W = W.factor()
W = W.subs([(Ki, 1/(T**2)), (Kp, 2*ksi/T)])
print(W)

#W = (2*ksi*T*s+1)/(T**2*s**2+2*ksi*T*s+1)

W = W.subs([(T,1), (ksi,2)])

W = (4*s + 1)/(s**2 + 4*s + 1)
#W = (1)/(s**2 + 4*s + 1)

#W = (1+2*s)/(s**2 + 2*s + 1)
print(W)



#ralgo.plot_step_responce_tf(W, 30, 1000)
ralgo.plot_step_responce_il(W, 30, 1000)
plt.show()
