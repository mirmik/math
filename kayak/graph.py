#!/usr/bin/env python3

import pandas 
import matplotlib.pyplot as plt

import numpy
import math

table = pandas.read_excel("20150216_062648_Павлов Михаил.xlsx")
#table = pandas.read_excel("20150220_062403_Павлов Михаил.xlsx")
table = pandas.read_excel("20180527_065456_Анюшина Е.xlsx")

acc_z = table["Accel, UpDown (g)"]
acc_y = table["Accel, LeftRight (g)"]
acc_x = table["Accel, ForwardBackward (g)"]

time = table["Time (sec)"]
stime = time[0]
for i in range(len(time)):
	time[i] = time[i] - stime


for i in range(len(acc_x)):
	if isinstance(acc_x[i], str) and "," in acc_x[i]:
		acc_x[i] = acc_x[i-1]

fft = numpy.fft.rfft(acc_x)
freqs = numpy.fft.rfftfreq(len(acc_x), d=(time[len(acc_x)-1]-time[0])/len(acc_x))

#amp = numpy.ndarray((len(acc_x),))
#for i in range(len(acc_x)):
#	amp[i] = math.sqrt(acc_x[i]**2 + acc_y[i]**2 + acc_z[i]**2)

FLTFREQ = 3

sig = acc_x[0]
flt = numpy.ndarray((len(acc_x),))
for i in range(1, len(acc_x)):
	delta = time[i] - time[i-1]
	sig = sig + (acc_x[i] - sig) * delta * FLTFREQ
	flt[i] = sig 

FLTFREQ = 0.0125
sig = acc_y[0]
flt_y = numpy.ndarray((len(acc_y),))
for i in range(1, len(acc_y)):
	delta = time[i] - time[i-1]
	sig = sig + (acc_y[i] - sig) * delta * FLTFREQ
	flt_y[i] = sig 


FLTFREQ = 0.25
sig = acc_y[0]
flt2_y = numpy.ndarray((len(acc_y),))
for i in range(1, len(acc_y)):
	delta = time[i] - time[i-1]
	sig = sig + (acc_y[i] - sig) * delta * FLTFREQ
	flt2_y[i] = sig 




count = 0
cindexes = []

last = 0
phase = False
status = False
power = 0
sacc = flt[i]
for i in range(1,len(acc_x)):
	delta = time[i] - time[i-1]

	if phase == True:
		if flt[i] < last:
			phase = False

		else:
			if status is False:
				power += (flt[i] - sacc) * delta

				#if power >= 0.01: #kanoe
				if flt[i] - sacc > 0.02: #power >= 0.001: 
					status = True
					cindexes.append(i)


	else:
		if flt[i] > last:
			count += 1
			phase = True
			status = False
			power = 0
			sacc = flt[i]
			#cindexes.append(i)

	last = flt[i]

print(count)

points = [ flt[i] for i in cindexes ]
times = [ time[i] for i in cindexes ]






fig, axs = plt.subplots(5)

axs[0].plot(time, acc_z)
axs[1].plot(time, acc_y)
axs[2].plot(time, acc_x)
axs[3].plot(time, flt_y - flt2_y)
axs[4].plot(time, flt)
axs[4].plot(times, points, ".")
plt.show()