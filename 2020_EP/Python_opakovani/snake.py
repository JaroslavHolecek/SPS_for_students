import pygame
import pygame.locals as konstanty
import random
pygame.init()

FPS = 50
hodiny = pygame.time.Clock()

sirka_okna = 600
vyska_okna = sirka_okna
pocet_clanku_v_okne = 10

hlavni_okno = pygame.display.set_mode( (sirka_okna, vyska_okna) )
pygame.display.set_caption('Had')

CERVENA = (255,0,0)
MODRA = (0,0,255)
CERNA = (0,0,0)
BILA = (255, 255, 255)

pozice_hlavy_x = 1
pozice_hlavy_y = 3
ocas = [ [1, 2], [1, 1], [1, 0] ]

zradylko = [random.randint(0, pocet_clanku_v_okne-1),
            random.randint(0, pocet_clanku_v_okne-1)]

NAHORU = 1
DOLU = 2
DOLEVA = 3
DOPRAVA = 4
NIKAM = 0

posun = NIKAM
posledni_pohyb = NIKAM

# velikost_clanku = sirka_okna / pocet_clanku_v_okne -> / výsledek je desetinné číslo
velikost_clanku = sirka_okna // pocet_clanku_v_okne # // výsledek je celé číslo
hra_bezi = True
while hra_bezi:
    posun = NIKAM
    # Zpracování vstupu
        # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hra_bezi = False
        elif event.type == konstanty.KEYDOWN:
            if event.key == konstanty.K_a and posledni_pohyb != DOPRAVA:
                posun = DOLEVA
            elif event.key == konstanty.K_d and posledni_pohyb != DOLEVA:
                posun = DOPRAVA
            elif event.key == konstanty.K_w and posledni_pohyb != DOLU:
                posun = NAHORU
            elif event.key == konstanty.K_s and posledni_pohyb != NAHORU:
                posun = DOLU

            if posun in (DOLU, NAHORU, DOLEVA, DOPRAVA):
                posledni_pohyb = posun

        # Zpracování aktuálního stavu
    # klavesy = pygame.key.get_pressed() # { K_a : True, K_s : False, K_d : True, ... pro všechny klávesy }
    # if klavesy[konstanty.K_a]:
    #     pozice_hlavy_x -= 1  # pozice_x = pozice_x - 10
    # elif klavesy[konstanty.K_d]:
    #     pozice_hlavy_x += 1
    # elif klavesy[konstanty.K_w]:
    #     pozice_hlavy_y -= 1
    # elif klavesy[konstanty.K_s]:
    #     pozice_hlavy_y += 1

    # Výpočty ve hře
    if posun != NIKAM:
        ocas.pop(-1) # poslední článek smažeme
        ocas.insert(0, [pozice_hlavy_x, pozice_hlavy_y]) # přidáme nový článek na začátek s pozicí hlavy
        if posun == NAHORU: # posuneme hlavu
            pozice_hlavy_y -= 1
        elif posun == DOLU:
            pozice_hlavy_y += 1
        elif posun == DOLEVA:
            pozice_hlavy_x -= 1
        elif posun == DOPRAVA:
            pozice_hlavy_x += 1

        if pozice_hlavy_x < 0 or pozice_hlavy_x >= pocet_clanku_v_okne or \
           pozice_hlavy_y < 0 or pozice_hlavy_y >= pocet_clanku_v_okne:
            hra_bezi = False

        if [pozice_hlavy_x, pozice_hlavy_y] in ocas:
            hra_bezi = False

    # Zobrazení změn
    hlavni_okno.fill(BILA)
    pygame.draw.rect(hlavni_okno, CERVENA,
                     [pozice_hlavy_x * velikost_clanku, pozice_hlavy_y * velikost_clanku, velikost_clanku,
                      velikost_clanku])

    pygame.draw.rect(hlavni_okno, CERNA,
                     [zradylko[0] * velikost_clanku, zradylko[1] * velikost_clanku, velikost_clanku,
                      velikost_clanku])

    for clanek in ocas:
        clanek_x, clanek_y = clanek
        pygame.draw.rect(hlavni_okno, MODRA,
                         [clanek_x * velikost_clanku, clanek_y * velikost_clanku, velikost_clanku,
                          velikost_clanku])

    # Aktualizace obrazovky
    pygame.display.flip()
    # Počkat pro požadované fps
    hodiny.tick(FPS)
pygame.quit()
