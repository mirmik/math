#!/usr/bin/env python3

import math


acc = 0

for i in range(5):
    for j in range(5):
        acc += math.comb(10, i) * math.comb(12, j) * math.comb(9, 8-i-j)

print(acc)
