#!/usr/bin/env python
"""mapper.py"""

import re
import sys

# Forzamos UTF-8 en la entrada y la salida estándar
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

# Cada mapper lee su split desde STDIN (entrada estándar)
for line in sys.stdin:
    # Minúsculas y solo letras (incluye acentos y la ñ)
    words = re.findall(r"[^\W\d_]+", line.lower())
    for word in words:
        # Se escribe <clave, valor> en STDOUT, delimitado por tabulaciones.
        # Lo que procese cada mapper será la entrada del reducer
        print(f"{word}\t1")
