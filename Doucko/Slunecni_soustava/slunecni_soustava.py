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


polomer_slunce = 20

pozice_zeme = [100, 100]
polomer_zeme = 5


hodiny = pygame.time.Clock()
FPS = 50

running = True
# game loop
while running:
    # ZPRACOVANI VSTUPU
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # VYPOCTY


    # VYKRESLENI
    pygame.draw.circle(screen, RED, [SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2], polomer_slunce )
    pygame.draw.circle(screen, BLUE, pozice_zeme, polomer_zeme)

    pygame.display.flip()
    hodiny.tick(FPS)



pygame.quit()