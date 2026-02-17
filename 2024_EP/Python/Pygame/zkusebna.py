# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

class Hrac(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.image.load("./2024_EP/Python/Pygame/lod.png")

       self.rect = self.image.get_rect()


hrac1 = Hrac("red", 200, 50)

vsichni_hraci = pygame.sprite.Group()
vsichni_hraci.add(hrac1)


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Hlavní smyčka
while running:

    ## Zpracování vstupu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    ## Výpočty ve hře

    ## Zobrazení stavu na monitor
    screen.fill("purple") # smazat starý stav

    # vykreslit nový stav
    pygame.draw.circle(screen, "red", player_pos, 40)
    vsichni_hraci.draw(screen)

    pygame.display.flip() # odeslání změn na monitor

    ## Pauza pro FPS
    dt = clock.tick(60) / 1000 # pauza + kolik času uběhlo v sekundách

    

pygame.quit()