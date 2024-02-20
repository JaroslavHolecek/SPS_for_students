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
rychlost_x = 1
rychlost_y = 1
zrychleni = 5

def uprav_rychlost(rychlost, zrychleni):
    uprav_limit = 10
    if rychlost < 0:
        return rychlost-zrychleni
    else:
        if rychlost > uprav_limit:
            return rychlost-zrychleni
        else:
            return rychlost+zrychleni

running = True
while running:
    # Zpracování vstupu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Výpočty
    aktualni_x += rychlost_x
    aktualni_y += rychlost_y
    if aktualni_x < 0+velikost_predmetu or aktualni_x > display_width-velikost_predmetu:
        rychlost_x = -zvetsit_rychlost(rychlost_x, zrychleni)
        rychlost_y = zvetsit_rychlost(rychlost_y, zrychleni)

    if aktualni_y < 0+velikost_predmetu or aktualni_y > display_height-velikost_predmetu:
        rychlost_y = -zvetsit_rychlost(rychlost_y, zrychleni)
        rychlost_x = zvetsit_rychlost(rychlost_x, zrychleni)


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