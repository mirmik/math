#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as plt

L = 10
Y = 1
M = 1
delta = 0.001
T = 800

time = numpy.linspace(0, T, T/delta)

class Ball:
    def __init__(self, x, v, m=M):
        self.x = x
        self.v = v
        self.m = m
        self.position_history = []

    def force_from_other(self, other):
        diff = self.x - other.x
        return Y * diff / (abs(diff)**3)

    def demp(self, koeff):
        return -koeff * self.v

    def update(self, force, delta):
        self.v += force / self.m * delta
        self.x += self.v * delta
        self.position_history.append(self.x)
        
balls = [Ball(-5, 0), Ball(5, 0), Ball(0, 0.3)]

left_bound = Ball(-L, 0, 50)
right_bound = Ball(L, 0, 50)

for t in time:
    for i in range(len(balls)):
        ball = balls[i]
        force = 0
        for j in range(len(balls)):
            other = balls[j]
            if ball is not other:
                force += ball.force_from_other(other)
        force += ball.force_from_other(left_bound)
        force += ball.force_from_other(right_bound)
        force += ball.demp(0)
        ball.update(force, delta)

# Plot the results. x is time, y is position.
for ball in balls:
    plt.plot(time, ball.position_history)
plt.show()    