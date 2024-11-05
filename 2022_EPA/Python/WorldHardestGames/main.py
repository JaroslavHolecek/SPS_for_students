# -> Řízení stavů hry - KONEC HRY + restart, MENU - nápisy/tlačítka nemusí nic dělat, jen ať tam jsou
# =================
# OOP + Sprite

# Example file showing a circle moving on screen
import pygame
print("Loading...")

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
FPS = 60
pozice_casu = (600, 100)
background_color = pygame.Color("purple")

# Výběr písma a velikosti
font = pygame.font.Font(None, 74)  # Žádné písmo, velikost 74

# Načtení obrázku ze souboru
obrazek_boss = pygame.image.load("img/boss.png")
# A zjištění jeho rozměrů + nastavení pozice
boss_rect = obrazek_boss.get_rect(center=(500, 250))


# Hodnoty hráčů
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 300 # px/s
player_radius = 40
player_color = pygame.Color("red")
body = 0
naraz_do_steny_penalta = -2
naraz_mezi_hraci = 1

player2_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_speed = 300 # px/s
player2_radius = 40
player2_color = pygame.Color("blue")

# Hodnoty překážek
ctverec = pygame.Rect([100, 200, 10, 20])
ctverec_barva = pygame.Color("yellow")

# Past
past_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 4)
past_radius = 40
past_color = pygame.Color("black")

# Vytvoření textu pro zobrazení
text = "Text na zkoušku"
barva_textu = pygame.Color("green")
# Vyrendrování obrázku s textem
obrazek_textu = font.render(text, True, barva_textu)
# A zjištění jeho velikosti + určení pozice
text_rect = obrazek_textu.get_rect(center=(200, 50))

max_doba_behu = 10

HRA_BEZI = 1
PAUZA = 2

stav_hry = HRA_BEZI

# Zaznamenání času při spuštění hry (po načtení všech hodnot/obrázků a pod.)
cas_zacatku = pygame.time.get_ticks()
cas_hry = 0 # v sekundach
while running:
    # >>>>>>> Z p r a c o v á n í   v s t u p u <<<<<<<
    # Zpracování událostí, kdybkoliv v průběhu programu
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_p:
                if stav_hry == PAUZA:
                    stav_hry = HRA_BEZI
                elif stav_hry == HRA_BEZI:
                    stav_hry = PAUZA

    if stav_hry == HRA_BEZI:
        # Zpracování stavy kláves v jednom konrétním okamžiku (jednou za frame)
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

    # >>>>>>> V ý p o č t y   v e   h ř e <<<<<<<
    # Aktualizace času
    if stav_hry == PAUZA:
        pass
    elif stav_hry == HRA_BEZI:
        cas_hry += dt
        zbyvajici_cas = max_doba_behu - cas_hry

    if cas_hry >= max_doba_behu:
        running = False

    # Hrac nemuze mimo obrazovku
    if stav_hry == HRA_BEZI:
        if player_pos.x < 0:
            player_pos.x = 0
            body += naraz_do_steny_penalta
        elif player_pos.x > screen.get_width():
            player_pos.x = screen.get_width()
            body += naraz_do_steny_penalta
        if player_pos.y < 0:
            player_pos.y = 0
            body += naraz_do_steny_penalta
        elif player_pos.y > screen.get_height():
            player_pos.y = screen.get_height()
            body += naraz_do_steny_penalta

        if player2_pos.x < 0:
            player2_pos.x = 0
        elif player2_pos.x > screen.get_width():
            player2_pos.x = screen.get_width()
        if player2_pos.y < 0:
            player2_pos.y = 0
        elif player2_pos.y > screen.get_height():
            player2_pos.y = screen.get_height()

    # Sražení objektů
    if player_pos.distance_to(player2_pos) < player_radius + player2_radius:
        body += naraz_mezi_hraci

    if player_pos.distance_to(past_pos) < player_radius + past_radius:
        running = False
    # pygame.sprite.collide_rect()
    # pygame.sprite.collide_circle()




    # >>>>>>> V y k r e s l e n í   a   z o b r a z e n í   n a   o b r a z o v k u <<<<<<<

    # smazání předchozího framu
    screen.fill(background_color)

    if stav_hry == HRA_BEZI:
        # Hraci
        pygame.draw.circle(screen, player_color, player_pos, player_radius)
        pygame.draw.circle(screen, player2_color, player2_pos, player2_radius)
        # Prekazky
        pygame.draw.rect(screen, ctverec_barva, ctverec)
        # Nepritel - Vykreslení načteného obrázku
        screen.blit(obrazek_boss, boss_rect)
        # Past
        pygame.draw.circle(screen, past_color, past_pos, past_radius)
        # Vykreslení textu
        screen.blit(obrazek_textu, text_rect)
        # Zobrazení bodů
        obrazek_body = font.render(f"Body: {body}", True, (0, 0, 0))
        screen.blit(obrazek_body, (500, 500))

    elif stav_hry == PAUZA:
        # Napis pauza
        obrazek_pauza = font.render(f"Pauza", True, (0, 0, 0))
        screen.blit(obrazek_pauza, (500, 500))

    # Zobrazuje se vždy
    # Doba běhu
    obrazek_casu = font.render(f"Doba běhu: {int(cas_hry)} s, zbývá {int(zbyvajici_cas)}", True, (0, 0, 0))
    screen.blit(obrazek_casu, pozice_casu)

    # Zobrazení změn na monitoru
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000 # [sec]

pygame.quit()