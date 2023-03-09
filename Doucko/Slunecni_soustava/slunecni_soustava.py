import math
# import the pygame module
import pygame
pygame.init()

# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)
RED = pygame.Color("red")
BLUE = pygame.Color("blue")

# Define the dimensions of
# screen object(width,height)
            #  0    1
SCREEN_SIZE = (300, 300)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the caption of the screen
pygame.display.set_caption('Sluneční soustava')

# Fill the background colour to the screen
screen.fill(background_colour)

pozice_slunce = [SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2]
polomer_slunce = 20

class Planeta(pygame.sprite.Sprite):
    def __init__(self, polomer, vzdalenost_od_slunce, rychlost_obehu): # initialization - vytvoření
        pygame.sprite.Sprite.__init__(self) #super.__init__(self)

        self.image = pygame.Surface([2*polomer, 2*polomer])
        pygame.draw.circle(self.image, BLUE, [polomer, polomer], polomer)

        # rectangle -> [levy_horni_x, levy_horni_y, sirka, vyska]
        self.rect = self.image.get_rect()

        self.vzdalenost_od_slunce = vzdalenost_od_slunce
        self.rychlost_obehu = rychlost_obehu

    def update(self, ubehnuty_cas):
        self.rect.x = int(
            pozice_slunce[0] + self.vzdalenost_od_slunce * math.sin(self.rychlost_obehu * ubehnuty_cas))  # x
        self.rect.y = int(
            pozice_slunce[1] + self.vzdalenost_od_slunce * math.cos(self.rychlost_obehu * ubehnuty_cas))  # y


vsechny_planety = pygame.sprite.Group()
vsechny_planety.add(Planeta(polomer=5, vzdalenost_od_slunce=100, rychlost_obehu=0.001))
vsechny_planety.add(Planeta(2, 50, 0.002))
# for i in range(1,10):
#     vsechny_planety.add(Planeta(5, 100, i*0.001))


hodiny = pygame.time.Clock()
FPS = 100

start_time = pygame.time.get_ticks()
running = True
# game loop
while running:
    # ZPRACOVANI VSTUPU
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # VYPOCTY
    actual_time = pygame.time.get_ticks()
    ubehnuty_cas = actual_time - start_time

    vsechny_planety.update(ubehnuty_cas)

    # VYKRESLENI
    screen.fill(background_colour)

    vsechny_planety.draw(screen)
    pygame.draw.circle(screen, RED, pozice_slunce, polomer_slunce)

    pygame.display.flip()
    hodiny.tick(FPS)



pygame.quit()