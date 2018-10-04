#!/usr/bin/env python3
#coding: utf-8

import sys

rev = 4194304.0
rev_to_mm = float(sys.argv[1])
mm_to_sm = 10.0

res = rev * rev_to_mm * mm_to_sm
print(res)