import pygame
import random
pygame.init()

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

background_colour = (255,255,255)
RED = pygame.Color("red")

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake')

screen.fill(background_colour)

pygame.display.flip()
pocitadlo = 0
obdelnicek = pygame.Rect(10, 10, 100, 200)
running = True
hodiny = pygame.time.Clock()
NAHORU = 0
DOLU = 1
DOPRAVA = 2
DOLEVA = 3

BEZI = 0
KONEC_HRY = 1
PAUZA = 2
stav_hry = BEZI

class Zradylko(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,width-self.rect.w)
        self.rect.y = random.randint(0, height-self.rect.h)

class Clanek(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = width//2
        self.rect.y  = height//2
        self.smer = NAHORU

    def update(self, klavesy):
        global stav_hry
        if klavesy[pygame.K_a]:
            self.smer = DOLEVA
        elif klavesy[pygame.K_s]:
            self.smer = DOLU
        elif klavesy[pygame.K_w]:
            self.smer = NAHORU
        elif klavesy[pygame.K_d]:
            self.smer = DOPRAVA

        if self.smer == NAHORU:
            self.rect.y -= 1
        elif self.smer == DOLU:
            self.rect.y += 1
        elif self.smer == DOLEVA:
            self.rect.x -= 1
        elif self.smer == DOPRAVA:
            self.rect.x += 1


        if self.rect.x <= 0 or \
            self.rect.y <= 0 or \
            self.rect.x +self.rect.w >= width or \
            self.rect.y +self.rect.h >= height :
            print("konec hry")
            stav_hry = KONEC_HRY




had=pygame.sprite.Group()
had.add(Clanek())

potrava=pygame.sprite.Group()
potrava.add(Zradylko())



while running:
  # Zpracování vstupu
  for event in pygame.event.get(): # fronta událostí
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        print("Stiskl jsi S")

  stav_klaves = pygame.key.get_pressed() # okamžitý stav kláves
    #výpočty
  had.update(stav_klaves)
    #vykreslení
  screen.fill(background_colour) # vymazání předchozího framu

  if stav_hry == KONEC_HRY:
      text_surface = my_font.render('Konec hry', False, (0, 0, 0))
      screen.blit(text_surface, (0, 0))

  had.draw(screen)
  potrava.draw(screen)
  pygame.display.flip()
  hodiny.tick(30)

pygame.quit()