#!/usr/bin/env python3

import licant

licant.cxx_application("target",
	sources=["main.cpp"],
	libs=["nos", "igris"]
)

licant.ex("target")