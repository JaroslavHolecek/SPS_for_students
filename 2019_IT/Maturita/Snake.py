import pygame
pygame.init()

background_colour = (255,255,255)
RED = pygame.Color("red")

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake')

screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
  # Zpracování vstupu
  for event in pygame.event.get(): # fronta událostí
    if event.type == pygame.QUIT:
      running = False

  stav_klaves = pygame.key.get_pressed() # okamžitý stav kláves


pygame.quit()