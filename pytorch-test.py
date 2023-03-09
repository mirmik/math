#!/usr/bin/env python3

import numpy
import torch

#import numpy pprint
from pprint import pprint
   

A = numpy.array([
    [1,1,0,0,0],
    [2,0,1,0,0],
    [3,0,0,1,0],
    [4,0,0,0,1],
    [5,0,1,0,0],
    [6,1,0,0,0],
    [7,1,0,1,0],
])

B = numpy.array([1,4,7,8,10,11,14])

# easy neuronetwork with 1 hidden layer
# 5 inputs, 1 output, 1 hidden layer with 4 neurons
I = 5
H = 4
O = 1

# weights
W1 = numpy.random.rand(H, I)
W2 = numpy.random.rand(O, H)

# learning rate
lr = 0.01

# activation function
def tangent(x):
    return numpy.tanh(x) 

def tangent_derivative(x):
    return 1 - numpy.tanh(x)**2 

def linear(x):
    return x

def linear_derivative(x):
    return 1

activation_function = tangent
activation_function_derivative = tangent_derivative
activation_function_2 = linear
activation_function_2_derivative = linear_derivative

def forward_pass(signal_in):
    signal_in = signal_in.reshape(I, 1)
    signal_hidden = activation_function(numpy.dot(W1, signal_in))
    signal_out = activation_function_2(numpy.dot(W2, signal_hidden))
    return signal_hidden, signal_out

# training
for i in range(1000):
    for j in range(len(A)):
        # forward pass
        signal_in = A[j].reshape(I, 1)
        signal_hidden, signal_out = forward_pass(signal_in)
        
        # backpropagation
        error = B[j] - signal_out
        d_signal_out = error * activation_function_2_derivative(signal_out)
        error_hidden = numpy.dot(W2.transpose(), d_signal_out)
        d_signal_hidden = error_hidden * activation_function_derivative(signal_hidden)
        
        # update weights
        W2 += lr * numpy.dot(d_signal_out, signal_hidden.transpose())
        W1 += lr * numpy.dot(d_signal_hidden, signal_in.transpose())

print("W1:")
pprint (W1)

print("W2:")
pprint (W2)

# testing
for i in range(len(A)):
    signal_hidden, signal_out = forward_pass(A[i])
    print(B[i], signal_out)

sh, so = forward_pass([20,5,2,5,7])
print(so)