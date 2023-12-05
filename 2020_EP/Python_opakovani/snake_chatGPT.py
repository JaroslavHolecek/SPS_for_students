import pygame
import sys
import random

# Inicializace Pygame
pygame.init()

# Nastavení velikosti okna a dalších konstant
width, height = 640, 480
cell_size = 20
snake_size = 20
speed = 15

# Barvy
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Inicializace okna
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Funkce pro vykreslení hada
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, white, [segment[0], segment[1], snake_size, snake_size])

# Funkce pro generování jídla
def generate_food():
    food_x = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_size) / 20.0) * 20.0
    return food_x, food_y

# Hlavní smyčka hry
def game_loop():
    game_over = False
    game_close = False

    # Počáteční poloha hada
    snake = [[width / 2, height / 2]]

    # Počáteční směr hada
    direction = 'RIGHT'

    # Počáteční rychlost hada
    change_x = 20
    change_y = 0

    # Počáteční poloha jídla
    food_x, food_y = generate_food()

    while not game_over:

        while game_close:
            screen.fill(black)
            font = pygame.font.SysFont(None, 55)
            message = font.render("Prohrál jsi! Stiskni Q pro ukončení nebo C pro novou hru.", True, red)
            screen.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_x = -cell_size
                    change_y = 0
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_x = cell_size
                    change_y = 0
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    change_x = 0
                    change_y = -cell_size
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_x = 0
                    change_y = cell_size
                    direction = 'DOWN'

        # Aktualizace polohy hada
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = list(snake[i - 1])

        snake[0][0] += change_x
        snake[0][1] += change_y

        # Kontrola kolize s okrajem
        if snake[0][0] >= width or snake[0][0] < 0 or snake[0][1] >= height or snake[0][1] < 0:
            game_close = True

        # Kontrola kolize s tělem hada
        for segment in snake[1:]:
            if snake[0][0] == segment[0] and snake[0][1] == segment[1]:
                game_close = True

        # Kontrola kolize s jídlem
        if snake[0][0] == food_x and snake[0][1] == food_y:
            food_x, food_y = generate_food()
            snake.append([0, 0])

        # Vykreslení pozadí
        screen.fill(black)

        # Vykreslení hada
        draw_snake(snake)

        # Vykreslení jídla
        pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])

        # Aktualizace obrazovky
        pygame.display.update()

        # Rychlost hada
        pygame.time.Clock().tick(speed)

    pygame.quit()
    sys.exit()

# Spuštění hry
game_loop()
