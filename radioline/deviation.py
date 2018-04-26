#!/usr/bin/env python3.6
#coding: utf-8

#deviation = 0x9CC 
deviation = - 0xFF_FF_FF_FF + 0xFF_FF_E2DD
#dist = 9000000
dist = -6000000

#deviation = 100_000

cdiv = 1749
ndiv = cdiv * (dist/(dist + deviation))

print("error: {}".format(deviation))
print("distance: {}".format(dist))
print("curdiv: {}".format(cdiv))
print("newdiv: {}".format(ndiv))