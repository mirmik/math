#!/usr/bin/env python3
#coding: utf-8

import sys

rev = 4194304.0
ratio = float(sys.argv[1])
rev_to_gr = 1.0/360.0

res = rev * rev_to_gr * ratio

print(res)