# -> Řízení stavů hry - KONEC HRY + restart, MENU - nápisy/tlačítka nemusí nic dělat, jen ať tam jsou
# =================
# Překážky jako Sprite, Žetonky pro sbíraní jako Sprite, Past jako Sprite

# Example file showing a circle moving on screen
import pygame
from Tools.demo.spreadsheet import center

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

class Hrac(pygame.sprite.Sprite):
    def __init__(self, rychlost, pozice, barva, radius, ovladani):
        pygame.sprite.Sprite.__init__(self) # vytváříme objekt Sprite

        self.rychlost = rychlost
        self.barva = barva
        self.body = 0
        self.ovladani = ovladani # [nahoru, dolu, doleva, doprava]
        self.radius = radius

        self.image = pygame.Surface([2*radius, 2*radius])
        self.image.fill(pygame.Color("black"))
        pygame.draw.circle(self.image, self.barva, (radius, radius), radius)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=pozice)

    def update(self, keys, dt):
        if keys[self.ovladani[0]]:
            self.rect.y -= self.rychlost * dt
        if keys[self.ovladani[1]]:
            self.rect.y += self.rychlost * dt
        if keys[self.ovladani[2]]:
            self.rect.x -= self.rychlost * dt
        if keys[self.ovladani[3]]:
            self.rect.x += self.rychlost * dt

        pygame.draw.circle(self.image, self.barva, (self.radius, self.radius), self.radius)
        obrazek_bodu = font.render(f"{self.body}", True, (0, 0, 0))
        pozice = obrazek_bodu.get_rect(center=(self.radius, self.radius))
        self.image.blit(obrazek_bodu, pozice)


H1 = Hrac(300, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2),
          pygame.Color("red"), 40,
          [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])

H2 = Hrac(100, pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3),
          pygame.Color("blue"), 30,
          [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

vsichni_hraci = pygame.sprite.Group()
vsichni_hraci.add([H1, H2])

# Hodnoty hráčů
naraz_do_steny_penalta = -2
naraz_mezi_hraci = 1

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

max_doba_behu = 100

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
        vsichni_hraci.update(keys, dt)

    # >>>>>>> V ý p o č t y   v e   h ř e <<<<<<<
    if cas_hry >= max_doba_behu:
        running = False

    if stav_hry == PAUZA:
        pass
    elif stav_hry == HRA_BEZI:
        cas_hry += dt
        zbyvajici_cas = max_doba_behu - cas_hry

        # Hrac nemuze mimo obrazovku
        for hrac in vsichni_hraci:
            if hrac.rect.x < 0:
                hrac.rect.x = 0
            elif hrac.rect.x > screen.get_width():
                hrac.rect.x = screen.get_width()
            if hrac.rect.y < 0:
                hrac.rect.y = 0
            elif hrac.rect.y > screen.get_height():
                hrac.rect.y = screen.get_height()
    #
        # Sražení hráčů
        if pygame.sprite.collide_rect(H1, H2) :
            H1.body += naraz_mezi_hraci
            H2.body += naraz_mezi_hraci

    # if player_pos.distance_to(past_pos) < player_radius + past_radius:
    #     running = False
    # pygame.sprite.collide_rect()
    # pygame.sprite.collide_circle()




    # >>>>>>> V y k r e s l e n í   a   z o b r a z e n í   n a   o b r a z o v k u <<<<<<<

    # smazání předchozího framu
    screen.fill(background_color)

    if stav_hry == HRA_BEZI:
        # Hraci
        vsichni_hraci.draw(screen)
        # Prekazky
        pygame.draw.rect(screen, ctverec_barva, ctverec)
        # Nepritel - Vykreslení načteného obrázku
        screen.blit(obrazek_boss, boss_rect)
        # Past
        pygame.draw.circle(screen, past_color, past_pos, past_radius)
        # Vykreslení textu
        screen.blit(obrazek_textu, text_rect)
        # Zobrazení bodů
        # obrazek_body = font.render(f"Body: {body}", True, (0, 0, 0))
        # screen.blit(obrazek_body, (500, 500))

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