import pygame
import pygame.locals as konstanty
import random
pygame.init()

# Nastavení rychlosti hry
FPS = 5
hodiny = pygame.time.Clock()

# Rozměry okna a rozlišení mřížky
sirka_okna = 600
vyska_okna = sirka_okna
pocet_clanku_v_okne = 10

# Start hry ze souboru nebo odznovu
zacatek = input("Chceš začít novou hru (N), nebo načíst ze souboru (S)?")
if zacatek not in ("S", "N"):
    print("Neplatná volba, začínám novou hru")

if zacatek == "S":
    # Načtení stavu hry ze souboru
    with open("ulozena_hra.had", "r") as soubor:
        skore = int(soubor.readline())
        zradylko = list(map(int, soubor.readline().split()))
        pozice_hlavy_x, pozice_hlavy_y = list(map(int, soubor.readline().split()))
        ocas = []
        for radek in soubor:
            ocas.append( list(map(int, radek.split())) )
else: # nastavení hodnot pro novou hru
    pozice_hlavy_x = 1
    pozice_hlavy_y = 3
    ocas = []
    skore = 0

    zradylko = [random.randint(0, pocet_clanku_v_okne - 1),
                random.randint(0, pocet_clanku_v_okne - 1)]


hlavni_okno = pygame.display.set_mode( (sirka_okna, vyska_okna) )
pygame.display.set_caption('Had')

# definice barev
CERVENA = (255,0,0)
MODRA = (0,0,255)
CERNA = (0,0,0)
BILA = (255, 255, 255)

# Nastavení fontu
font_size = 36
font = pygame.font.Font(None, font_size)

# Smer pohybu hada
NAHORU = 1
DOLU = 2
DOLEVA = 3
DOPRAVA = 4
NIKAM = 0
# aktuální a poslední pohyb hada
posun = NIKAM
posledni_pohyb = NIKAM

# definice stavů hry
BEZI = 1
KONEC = 2
PAUZA = 3
stav_hry = BEZI

# velikost_clanku = sirka_okna / pocet_clanku_v_okne -> / výsledek je desetinné číslo
velikost_clanku = sirka_okna // pocet_clanku_v_okne # // výsledek je celé číslo

# Hlavní smyčka hry
hra_bezi = True
while hra_bezi:
    # Zpracování vstupu
        # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hra_bezi = False
        elif event.type == konstanty.KEYDOWN:
            if event.key == konstanty.K_u:
                # Uložení stavu hry do souboru
                with open("ulozena_hra.had", "w") as soubor:
                    soubor.write(f"{skore}\n")
                    soubor.write(f"{zradylko[0]} {zradylko[1]}\n")
                    soubor.write(f"{pozice_hlavy_x} {pozice_hlavy_y}\n")
                    for clanek in ocas:
                        soubor.write(f"{clanek[0]} {clanek[1]}\n")

            if stav_hry == BEZI:
                # pohyb hada
                if event.key == konstanty.K_a and posledni_pohyb != DOPRAVA:
                    posun = DOLEVA
                elif event.key == konstanty.K_d and posledni_pohyb != DOLEVA:
                    posun = DOPRAVA
                elif event.key == konstanty.K_w and posledni_pohyb != DOLU:
                    posun = NAHORU
                elif event.key == konstanty.K_s and posledni_pohyb != NAHORU:
                    posun = DOLU

                # Pro zamezení pohybu opačným směrem než se had hýbe
                if posun in (DOLU, NAHORU, DOLEVA, DOPRAVA):
                    posledni_pohyb = posun

                # Pauza hry
                if event.key == konstanty.K_p:
                    stav_hry = PAUZA

            elif stav_hry == KONEC:
                # Restart hry
                if event.key == konstanty.K_r:
                    stav_hry = BEZI
                    skore = 0
                    pozice_hlavy_x = 1
                    pozice_hlavy_y = 3
                    ocas = []
                    posun = NIKAM
                    posledni_pohyb = NIKAM

            elif stav_hry == PAUZA:
                # Odpauzování hry
                if event.key == konstanty.K_p:
                    stav_hry = BEZI

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
    if stav_hry == BEZI:
        if posun != NIKAM:
            ocas.insert(0, [pozice_hlavy_x, pozice_hlavy_y]) # přidáme nový článek na začátek s pozicí hlavy
            if posun == NAHORU: # posuneme hlavu
                pozice_hlavy_y -= 1
            elif posun == DOLU:
                pozice_hlavy_y += 1
            elif posun == DOLEVA:
                pozice_hlavy_x -= 1
            elif posun == DOPRAVA:
                pozice_hlavy_x += 1

            # Náraz do stěny
            if pozice_hlavy_x < 0 or pozice_hlavy_x >= pocet_clanku_v_okne or \
               pozice_hlavy_y < 0 or pozice_hlavy_y >= pocet_clanku_v_okne:
                stav_hry = KONEC

            # Náraz do ocasu
            if [pozice_hlavy_x, pozice_hlavy_y] in ocas:
                stav_hry = KONEC

            # Sběr žrádýlka
            if pozice_hlavy_x == zradylko[0] and pozice_hlavy_y == zradylko[1]:
                zradylko = [random.randint(0, pocet_clanku_v_okne - 1),
                            random.randint(0, pocet_clanku_v_okne - 1)]
                skore += 1
            else:
                ocas.pop(-1)  # poslední článek smažeme když jsme nesebrali žrádýlko

    # Zobrazení změn
    hlavni_okno.fill(BILA)
    # had + žrádýlko
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

    # Různé výpisy pro různé stavy hry
    if stav_hry == BEZI or stav_hry == PAUZA:
        text_surface = font.render(f"Skóre: {skore}", True, CERNA)
        hlavni_okno.blit(text_surface, (10, 10))
    if stav_hry == PAUZA:
        text_surface = font.render(f"Pauza, stiskni p pro pokračování", True, CERNA)
        hlavni_okno.blit(text_surface, (10, 30))
    if stav_hry == KONEC:
        text_surface = font.render(f"Konec hry, dosáhl jsi: {skore} bodů, stiskni r pro restart", True, CERNA)
        hlavni_okno.blit(text_surface, (10, 10))

    # Aktualizace obrazovky
    pygame.display.flip()
    # Počkat pro požadované fps
    hodiny.tick(FPS)
pygame.quit()
