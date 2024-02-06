import pygame
import sys
import random

# Inicializace Pygame
pygame.init()

# Nastavení fontu
font_size = 36
font = pygame.font.Font(None, font_size)

# Nastavení velikosti okna a dalších konstant
width, height = 640, 480

hlavni_okno = pygame.display.set_mode( (width, height) )

# Barvy
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

center = (100, 100)
radius = 50

FPS = 20
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    button1, button2, button3 = pygame.mouse.get_pressed()
    pozice = pygame.mouse.get_pos()

    hlavni_okno.fill(white)

    if radius**2 >= (pozice[0]-center[0])**2 + (pozice[1]-center[1])**2:
        barva = red
    else:
        barva = black
    pygame.draw.circle(hlavni_okno, barva, center, radius)

    text_surface = font.render(f"Pozice myši: {pozice}", True, black)
    hlavni_okno.blit(text_surface, (10, 10))


    # Aktualizace obrazovky
    pygame.display.update()

    # Rychlost hada
    pygame.time.Clock().tick(FPS)

pygame.quit()
sys.exit()

# Spuštění hry
game_loop()
