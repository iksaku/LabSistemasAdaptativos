#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import random
import pygame
import sys


def explotar(posx=400, posy=400, radio=399, color_particulas=(0, 0, 0), color_pantalla=(255, 255, 255)):
    print("Coordenadas de Explosion -> x: %d, y: %d, radio: %d" % (posx, posy, radio))
    for i in range(radio):
        screen.fill(color_pantalla)
        for speed, angle in particles:
            distance = i * speed
            x = posx + distance * math.cos(angle)
            y = posy + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), color_particulas)
        pygame.display.flip()


def secuencia_explosiones():
    posx = 200
    for i in range(10):
        explotar(posx, 400, 100)
        posx += 40


n_explosiones = 5
n_predeterminado = True
try:
    n_explosiones = int(sys.argv[1])
    if n_explosiones < 0:
        raise ValueError
    n_predeterminado = False
    print("\n[Info] Cantidad de explosiones definidas por el usuario: %d" % n_explosiones)
except IndexError:
    print("\n[Info] No se ha recibido argumento con cantidad de explosiones. Utilizando valor predeterminado...")
except ValueError:
    print("\n[Error] El argumento recibido por el programa no es un número entero permitido. Utilizando valor "
          "predeterminado...")

pygame.init()

screen = pygame.display.set_mode((700, 700))
particles = [(random.gauss(0, 0.5), random.uniform(0, 6.28318)) for i in range(2000)]

input("\nPresione <Enter> para comenzar...")

print("\nGenerando explosiones con coordenadas y radio explicitos...")
explotar(300, 300, 100)
explotar(50, 50, 50)
explotar(600, 600, 300)

print("\nGenerando secuencia de Explosiones en línea...")
secuencia_explosiones()

if n_explosiones > 0:
    print("\nGenerando", n_explosiones, "explosiones",
          "(Argumento predeterminado)" if n_predeterminado else "(Argumento de Usuario)", "...")
    for i in range(n_explosiones):
        explotar(random.randint(100, 600), random.randint(100, 600), random.randint(0, 400))
else:
    print("Ha pedido que se generen 0 explosiones... Por lo cual no generaremos ninguna explosion... "
          "#WorldPeace #ImagineByJohnLennon")

colores = [
    (176, 23, 31),
    (128, 0, 128),
    (71, 60, 139),
    (0, 0, 255),
    (119, 136, 153),
    (30, 144, 255),
    (0, 229, 238),
    (69, 139, 116),
    (0, 255, 0),
    (255, 255, 0),
    (139, 105, 20),
    (255, 69, 0),
    (238, 0, 0),
    (0, 0, 0)
]

print("\nGenerando explosiones de distintos colores... #RainbowIsAPromise")
for color in colores:
    explotar(
        posx=random.randint(100, 600),
        posy=random.randint(100, 600),
        radio=random.randint(50, 300),
        color_particulas=color
    )

screen.fill((255, 255, 255))
pygame.display.flip()
input("\nPresione <Enter> para finalizar...")
