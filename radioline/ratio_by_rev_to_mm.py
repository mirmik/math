#!/usr/bin/env python3
#coding: utf-8

import sys

mm_per_sm = 10.0
imp_per_rev = 4194304.0

mm_per_rev = float(sys.argv[1])
rev_per_mm = 1.0 / mm_per_rev


imp_per_sm = imp_per_rev * rev_per_mm * mm_per_sm
print(imp_per_sm)