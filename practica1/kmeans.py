import os.path
import sys
from math import *
from random import *


def calcularDistanciaEuclideana(puntoA: tuple, puntoB: tuple):
    return sqrt(
        sum(
            pow(puntoA[i] - puntoB[i], 2) for i in range(dimensiones)
        )
    )


def actualizarCentroide(indiceCentroide: int):
    for centroide in grupos:
        if centroide != indiceCentroide:
            continue
        vectoresPertenecientes = [
            datos[indiceVector] for indiceVector, iCentroide in grupos.items() if iCentroide == indiceCentroide
        ]
        if len(vectoresPertenecientes) > 0:
            centroides[indiceCentroide] = tuple(
                [
                    sum([
                        vector[dimension] for vector in vectoresPertenecientes
                    ]) / len(vectoresPertenecientes)
                    for dimension in range(dimensiones)
                ]
            )


# Vectores
datos = ((153, 51, 255), (121, 236, 221), (209, 236, 121), (240, 164, 76), (240, 98, 76), (76, 93, 240), (50, 239, 94))

# Centroides
centroides = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Pertenencia
grupos = {}  # indice = indice del Vector de referencia, valor = indice del Centroide de referencia

dimensiones = len(datos[0])

if len(sys.argv) > 1:
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print('[Error] El archivo \'' + filename + '\' no existe.')
        exit(1)
    d = []
    with open(filename) as file:
        for line in file:
            if len(line.split()) < 1:
                continue
            d.append(tuple([int(valor) for valor in line.split()]))
    datos = tuple(d)
    dimensiones = len(datos[0])

    centroides = []
    for n in range(randint(3, 5)):
        centroides.append(
            tuple([randint(0, 10000000) for d in range(dimensiones)])
        )

# (C) Bloque de codigo: Calculo de distancias y asignacion de grupos
for indiceVector, vector in enumerate(datos):
    nearest = (None, None)  # (distancia, indiceCentroide)
    for indiceCentroide, centroide in enumerate(centroides):
        distancia = calcularDistanciaEuclideana(vector, centroide)
        if nearest[0] is None or distancia < nearest[0]:
            nearest = (distancia, indiceCentroide)
    grupos[indiceVector] = nearest[1]

print('----- Grupos -----')
for indiceVector, indiceCentroide in grupos.items():
    print('\t' + str(indiceVector) + ' => ' + str(indiceCentroide))

# (D) Bloque de codigo: Actualizacion de centroides
for indiceCentroide, centroide in enumerate(centroides):
    actualizarCentroide(indiceCentroide)

print('\n----- Centroides Actualizados -----')
for centroide in centroides:
    print('\t' + str(centroide))
