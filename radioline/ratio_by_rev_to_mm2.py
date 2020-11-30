#!/usr/bin/env python3
#coding: utf-8

import sys
import math

angle = 19.5283 / 180 * math.pi

MODULE = 3
NZUBOV = 22

mm_per_sm = 10.0
imp_per_rev = 4194304.0

mm_per_rev = MODULE * NZUBOV / math.cos(angle) * math.pi
rev_per_mm = 1.0 / mm_per_rev


imp_per_sm = imp_per_rev * rev_per_mm * mm_per_sm
print(imp_per_sm)