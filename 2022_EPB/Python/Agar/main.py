# vytvořit jako Sprite
# -> prekážky
# -> kolize objektů přes sprite.Group
# =========================================
# OOP - dědičnost
# =========================================
# Dlouhodobě - potřeba udržovat pořád
# Řízení stavů hry - HRA, PAUZA, KONEC HRY, MENU
import random
import pygame
from Tools.demo.spreadsheet import center

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
class Hrac(pygame.sprite.Sprite):
    def __init__(self, pozice, radius, rychlost, barva, ovladani):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([2*radius, 2*radius])
        self.image.fill(pygame.Color("white"))
        pygame.draw.circle(self.image, barva, [radius, radius], radius)

        self.rect = self.image.get_rect(center = pozice)

        self.rychlost = rychlost
        self.ovladani = ovladani # klávesy: [nahoru, dolu, doleva, doprava]

    def update(self, dt, keys):
        if keys[self.ovladani[0]]:
            self.rect.y -= self.rychlost * dt
        if keys[self.ovladani[1]]:
            self.rect.y += self.rychlost * dt
        if keys[self.ovladani[2]]:
            self.rect.x -= self.rychlost * dt
        if keys[self.ovladani[3]]:
            self.rect.x += self.rychlost * dt

class Zradylko(pygame.sprite.Sprite):
    def __init__(self, velikost, pozice):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([velikost, velikost])
        self.image.fill(pygame.Color("orange"))

        self.rect = self.image.get_rect(center = pozice)
        self.hodnota = 5

H1 = Hrac(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2),
          40,
          300,
          pygame.Color("red"),
          [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])

H2 = Hrac(pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3),
          40,
          300,
          pygame.Color("blue"),
          [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

vsichni_hraci = pygame.sprite.Group()
vsichni_hraci.add(H1)
vsichni_hraci.add(H2)

vsechny_zradylka = pygame.sprite.Group()
for i in range(0,50):
    vsechny_zradylka.add(Zradylko(20, pygame.Vector2(
        random.randint(0, screen.get_width()),
        random.randint(0, screen.get_height()) )
                                  )
                         )

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

            if (not stav_hry == KONEC_HRY) and event.key == pygame.K_p:
                if stav_hry == PAUZA:
                    stav_hry = HRA_BEZI
                elif stav_hry == HRA_BEZI:
                    stav_hry = PAUZA

            if event.key == pygame.K_r:
                # restart
                boss_rect = obrazek_boss.get_rect(center=(400, 500))
                player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                player2_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                cas_hry = 0
                stav_hry = HRA_BEZI


    if stav_hry == HRA_BEZI:
        # Zpracování kláves v tomto konkrétním okamžiku (jednou za frame)
        keys = pygame.key.get_pressed()
        vsichni_hraci.update(dt, keys)

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
            stav_hry = KONEC_HRY

        for hrac in vsichni_hraci:
            if hrac.rect.x < 0 or hrac.rect.x > screen.get_width():
                hrac.rect.x = screen.get_width()/2
            if hrac.rect.y < 0 or hrac.rect.y > screen.get_height():
                hrac.rect.y = screen.get_height()/2

        # if (player_radius + player2_radius)**2 > (player_pos.x - player2_pos.x)**2 + (player_pos.y - player2_pos.y)**2:
        #     player_color = pygame.Color("white")
        # else:
        #     player_color = pygame.Color("black")

    text_stavu = ""
    if stav_hry == PAUZA:
        text_stavu = "Pauza, stiskni P pro pokračování"
    elif stav_hry == HRA_BEZI:
        text_stavu = "Hra běží"
    elif stav_hry == KONEC_HRY:
        text_stavu = "Konec hry, stisni r pro restart"
    obrazek_stavu = font.render(text_stavu, True, barva_textu)
    stav_rect = obrazek_stavu.get_rect(center=(200, 600))


    # >>>>>> Z o b r a z e n í   a k t u á l n í h o   f r a m u <<<<<<<
    # Vymazání předchozího framu
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Vykreslení hráčů
    vsichni_hraci.draw(screen)

    # Vykreslení žrádýlek
    vsechny_zradylka.draw(screen)

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