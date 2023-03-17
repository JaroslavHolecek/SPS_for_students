import pygame
import random

pygame.init()
vyska = 600
sirka = 1000
background_colour = (234, 212, 252)
background = pygame.Surface([sirka, vyska])
background.fill(background_colour)

pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)

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
        self.maxpocetstrel = 20
    def update(self, klavesy, seznamstrel):
        if klavesy[pygame.K_a]:
            self.rect[0] = self.rect[0] - self.rychlost * (dt//10)
        if klavesy[pygame.K_d]:
            self.rect[0] = self.rect[0] + self.rychlost * (dt//10)
        if klavesy[pygame.K_SPACE]:
            if self.maxpocetstrel > len(seznamstrel):
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
def pridej_nepratele(pocet, kam):
    for p in range(pocet):
        kam.add(Nepritel(random.randint(0, sirka), 10))

vsichni_nepratele = pygame.sprite.Group()
pridej_nepratele(2,vsichni_nepratele)

vsechny_strely = pygame.sprite.Group()


pygame.display.flip()
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(FPS)
running = True
PAUSE = 1
stav_hry = PAUSE
BEZI = 0
unpaused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if stav_hry == BEZI:
                    stav_hry = PAUSE
                elif stav_hry == PAUSE:
                    stav_hry = BEZI
                    unpaused = True

    if PAUSE == stav_hry:
        pass

    elif stav_hry == BEZI:
        # výpočty
        klavesy = pygame.key.get_pressed()
        vsichni_hraci.update(klavesy, vsechny_strely)
        vsechny_strely.update(dt)
        vsichni_nepratele.update(dt)


        pygame.sprite.groupcollide(vsechny_strely, vsichni_nepratele, True, True)
        if len(vsichni_nepratele)< 2:
            pridej_nepratele(3, vsichni_nepratele)

        for strela in vsechny_strely:
            if strela.rect.y < 0:
                vsechny_strely.remove(strela)

    #vykreslovani
    # screen.blit(obrazek_hrac,dest = hrac_pozice)
    # screen.blit(obrazek_enemy, dest=enemy_pozice)
    if stav_hry == PAUSE:
        text_surface = my_font.render('Pause: Press Escape to Continue', False, (0, 0, 0))
        screen.blit(text_surface, (sirka//2,vyska//2))
    if unpaused == True:
        screen.fill(background_colour)
        unpaused = False

    vsichni_hraci.clear(screen, background)
    vsichni_hraci.draw(screen)
    vsechny_strely.clear(screen, background)
    vsechny_strely.draw(screen)
    vsichni_nepratele.clear(screen, background)
    vsichni_nepratele.draw(screen)
    pygame.display.flip()
    dt = clock.tick(FPS)
pygame.quit()