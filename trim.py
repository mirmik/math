#!/usr/bin/env python3

import sys

Am = float(sys.argv[1]) / 1000 # сек
S = 4194304 / 1000
RATIO = 583

NOM = 3000 * S / 60 # имп в секунду
print("NOM:", 3000/60)
print("NOM:", NOM)


imppersec2 = NOM / Am


print("A:", imppersec2 / RATIO )

# NOM / Am / RATIO


print("B:", NOM/RATIO/float(sys.argv[1]) * 1000)