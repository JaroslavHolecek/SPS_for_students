import pygame
from pygame.locals import *
from math import sin, cos, pi
pygame.init()
comic_sans_font = pygame.font.SysFont('Comic Sans MS', 25)
default_font = pygame.font.Font(pygame.font.get_default_font(), 25)

hodiny = pygame.time.Clock()
fps = 40
display_width = 800
display_height = 600

velikost_predmetu = 20

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Odrazeni')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pocatecni_misto_x = 50
pocatecni_misto_y = 100
aktualni_x = pocatecni_misto_x
aktualni_y = pocatecni_misto_y

running = True
while running:
    # Zpracování vstupu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Výpočty
    aktualni_x += 1
    aktualni_y += 1
    # Zobrazení
    screen.fill(white)  # smazat předchozí frame
    pygame.draw.circle(screen, red, [aktualni_x,aktualni_y], velikost_predmetu)

    #Text zobrazení

    textsurface = comic_sans_font.render(
        f"Pozice kuličky {aktualni_x} {aktualni_y}", False, black)
    screen.blit(textsurface, dest=(60, 300))



    pygame.display.flip()
    hodiny.tick(fps)

pygame.quit()