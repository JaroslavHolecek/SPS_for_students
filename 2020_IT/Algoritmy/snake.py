import pygame
import sys
import random

# Inicializace Pygame
pygame.init()

vstup = input("Chcete načíst hru ze souboru (S), nebo hrát novou (N)?")
if vstup == "S":
    new_game = False
elif vstup == "N":
    new_game = True
else:
    print("Neplátná volba, začínám novou hru")
    new_game = True

# Nastavení šířky a výšky okna
width, height = 840, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hra Had")

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Velikost hada a jeho rychlost
snake_size = 20
snake_speed = 15

# Nastavení fontu
font = pygame.font.SysFont(None, 55)



if new_game:
    # Skóre
    score = 0
    # Inicializace hada
    snake = [(width // 2, height // 2)]
    snake_direction = (1, 0)
else:
    # načíst hru ze souboru
    with open("ulozeno.had", "r") as soubor:
        score = int(soubor.readline())
        snake_direction = tuple(map(int, soubor.readline().split()))
        snake = []
        for radek in soubor:
            snake.append(tuple(map(int, radek.split())))

# Inicializace ovoce
fruit = (random.randrange(1, (width // snake_size)) * snake_size,
         random.randrange(1, (height // snake_size)) * snake_size)

HRAJU = 1
KONEC = 2
PAUZA = 3
stav_hry = HRAJU
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
            elif event.key == pygame.K_p and (stav_hry == HRAJU or stav_hry == PAUZA):
                if stav_hry == PAUZA:
                    stav_hry = HRAJU
                elif stav_hry == HRAJU:
                    stav_hry = PAUZA

            elif event.key == pygame.K_u:
                with open("ulozeno.had", "w") as soubor:
                    soubor.write(f"{score}\n{snake_direction[0]} {snake_direction[1]}\n")
                    for clanek in snake:
                        soubor.write(f"{clanek[0]} {clanek[1]}\n")

            if stav_hry == KONEC:
                stav_hry = HRAJU
                score = 0
                snake = [(width // 2, height // 2)]
                snake_direction = (1, 0)



    if stav_hry == HRAJU:
        # Pohyb hada
        new_head = (snake[0][0] + snake_direction[0] * snake_size,
                    snake[0][1] + snake_direction[1] * snake_size)

        # Konec hry, pokud had narazí do okraje
        if not (0 <= new_head[0] < width and 0 <= new_head[1] < height):
            stav_hry = KONEC

        # Konec hry, pokud had narazí do sebe
        if new_head in snake:
            stav_hry = KONEC

        snake.insert(0, new_head)

        # Když had sežere ovoce
        if new_head == fruit:
            fruit = (random.randrange(1, (width // snake_size)) * snake_size,
                     random.randrange(1, (height // snake_size)) * snake_size)
            score += 1
        else:
            snake.pop()
    elif stav_hry == PAUZA:
        pass

    # Vykreslení obrazovky
    screen.fill(black)
    pygame.draw.rect(screen, red, (fruit[0], fruit[1], snake_size, snake_size))
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))


    # Vykreslení skóre
    if stav_hry == HRAJU:
        score_text = font.render(f"Skóre: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
    elif stav_hry == KONEC:
        # Zobrazení výsledného skóre
        final_score_text = font.render(f"Konečné skóre: {score}", True, (255, 255, 255))
        screen.blit(final_score_text, (10, 300))
        new_game_text = font.render(f"Nová hra na stisk libovolné klávesy", True,
                                       (255, 255, 255))
        screen.blit(new_game_text, (10, 360))
    elif stav_hry == PAUZA:
        pauza_text = font.render(f"Pauza - stikni p pro pokračování", True,
                                    (255, 255, 255))
        screen.blit(pauza_text, (10, 360))


    pygame.display.flip()

    # Omezení rychlosti hry
    pygame.time.Clock().tick(snake_speed)

pygame.quit()
