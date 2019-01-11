#!/usr/bin/env python3
#coding: utf-8

from sympy import *

var("W a b c s kp Ti")

Wap = 1/(a*s**2 + b*s + c)
Wpid = (kp+1/Ti*s)

W = Wap * Wpid

pprint (W)