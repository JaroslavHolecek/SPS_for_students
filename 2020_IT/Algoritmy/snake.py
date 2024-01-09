import pygame
import sys
import random

# Inicializace Pygame
pygame.init()

# Nastavení šířky a výšky okna
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hra Had")

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Velikost hada a jeho rychlost
snake_size = 20
snake_speed = 15

# Inicializace hada
snake = [(width // 2, height // 2)]
snake_direction = (1, 0)

# Inicializace ovoce
fruit = (random.randrange(1, (width // snake_size)) * snake_size,
         random.randrange(1, (height // snake_size)) * snake_size)

# Hlavní smyčka hry
while True:
    # Zpracování vstupu od uživatele
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Pohyb hada
    new_head = (snake[0][0] + snake_direction[0] * snake_size,
                snake[0][1] + snake_direction[1] * snake_size)

    # Konec hry, pokud had narazí do okraje
    if not (0 <= new_head[0] < width and 0 <= new_head[1] < height):
        pygame.quit()
        sys.exit()

    # Konec hry, pokud had narazí do sebe
    if new_head in snake:
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Když had sežere ovoce
    if new_head == fruit:
        fruit = (random.randrange(1, (width // snake_size)) * snake_size,
                 random.randrange(1, (height // snake_size)) * snake_size)
    else:
        snake.pop()

    # Vykreslení obrazovky
    screen.fill(black)
    pygame.draw.rect(screen, red, (fruit[0], fruit[1], snake_size, snake_size))

    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

    pygame.display.flip()

    # Omezení rychlosti hry
    pygame.time.Clock().tick(snake_speed)
