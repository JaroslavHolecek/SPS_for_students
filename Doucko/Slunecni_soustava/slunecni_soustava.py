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
            #  0    1
pozice_zeme = [100, 100]
polomer_zeme = 5
vzdalenost_zeme_od_slunce = 100
rychlost_obehu = 0.001


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

    pozice_zeme[0] = int(pozice_slunce[0] + vzdalenost_zeme_od_slunce*math.sin(rychlost_obehu * ubehnuty_cas) ) # x
    pozice_zeme[1] = int(pozice_slunce[1] + vzdalenost_zeme_od_slunce*math.cos(rychlost_obehu * ubehnuty_cas) ) # y

    # VYKRESLENI
    screen.fill(background_colour)

    pygame.draw.circle(screen, RED, pozice_slunce, polomer_slunce )
    pygame.draw.circle(screen, BLUE, pozice_zeme, polomer_zeme)

    pygame.display.flip()
    hodiny.tick(FPS)



pygame.quit()