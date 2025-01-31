import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

x, y = 100, HEIGHT // 2
velocity = 0
gravity = 0.5
jump_strenght = -10
