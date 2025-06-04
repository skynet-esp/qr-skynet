#!/usr/bin/env python3

"""Buscar secuencias dentro de un archivo FASTA.

Uso:
    python buscar_secuencia_fasta.py archivo.fasta SECUENCIA_A_BUSCAR

El programa lee el archivo FASTA, busca la secuencia indicada en cada una de
las entradas y muestra los encabezados de aquellas que contengan dicha
secuencia.
"""

import sys


def leer_fasta(path):
    """Genera tuplas (encabezado, secuencia) para cada entrada del FASTA."""
    encabezado = None
    secuencia = []
    with open(path) as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            if linea.startswith('>'):
                if encabezado:
                    yield encabezado, ''.join(secuencia)
                encabezado = linea[1:]
                secuencia = []
            else:
                secuencia.append(linea)
        if encabezado:
            yield encabezado, ''.join(secuencia)


def buscar_secuencia(fasta, query):
    """Imprime los encabezados de las secuencias que contengan la consulta."""
    query = query.upper()
    for encabezado, sec in leer_fasta(fasta):
        if query in sec.upper():
            print(encabezado)


def main(argv):
    if len(argv) != 3:
        print('Uso: python buscar_secuencia_fasta.py archivo.fasta SECUENCIA')
        return 1
    fasta = argv[1]
    query = argv[2]
    buscar_secuencia(fasta, query)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
