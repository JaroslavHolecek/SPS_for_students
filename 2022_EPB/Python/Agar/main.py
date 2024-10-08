# =========================================
# OOP - Sprite
# =========================================
# Řízení stavů hry - HRA, PAUZA, KONEC HRY, MENU

import pygame

# Nastavení parametrů hry
pygame.init()
#                                0 - 1280, 0 - 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
FPS = 60
max_cas_hry = 10 # s
# Nastavení fontu
font = pygame.font.Font(None, 74)

HRA_BEZI = 1
PAUZA = 2
KONEC_HRY = 3

# Načtení obrázku ze souboru
obrazek_boss = pygame.image.load("img/boss.png")
boss_rect = obrazek_boss.get_rect(center=(400,500))

# Hodnoty hráčů
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 300 # px / s
player_radius = 40
player_color = pygame.Color("red")

player2_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_speed = 300 # px / s
player2_radius = 40
player2_color = pygame.Color("blue")

# Hodnoty překážek
ctverec_barva = pygame.Color("yellow")
ctverec = pygame.Rect([200, 300, 30,30])

# Vytvoření obrázku z textu
text = "Doufám, že se ti hra líbí"
barva_textu = pygame.Color("red")
obrazek_textu = font.render(text, True, barva_textu)
text_rect = obrazek_textu.get_rect(center=(300,50))

cas_start = pygame.time.get_ticks() // 1000
cas_hry = 0
stav_hry = HRA_BEZI
while running:
    # >>>>>> Z p r a c o v á n í   v s t u p u <<<<<<<
    # Zpracování událostí z libovolné chvíle hry
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_p:
                if stav_hry == PAUZA:
                    stav_hry = HRA_BEZI
                elif stav_hry == HRA_BEZI:
                    stav_hry = PAUZA

    if stav_hry == HRA_BEZI:
        # Zpracování kláves v tomto konkrétním okamžiku (jednou za frame)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= player_speed * dt
        if keys[pygame.K_s]:
            player_pos.y += player_speed * dt
        if keys[pygame.K_a]:
            player_pos.x -= player_speed * dt
        if keys[pygame.K_d]:
            player_pos.x += player_speed * dt

        if keys[pygame.K_UP]:
            player2_pos.y -= player2_speed * dt
        if keys[pygame.K_DOWN]:
            player2_pos.y += player2_speed * dt
        if keys[pygame.K_LEFT]:
            player2_pos.x -= player2_speed * dt
        if keys[pygame.K_RIGHT]:
            player2_pos.x += player2_speed * dt

        if keys[pygame.K_i]:
            boss_rect.y -= player_speed * dt
        if keys[pygame.K_k]:
            boss_rect.y += player_speed * dt
        if keys[pygame.K_j]:
            boss_rect.x -= player_speed * dt
        if keys[pygame.K_l]:
            boss_rect.x += player_speed * dt

    # >>>>>>>> V ý p o č t y   v e   h ř e <<<<<<<<<
    if stav_hry == HRA_BEZI:
        # Výpočet doby hry
        # aktualni_cas = pygame.time.get_ticks() // 1000
        cas_hry = cas_hry + dt
        cas_hry_s = int(cas_hry)
        cas_zbyva = max_cas_hry - cas_hry_s
        obrazek_casomiry = font.render(f"Uběhnutý čas: {cas_hry_s}, zbývá {cas_zbyva}", True, barva_textu)
        casomira_rect = obrazek_casomiry.get_rect(center=(900, 50))

        if cas_zbyva <= 0:
            running = False

        # Udržení hráčů v okně
        if player_pos.x < 0 or player_pos.x > screen.get_width():
            player_pos.x = screen.get_width()/2
        if player_pos.y < 0 or player_pos.y > screen.get_height():
            player_pos.y = screen.get_height()/2

        if player2_pos.x < 0 or player2_pos.x > screen.get_width():
            player2_pos.x = screen.get_width()/2
        if player2_pos.y < 0 or player2_pos.y > screen.get_height():
            player2_pos.y = screen.get_height()/2

        if (player_radius + player2_radius)**2 > (player_pos.x - player2_pos.x)**2 + (player_pos.y - player2_pos.y)**2:
            player_color = pygame.Color("white")
        else:
            player_color = pygame.Color("black")

    text_stavu = ""
    if stav_hry == PAUZA:
        text_stavu = "Pauza, stiskni P pro pokračování"
    elif stav_hry == HRA_BEZI:
        text_stavu = "Hra běží"
    obrazek_stavu = font.render(text_stavu, True, barva_textu)
    stav_rect = obrazek_stavu.get_rect(center=(200, 600))


    # >>>>>> Z o b r a z e n í   a k t u á l n í h o   f r a m u <<<<<<<
    # Vymazání předchozího framu
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Vykreslení hráčů
    pygame.draw.circle(screen, player_color, player_pos, player_radius)
    pygame.draw.circle(screen, player2_color, player2_pos, player2_radius)

    # Vykreslení překážky
    pygame.draw.rect(screen, ctverec_barva, ctverec)
    # flip() the display to put your work on screen

    # Vykreslení textu
    screen.blit(obrazek_textu, text_rect)

    #Vykreslení textu s časomírou
    screen.blit(obrazek_casomiry, casomira_rect)

    # Vykresleni stavu
    screen.blit(obrazek_stavu, stav_rect)

    # Vykrelsení načteného obrázku
    screen.blit(obrazek_boss, boss_rect)
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pygame.quit()