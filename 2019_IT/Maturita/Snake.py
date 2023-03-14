import pygame
pygame.init()

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

class Clanek(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([10, 10])
       self.image.fill((0, 255, 0))
       self.rect = self.image.get_rect()

had=pygame.sprite.Group()
had.add(Clanek())

while running:
  # Zpracování vstupu
  for event in pygame.event.get(): # fronta událostí
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        print("Stiskl jsi S")

  stav_klaves = pygame.key.get_pressed() # okamžitý stav kláves
  if stav_klaves[pygame.K_a]:
    obdelnicek.x += 1
    #výpočty

  #vykreslení
  screen.fill(background_colour)
  had.draw(screen)
  pygame.display.flip()
  hodiny.tick(30)

pygame.quit()