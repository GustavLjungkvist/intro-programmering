import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

bird_image = pygame.image.load("img/fågel.jpg")
bird_x = 50
bird_y = 50

size = (600, 800)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Gustavs spel")

done = False

keys = pygame.key.get_pressed()

if keys[pygame.K_SPACE]:
    bird_y -= 5


