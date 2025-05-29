import pygame
import random

# this make by chatgpt

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 500
BLOCK_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
SPEED = 10

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and Food Initialization
snake = [(100, 100), (90, 100), (80, 100)]
direction = (BLOCK_SIZE, 0)
food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE, 
        random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(SPEED)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, BLOCK_SIZE):
        direction = (0, -BLOCK_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -BLOCK_SIZE):
        direction = (0, BLOCK_SIZE)
    if keys[pygame.K_LEFT] and direction != (BLOCK_SIZE, 0):
        direction = (-BLOCK_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-BLOCK_SIZE, 0):
        direction = (BLOCK_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Check for collisions
    if new_head == food:
        food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE, 
                random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
    else:
        snake.pop()  # Remove last segment if no food eaten

    # Check if snake hits the wall or itself
    if (new_head[0] < 0 or new_head[0] >= WIDTH or 
        new_head[1] < 0 or new_head[1] >= HEIGHT or 
        new_head in snake[1:]):
        running = False  # Game over

    # Draw everything
    screen.fill(BG_COLOR)
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    pygame.display.flip()

pygame.quit()
