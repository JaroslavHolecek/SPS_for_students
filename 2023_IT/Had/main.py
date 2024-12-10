# Example file showing a circle moving on screen
import pygame

# >>>>>>>> inicializace <<<<<<<<<
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True # boolean
dt = 0 # int
FPS = 60
pozadi = pygame.Color("purple")
background_image = pygame.image.load("images/pozadi_vlk.jpg")  # Nahraďte 'background.jpg' cestou k vašemu obrázku
background_image = pygame.transform.scale(background_image, screen.get_size())  # Přizpůsobení velikosti obrazovky


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40
player_color = pygame.Color("red")
player_speed = 300

MOVE_UP = pygame.Vector2(0, -1)
MOVE_DOWN = pygame.Vector2(0, 1)
MOVE_LEFT = pygame.Vector2(-1, 0)
MOVE_RIGHT = pygame.Vector2(1, 0)

# >>>>>>>> hlavni cyklus hry <<<<<<<<<
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # >>>>>>>> zpracovani vstupu <<<<<<<<<
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player_move = pygame.Vector2(0,0)
    if keys[pygame.K_w]:
        player_move += MOVE_UP
    if keys[pygame.K_s]:
        player_move += MOVE_DOWN
    if keys[pygame.K_a]:
        player_move += MOVE_LEFT
    if keys[pygame.K_d]:
        player_move += MOVE_RIGHT

    # >>>>>>>> výpočty hry <<<<<<<<<
    player_pos += player_move * player_speed * dt


    # fill the screen with a color to wipe away anything from last frame
    # >>>>>>>> zobrazení <<<<<<<<<
    screen.blit(background_image, (0, 0))

    pygame.draw.circle(screen, player_color, player_pos, player_radius)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # >>>>>>>> pauza <<<<<<<<<
    dt = clock.tick(FPS) / 1000 # v sekundách

pygame.quit()