import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5

pipe_x = WIDTH
pipe_height = random.randint(100, 400)
pipe_gap = 150

running = True
while running:
    screen.fill((135, 206, 250))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = -8
    
    bird_velocity += gravity
    bird_y += bird_velocity
    
    pipe_x -= 5
    if pipe_x < -60:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
    
    pygame.draw.rect(screen, (255, 255, 255), (50, bird_y, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, 60, pipe_height))
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, pipe_height + pipe_gap, 60, HEIGHT))
    
    if bird_y < 0 or bird_y + 30 > HEIGHT:
        running = False
    if (50 < pipe_x + 60 and 50 + 30 > pipe_x and
        (bird_y < pipe_height or bird_y + 30 > pipe_height + pipe_gap)):
        running = False
    
    pygame.display.update()
    clock.tick(30)

pygame.quit() 