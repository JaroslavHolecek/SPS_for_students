# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()


informacni_font = pygame.font.Font(None, 50)

class Hrac(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.image.load("./2024_EP/Python/Pygame/lod.png")

        # pozice objektu je uložená v "rect" -> zle ji měnit přes rect.x atd.
       self.rect = self.image.get_rect()


hrac1 = Hrac("red", 200, 50)
hrac2 = Hrac("blue", 200, 50)

vsichni_hraci = pygame.sprite.Group()
vsichni_hraci.add(hrac1)
vsichni_hraci.add(hrac2)


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
ubehly_cas = 0
pocet_framu = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Hlavní smyčka
while running:

    ## Zpracování vstupu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("Stisk")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        hrac1.rect.y -= 300 * dt
    if keys[pygame.K_s]:
        hrac1.rect.y += 300 * dt
    if keys[pygame.K_a]:
        hrac1.rect.x -= 300 * dt
    if keys[pygame.K_d]:
        hrac1.rect.x += 300 * dt

    if keys[pygame.K_UP]:
        hrac2.rect.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        hrac2.rect.y += 300 * dt
    if keys[pygame.K_LEFT]:
        hrac2.rect.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        hrac2.rect.x += 300 * dt

    kolize = pygame.sprite.collide_rect(hrac1, hrac2) #jeden objekt vs. druhý objekt
    # seznam_trefenych = pygame.sprite.spritecollide() #jeden objekt vs. skupina

    if kolize:
        print("Kolize")

    ## Výpočty ve hře

    ## Zobrazení stavu na monitor
    screen.fill("purple") # smazat starý stav

    obrazek_textu = informacni_font.render(f"Uběhlý čas {ubehly_cas}", False, "black")
    screen.blit(obrazek_textu, (100, 50), area=(0,0,100,50))

    # vykreslit nový stav
    pygame.draw.circle(screen, "red", player_pos, 40)
    vsichni_hraci.draw(screen)

    pygame.display.flip() # odeslání změn na monitor

    ## Pauza pro FPS
    dt = clock.tick(60) / 1000 # pauza + kolik času uběhlo v sekundách
    ubehly_cas += dt
    pocet_framu += 1

    print(f"Uběhlý čas: {ubehly_cas} a framů: {pocet_framu}")

    

pygame.quit()