import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

try:
    background_image = pygame.image.load("7200 pygame/stad.jpg")
    background_image = pygame.transform.scale(background_image, (400, 600))
except pygame.error as e:
    print(f"Fel vid inläsning av bakgrundsbild: {e}")

try:
    tower_image = pygame.image.load("7200 pygame/tower.jpg")
    tower_width = 80  
except pygame.error as e:
    print(f"Fel vid inläsning av tornbild: {e}")

try:
    bird_image = pygame.image.load("7200 pygame/birdie.png")
    bird_image = pygame.transform.scale(bird_image, (45, 45))
except pygame.error as e:
    print(f"Fel vid inläsning av fågelbild: {e}")

width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")


clock = pygame.time.Clock()
bird_width, bird_height = 45, 45
pipe_width = tower_width
pipe_gap = 150
pipe_velocity = 4  
pipe_frequency = 1500

font = pygame.font.SysFont('Arial', 30)

def reset_game():
    global bird, bird_y, bird_velocity, poäng, pipes, pipe_timer, game_over
    bird_y = height // 2
    bird_velocity = 0
    poäng = 0
    pipes = []
    pipe_timer = 0
    bird = pygame.Rect(100, bird_y, bird_width, bird_height)
    game_over = False

reset_game()

def draw_bird():
    screen.blit(bird_image, (bird.x, bird.y))

def draw_pipes():
    for pipe in pipes:
        top_scaled = pygame.transform.scale(tower_image, (pipe_width, pipe['top'].height))
        bottom_scaled = pygame.transform.scale(tower_image, (pipe_width, pipe['bottom'].height))
        
        screen.blit(top_scaled, (pipe['top'].x, pipe['top'].y))
        screen.blit(pygame.transform.flip(bottom_scaled, False, True), (pipe['bottom'].x, pipe['bottom'].y))


def move_pipes():
    global poäng
    for pipe in pipes:
        pipe['top'].x -= pipe_velocity
        pipe['bottom'].x -= pipe_velocity
        if pipe['top'].right < 0:
            pipes.remove(pipe)
            poäng += 1


def generate_pipe():
    gap_height = 150  
    min_height = 50  
    max_height = height - 200  

    pipe_height = random.randint(min_height, max_height)
    bottom_height = height - pipe_height - gap_height  

    top_rect = pygame.Rect(width, 0, tower_width, pipe_height)
    bottom_rect = pygame.Rect(width, height - bottom_height, tower_width, bottom_height)

    pipes.append({'top': top_rect, 'bottom': bottom_rect})



def check_collision():
    global bird_y
    for pipe in pipes:
        if bird.colliderect(pipe['top']) or bird.colliderect(pipe['bottom']):
            return True
    if bird_y > height - bird_height or bird_y < 0:
        return True
    return False

def show_game_over():
    game_over_text = font.render(f"Spel över! poäng: {poäng}", True, WHITE)
    restart_text = font.render("Tryck SPACE för spela!", True, WHITE)
    screen.blit(game_over_text, (width // 4, height // 2 - 30))
    screen.blit(restart_text, (width // 4, height // 2 + 30))
    pygame.display.flip()

running = True
game_over = False
pipe_timer = 0

while running:
    screen.fill(WHITE)

    if 'background_image' in locals():
        screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                reset_game()
            else:
                bird_velocity = -8  

    if not game_over:
        bird_velocity += 0.5  
        bird_y += bird_velocity
        bird.y = bird_y

        pipe_timer += clock.get_time()
        if pipe_timer >= pipe_frequency:
            generate_pipe()
            pipe_timer = 0

        move_pipes()

        if check_collision():
            game_over = True

        draw_bird()
        draw_pipes() 

        poäng_text = font.render(f"poäng: {poäng}", True, GREEN)
        screen.blit(poäng_text, (10, 10))

    else:
        show_game_over()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()