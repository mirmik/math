#!/usr/bin/env python3

import numpy
import torch

#import numpy pprint
from pprint import pprint
   
#numpy.random.seed(1)

def y(x):
    return x[0]*2 + x[1]*-1+ x[2]*0 + x[3]*1 + x[4]*0

A = numpy.array([
    [1,1,0,10,0],
    [2,33,1,0,0],
    [3,0,32,12,0],
    [4,44,0,42,1],
    [5,0,1,33,0],
    [6,1,15,0,0],
    [7,1,0,1,0],
    [8,1,34,0,1],
    [9,0,1,0,1],
    [10,0,0,1,1],
    [11,33,12,1,0],
    [12,0,1,0,0],
    [13,2,33,32,0],
])

B = numpy.array([y(x) for x in A])

# easy neuronetwork with 1 hidden layer
# 5 inputs, 1 output, 1 hidden layer with 4 neurons
I = 5
H = 1
O = 1

# weights
W1 = numpy.random.rand(H, I) * 2 - 1
W2 = numpy.random.rand(O, H) * 2 - 1

# learning rate
lr = 0.0001

# activation function
def tangent(x):
    return numpy.tanh(x)

def tangent_derivative(x):
    t = tangent(x)
    return 1 - t**2

def linear(x):
    return x

def linear_derivative(x):
    return 1

def relu(x):
    return numpy.where(x < 0, 0.5*x, x)

def relu_derivative(x):
    return numpy.where(x < 0, 0.5, 1)
    
activation_function = linear
activation_function_derivative = linear_derivative
activation_function_2 = linear
activation_function_2_derivative = linear_derivative

def forward_pass(signal_in):
    signal_hidden = activation_function(numpy.dot(W1, signal_in))
    signal_out = activation_function_2(numpy.dot(W2, signal_hidden))
    return signal_hidden, signal_out

# training
for i in range(10000):
    for j in range(len(A)):
        # forward pass
        signal_in = A[j].reshape(I, 1)
        signal_hidden, signal_out = forward_pass(signal_in)
        
#        W2_T = numpy.linalg.pinv(W2)
        W2_T = W2.transpose()

        # backpropagation
        error = B[j] - signal_out
        d_signal_out = error * activation_function_2_derivative(signal_out)
        error_hidden = numpy.dot(W2_T, d_signal_out)
        d_signal_hidden = error_hidden * activation_function_derivative(signal_hidden)
        
        # update weights
        W2 += lr * numpy.dot(d_signal_out, signal_hidden.transpose())
        W1 += lr * numpy.dot(d_signal_hidden, signal_in.transpose())

        W2 -= W2 * 0.01 * lr
        W1 -= W1 * 0.01 * lr

        #pprint(W1)
        #pprint(W2)

# testing
for i in range(len(A)):
    signal_hidden, signal_out = forward_pass(A[i])
    
sh, so = forward_pass([20,5,2,5,7])
print(sh)
print(so)