#!/usr/bin/env python3
#coding: utf-8

import sys
import math

REDUKTOR = 220
SHESTERNA = 20
KOLCO = 93

ELGEAR = 100

imp_per_rev = 4194304.0

imp_per_lrev = imp_per_rev * REDUKTOR * KOLCO / SHESTERNA / ELGEAR
imp_per_lgrad = imp_per_lrev / 360
print(imp_per_lgrad)