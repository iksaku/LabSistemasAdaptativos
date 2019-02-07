import math
import random
import pygame
import sys


def explode(posx, posy, radio, particle_color=(0, 0, 0), screen_color=(255, 255, 255)):
    for i in range(radio):
        screen.fill(screen_color)
        for speed, angle in particles:
            distance = i * speed
            x = posx + distance * math.cos(angle)
            y = posy + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), particle_color)
        pygame.display.flip()


def explode_sequence():
    posx = 200
    for i in range(10):
        explode(posx, 400, 100)
        posx += 40


pygame.init()

screen = pygame.display.set_mode((800, 800))
particles = [(random.gauss(0, 0.5), random.uniform(0, 6.28318)) for i in range(2000)]

# explode(300, 300, 100)
# explode(50, 50, 50)
# explode(600, 600, 300)

# explode_sequence()

# explosion_n = 5
# if 1 in sys.argv:
#     explosion_n = int(sys.argv[1])
#
# for i in range(explosion_n):
#     explode(random.randint(0, 300), random.randint(0, 300), random.randint(0, 400))

for i in range(5):
    explode(
        posx=random.randint(100, 700),
        posy=random.randint(100, 700),
        radio=100,
        particle_color=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )

# TODO: .gitignore
