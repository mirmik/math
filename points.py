#!/usr/bin/env python3

import numpy as np



G = np.array([
    [1,3,1,5],
    [0,0,1,1],
    [1,1,1,1],
])


x = np.array(
    [6,2,1]
)


A = G.T @ G
x = G.T @ x.reshape((len(x),1))

print(x)

print(np.linalg.pinv(A) @ x)
