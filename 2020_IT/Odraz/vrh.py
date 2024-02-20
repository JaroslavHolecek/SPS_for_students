import pygame
from pygame.locals import *
from math import sin, cos, pi

pygame.init()
comic_sans_font = pygame.font.SysFont('Comic Sans MS', 25)
default_font = pygame.font.Font(pygame.font.get_default_font(), 25)


def do_grafiky(pozice, zem):
    return [int(pozice[0]), int(-pozice[1] + zem)]  # y osa je smerem dolu a posunuta oproti nasi ZEMI ve hre


hodiny = pygame.time.Clock()
fps = 40
display_width = 800
display_height = 600

G = -10  # zrychleni [ms-2]
TSTEP = 0.1
ZEM = (50, 500, display_width - 50, 500)
velikost_predmetu = 20

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Sikmy vrh')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# zadani úvodních hodnot
pocatecni_misto_x = 50
pocatecni_misto_y = 100
mys_pres_kolecko = False

alpha = 30  # uhel [stupne]
alpharad = alpha * pi / 180  # uhel [radiany]

v = 40  # pocatecni rychlost
vx = v * sin(alpharad)
vy = v * cos(alpharad)

maxx = 0
maxy = 0
t = 0
posy = pocatecni_misto_y
posx = pocatecni_misto_x
prubezne_pozice = []

NEODSTARTOVANA = 1
POZASTAVENA = 2
BEZI = 3
NA_ZEMI = 4
TAHAM_ZA_KOLECKO = 5
NASTAVUJI_SMER = 6
stav_hry = NEODSTARTOVANA
running = True
while running:
    # Zpracování vstupu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_s:
                if stav_hry == NEODSTARTOVANA:
                    stav_hry = BEZI
                elif stav_hry == BEZI:
                    stav_hry = POZASTAVENA
                elif stav_hry == POZASTAVENA:
                    stav_hry = BEZI
            if event.key == K_r:
                prubezne_pozice = []
                stav_hry = NEODSTARTOVANA

    if stav_hry == NEODSTARTOVANA:
        pozice_mysi = do_grafiky(pygame.mouse.get_pos(), ZEM[1])
        if (posx - pozice_mysi[0]) ** 2 + (posy - pozice_mysi[1]) ** 2 <= velikost_predmetu ** 2:  # myš uvnitř kolečka
            mys_pres_kolecko = True
            if pygame.mouse.get_pressed()[0]:
                stav_hry = TAHAM_ZA_KOLECKO
            elif pygame.mouse.get_pressed()[2]:
                stav_hry = NASTAVUJI_SMER
        else:
            mys_pres_kolecko = False

    elif stav_hry == TAHAM_ZA_KOLECKO:
        if not pygame.mouse.get_pressed()[0]:
            stav_hry = NEODSTARTOVANA
    elif stav_hry == NASTAVUJI_SMER:
        if not pygame.mouse.get_pressed()[2]:
            stav_hry = NEODSTARTOVANA

    # Logika hry -> výpočty
    if stav_hry == NEODSTARTOVANA:
        t = 0
        posy = pocatecni_misto_y
        posx = pocatecni_misto_x

    elif stav_hry == TAHAM_ZA_KOLECKO:
        pozice_mysi = do_grafiky(pygame.mouse.get_pos(), ZEM[1])
        pocatecni_misto_x, pocatecni_misto_y = pozice_mysi
        posx, posy = pozice_mysi

    elif stav_hry == NASTAVUJI_SMER:
        pozice_mysi = pygame.mouse.get_pos()
        kolecko = do_grafiky((pocatecni_misto_x, pocatecni_misto_y), ZEM[1])
        vx = kolecko[0] - pozice_mysi[0]
        vy = pozice_mysi[1] - kolecko[1]

    elif stav_hry == BEZI:
        posx = vx * t + pocatecni_misto_x
        posy = vy * t + G * t * t / 2 + pocatecni_misto_y
        prubezne_pozice.append((posx, posy))

        maxx = max(maxx, abs(posx - pocatecni_misto_x))
        maxy = max(maxy, posy)
        print("Cas {:.1f} Objekt na souřadnicích {:.2f} : {:.2f}".format(t, posx, posy))

        if posy - velikost_predmetu <= 0:
            stav_hry = NA_ZEMI

        t += TSTEP

    # Zobrazení
    screen.fill(white)  # smazat předchozí frame

    pygame.draw.line(screen, black, ZEM[0:2], ZEM[2:4])
    barva_kolecka = red if mys_pres_kolecko else black  # toto je stejné jako if níže
    # if mys_pres_kolecko:
    #     barva_kolecka = black
    # else:
    #     barva_kolecka = red
    pygame.draw.circle(screen, barva_kolecka, do_grafiky([posx, posy], ZEM[1]), velikost_predmetu, 5)

    for pozice in prubezne_pozice:
        pygame.draw.circle(screen, red, do_grafiky(pozice, ZEM[1]), 2, 0)

    if stav_hry in (NEODSTARTOVANA, TAHAM_ZA_KOLECKO, NASTAVUJI_SMER):
        barva_cary = red if stav_hry == NASTAVUJI_SMER else black
        pygame.draw.line(screen, barva_cary, do_grafiky((pocatecni_misto_x, pocatecni_misto_y), ZEM[1]),
                         do_grafiky((pocatecni_misto_x + vx, pocatecni_misto_y + vy), ZEM[1]), 5)

        textsurface = comic_sans_font.render(
            "Nastav pocatecni pozici (leva mys) {:.2f} {:.2f} a smer (prava mys) {:.2f} {:.2f}: ".format(posx, posy, vx,
                                                                                                         vy), False,
            black)
        screen.blit(textsurface, dest=(60, 300))

    elif stav_hry == POZASTAVENA:
        textsurface = comic_sans_font.render("Pozastaveno na pozici: {:.2f} {:.2f}".format(posx, posy), False, black)
        screen.blit(textsurface, dest=(60, 300))

    elif stav_hry == NA_ZEMI:
        textsurface = comic_sans_font.render(
            "Dopadl na zem a Dosahl max vysky {:.2f} a doletel {:.2f} daleko (restart r)".format(maxy, maxx), False,
            black)
        screen.blit(textsurface, dest=(60, 300))

    if stav_hry in (POZASTAVENA, NEODSTARTOVANA, BEZI):
        textsurface = comic_sans_font.render("Start/Pause: s, Restart: r", False, black)
        screen.blit(textsurface, dest=(60, 200))

    pygame.display.flip()
    hodiny.tick(fps)

pygame.quit()