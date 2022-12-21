#!/usr/bin/env python3
import licant

licant.include("rabbit")

licant.cxx_application("target",
                       sources=["src/main.cpp"],
                       libs=["GLEW", "glfw", "GL", "X11", "GLU", "pthread", "Xrandr", "Xi", "SOIL", "nos", "igris"],
                       mdepends=["rabbit", "rabbit.opengl"]
                       )

licant.ex("target")
