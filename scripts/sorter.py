#!/usr/bin/env python
"""sorter.py"""

import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

# Una de las operaciones que provee automáticamente Hadoop es el sort por claves
# Aquí lo hacemos porque estamos emulando el funcionamiento
for line in sorted(sys.stdin, key=lambda l: l.split("\t", 1)[0]):
    sys.stdout.write(line)
