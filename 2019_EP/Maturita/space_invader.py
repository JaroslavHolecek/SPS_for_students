import pygame
import random

pygame.init()
vyska = 600
sirka = 1000
background_colour = (234, 212, 252)
background = pygame.Surface([sirka, vyska])
background.fill(background_colour)

black = (0, 0, 0)
screen = pygame.display.set_mode((sirka, vyska))

pygame.display.set_caption('Spaceinvader')

screen.fill(background_colour)

class Hrac(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hrac.jpg")
        self.rect = self.image.get_rect()
        self.rect[0] = sirka//2
        self.rect[1] = vyska-self.rect[3]
        self.rychlost = 10

    def update(self, klavesy, seznamstrel):
        if klavesy[pygame.K_a]:
            self.rect[0] = self.rect[0] - self.rychlost * (dt//10)
        if klavesy[pygame.K_d]:
            self.rect[0] = self.rect[0] + self.rychlost * (dt//10)
        if klavesy[pygame.K_NUMLOCK]:
            seznamstrel.add(Strela(self))

class Nepritel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.jpg")
        self.rect = self.image.get_rect()
        self.rect[0] = min(x,sirka-self.rect[3])
        self.rect[1] = y
        self.rychlost = 1

    def update(self, dt):
        self.rect[1] = self.rect[1] + self.rychlost * (dt // 10)


class Strela(pygame.sprite.Sprite):
    def __init__(self, hrac:Hrac):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([6,6])
        self.rect = self.image.get_rect()
        self.rect[0] = hrac.rect[0]
        self.rect[1] = hrac.rect[1]
        self.rychlost = 1

    def update(self, dt):
        self.rect[1] = self.rect[1] - self.rychlost * (dt // 10)

vsichni_hraci = pygame.sprite.Group()

vsichni_hraci.add(Hrac())

vsichni_nepratele = pygame.sprite.Group()
for p in range(10):
    vsichni_nepratele.add(Nepritel(random.randint(0,sirka),10))

vsechny_strely = pygame.sprite.Group()


pygame.display.flip()
clock = pygame.time.Clock()
FPS = 60

dt = clock.tick(FPS)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    klavesy = pygame.key.get_pressed()
    vsichni_hraci.update(klavesy,vsechny_strely)

        #výpočty
    vsechny_strely.update(dt)
    vsichni_nepratele.update(dt)
    #vykreslovani
    # screen.blit(obrazek_hrac,dest = hrac_pozice)
    # screen.blit(obrazek_enemy, dest=enemy_pozice)
    vsichni_hraci.clear(screen, background)
    vsichni_hraci.draw(screen)
    vsechny_strely.clear(screen, background)
    vsechny_strely.draw(screen)
    vsichni_nepratele.clear(screen, background)
    vsichni_nepratele.draw(screen)
    pygame.display.flip()
    dt = clock.tick(FPS)
pygame.quit()