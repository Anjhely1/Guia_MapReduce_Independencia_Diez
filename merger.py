#!/usr/bin/env python
"""merger.py"""

import heapq
import sys

sys.stdout.reconfigure(encoding="utf-8")

# Una de las operaciones que provee automáticamente Hadoop es el merge de las
# salidas de los diferentes mappers (ya ordenadas por clave).
# Aquí lo hacemos porque estamos emulando el funcionamiento.
# Uso: python merger.py part1.txt part2.txt part3.txt
archivos = [open(path, encoding="utf-8") for path in sys.argv[1:]]

for line in heapq.merge(*archivos, key=lambda l: l.split("\t", 1)[0]):
    sys.stdout.write(line)

for f in archivos:
    f.close()
