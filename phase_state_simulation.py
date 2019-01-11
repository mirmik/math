#!/usr/bin/env python3
#coding: utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy import linalg

def check_dimmension(A,B,C,D) :
	g_dim = B.shape[-1]
	x_dim = B.shape[-2]
	y_dim = C.shape[-2]

	assert(A.shape[-1] == x_dim)
	assert(A.shape[-2] == x_dim)
	assert(B.shape[-1] == g_dim)
	assert(B.shape[-2] == x_dim)
	assert(C.shape[-1] == x_dim)
	assert(C.shape[-2] == y_dim)
	assert(D.shape[-1] == g_dim)
	assert(D.shape[-2] == y_dim)

	return (g_dim, x_dim, y_dim)

def matrix_discretization(A,B,C,D,Step):
	_A = linalg.expm(A * Step)
	_B = linalg.inv(A).dot((np.identity(A.shape[0]) - _A).dot(B))
	_C = C
	_D = D
	return (_A,_B,_C,_D)

#d2x/dt^2 = Ddx/dt + Kx

A = np.mat('''	0 1;
				-1 0''') # собственная матрица

B = np.mat('''	0;
				-1''') # входная матрица

C = np.mat('''  1 0''') # выходная матрица

D = np.mat('''0''') # проходная матрица


x0 = np.mat("0; 0") # начальное состояние

def g(time ):	#генератор входного сигнала
	return np.mat(10)

Time = 20			#симулируемый интервал времени
Points = 201		#Количество итераций
Range = np.r_[0 : Time : Points * 1j] # генерация объекта Range
Step = Range[1] - Range[0]

dim_g, dim_x, dim_y = check_dimmension(A,B,C,D)
discrete_A, discrete_B, discrete_C, discrete_D = matrix_discretization(A,B,C,D,Step)

print("Start ", Range[0])
print("Stop ", Range[-1])
print("Step ", Step)

print("A*:")
print(discrete_A)

print("B*:")
print(discrete_B)

#Решатель
results = []	# массив результатов
internals = []	# массив результатов
signals = []	# массив результатов
x = x0			# инициализация начального состояния

print("Results dimmension", dim_y)
print("Internals dimmension", dim_x)
print("Signals dimmension", dim_g)

for _ in range(dim_x):
	internals.append([]) 

for _ in range(dim_y):
	results.append([]) 

for _ in range(dim_g):
	signals.append([]) 

#Основной цикл
for t in Range:
	_g = g(t)
	x = discrete_A.dot(x) + discrete_B.dot(_g)
	y = discrete_C.dot(x) + discrete_D.dot(_g)
	
	for i in range(dim_x):
		internals[i].append(np.asscalar(x[i]))

	for i in range(dim_y):
		results[i].append(np.asscalar(y[i]))

	for i in range(dim_g):
		signals[i].append(np.asscalar(_g[i]))

print("Results:")

for i in range(dim_x) :
	plt.plot(Range, internals[i], label = "state[%d]" % i)

for i in range(dim_y) :
	plt.plot(Range, results[i], label = "output[%d]" % i)

for i in range(dim_g) :
	plt.plot(Range, signals[i], label = "input[%d]" % i)

plt.legend(loc='upper right')
plt.show()