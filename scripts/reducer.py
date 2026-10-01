#!/usr/bin/env python
"""reducer.py"""

import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

current_word = None
current_count = 0

# Leemos cada línea proveniente de los mappers (ya ordenada y mezclada)
for line in sys.stdin:
    # Eliminamos los espacios
    line = line.strip()
    if not line:
        continue

    # Parseamos la entrada del mapper.py
    word, count = line.split("\t", 1)

    # Convertimos el contador a un entero
    try:
        count = int(count)
    except ValueError:
        # En caso que el contador no sea un entero ignoramos la línea
        continue

    # Este IF funciona porque Hadoop ordena la salida del mapper por clave
    # (aquí la clave es word) antes de que se pase al reducer.py
    if current_word == word:
        current_count += count
    else:
        if current_word is not None:
            # Escribimos el resultado a la salida estándar (STDOUT)
            print(f"{current_word}\t{current_count}")
        current_count = count
        current_word = word

# Se envía la última palabra
if current_word is not None:
    print(f"{current_word}\t{current_count}")
