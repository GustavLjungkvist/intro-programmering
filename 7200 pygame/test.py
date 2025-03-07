import pygame
import random

pygame.init()

# Ladda bakgrundsbilder
try:
    background_image = pygame.image.load("7200 pygame/stad.jpg")
    background_image = pygame.transform.scale(background_image, (400, 600))
except pygame.error as e:
    print(f"Fel vid inläsning av bakgrundsbild: {e}")

# Ladda tornen
try:
    tower_image = pygame.image.load("7200 pygame/tower.jpg")
    tower_image = pygame.transform.scale(tower_image, (60, 150))
except pygame.error as e:
    print(f"Fel vid inläsning av tornbild: {e}")

# Ladda fågelbild
try:
    bird_image = pygame.image.load("7200 pygame/fågel.jpg")
    bird_image = pygame.transform.scale(bird_image, (45, 45))
except pygame.error as e:
    print(f"Fel vid inläsning av fågelbild: {e}")

# Spelinställningar
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
bird_width, bird_height = 45, 45
pipe_width = 60
pipe_gap = 150
pipe_velocity = 4  # Lägre hastighet för pipen
pipe_frequency = 1500

font = pygame.font.SysFont('Arial', 30)

def reset_game():
    global bird, bird_y, bird_velocity, score, pipes, pipe_timer, game_over
    bird_y = height // 2
    bird_velocity = 0
    score = 0
    pipes = []
    pipe_timer = 0
    bird = pygame.Rect(100, bird_y, bird_width, bird_height)
    game_over = False

reset_game()

def draw_bird():
    screen.blit(bird_image, (bird.x, bird.y))

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe['top'])
        pygame.draw.rect(screen, GREEN, pipe['bottom'])

def move_pipes():
    global score
    for pipe in pipes:
        pipe['top'].x -= pipe_velocity
        pipe['bottom'].x -= pipe_velocity
        if pipe['top'].right < 0:
            pipes.remove(pipe)
            score += 1

def generate_pipe():
    pipe_height = random.randint(100, height - 100)
    top = pygame.Rect(width, 0, pipe_width, pipe_height)
    bottom = pygame.Rect(width, pipe_height + pipe_gap, pipe_width, height - pipe_height - pipe_gap)
    pipes.append({'top': top, 'bottom': bottom})

def check_collision():
    global bird_y
    for pipe in pipes:
        if bird.colliderect(pipe['top']) or bird.colliderect(pipe['bottom']):
            return True
    if bird_y > height - bird_height:  # Fågeln dör om den rör vid marken
        return True
    if bird_y < 0:  # Fågeln dör om den går för högt
        return True
    return False

def show_game_over():
    game_over_text = font.render(f"Game Over! Score: {score}", True, BLACK)
    screen.blit(game_over_text, (width // 4, height // 2 - 30))
    restart_text = font.render("Press SPACE to Restart", True, BLACK)
    screen.blit(restart_text, (width // 4, height // 2 + 30))
    pygame.display.flip()

running = True
game_over = False
pipe_timer = 0

while running:
    screen.fill(WHITE)

    # Visa bakgrund
    if 'background_image' in locals():
        screen.blit(background_image, (0, 0))  # Lägg till bakgrunden
    else:
        print("Bakgrundsbilden kunde inte laddas.")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                reset_game()
            else:
                bird_velocity = -8  # Lägre hoppstyrka för mindre "hopp"

    if not game_over:
        bird_velocity += 0.5  # Lägg till gravitation
        bird_y = bird.y + bird_velocity
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

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    else:
        show_game_over()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
