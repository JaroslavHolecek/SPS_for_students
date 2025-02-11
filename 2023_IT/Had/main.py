# Example file showing a circle moving on screen
import pygame
import random

# >>>>>>>> inicializace <<<<<<<<<
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True # boolean
dt = 0 # int
FPS = 60
font_color = pygame.Color("purple")
font_info = pygame.font.Font(None, 48)
background_image = pygame.image.load("images/pozadi_vlk.jpg")  # Nahraďte 'background.jpg' cestou k vašemu obrázku
background_image = pygame.transform.scale(background_image, screen.get_size())  # Přizpůsobení velikosti obrazovky


SNAKE_POSITION = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
SNAKE_SIZE = 80
SNAKE_COLOR = pygame.Color("red")
SNAKE_SPEED = 100

MOVE_UP = pygame.Vector2(0, -1)
MOVE_DOWN = pygame.Vector2(0, 1)
MOVE_LEFT = pygame.Vector2(-1, 0)
MOVE_RIGHT = pygame.Vector2(1, 0)
MOVE_NONE = pygame.Vector2(0, 0)
automatic_move = MOVE_NONE.copy()

# Herní objekt, který se bude zobrazovat a interagovat s ostatními objekty - dědíme od třídy Sprite
class Jidlo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/jablko.png")
        self.rect = self.image.get_rect(center=(100,100)) # pozice a velikost objektu

    def update(self):
        # TODO: ať není navázané na FPS
        self.rect.x += random.choice([-1, 0, 1])  # Random horizontal movement
        self.rect.y += random.choice([-1, 0, 1])  # Random vertical movement

class Had(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.image, SNAKE_COLOR, (SNAKE_SIZE // 2, SNAKE_SIZE // 2), SNAKE_SIZE // 2)
        self.rect = self.image.get_rect(center=SNAKE_POSITION)
        self.speed = SNAKE_SPEED

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, nove_x):
        if nove_x < 0:
            nove_x = 0
        elif nove_x > screen.get_width() - self.rect.width:
            nove_x = screen.get_width() - self.rect.width

        self.rect.x = nove_x

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, nove_y):
        if nove_y < 0:
            nove_y = 0
        elif nove_y > screen.get_height() - self.rect.height:
            nove_y = screen.get_height() - self.rect.height

        self.rect.y = nove_y

    def update(self, direction, dt):
        pohyb = direction * self.speed * dt
        self.x += pohyb[0]
        self.y += pohyb[1]


hrac_had = Had()
hrac_skupina = pygame.sprite.Group()
hrac_skupina.add(hrac_had)

vsechna_jidla = pygame.sprite.Group()
j1 = Jidlo()
vsechna_jidla.add(j1)

STATE_PLAY = 0
STATE_PAUSE = 1

ACTUAL_STATE = STATE_PLAY
# >>>>>>>> hlavni cyklus hry <<<<<<<<<
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # >>>>>>>> zpracovani vstupu <<<<<<<<<
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ACTUAL_STATE == STATE_PLAY:
                    ACTUAL_STATE = STATE_PAUSE
                elif ACTUAL_STATE == STATE_PAUSE:
                    ACTUAL_STATE = STATE_PLAY

    if ACTUAL_STATE == STATE_PLAY:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            automatic_move = MOVE_UP
        if keys[pygame.K_s]:
            automatic_move = MOVE_DOWN
        if keys[pygame.K_a]:
            automatic_move = MOVE_LEFT
        if keys[pygame.K_d]:
            automatic_move = MOVE_RIGHT

    # >>>>>>>> výpočty hry <<<<<<<<<
    if ACTUAL_STATE == STATE_PLAY:
        vsechna_jidla.update()

        player_move = MOVE_NONE.copy()
        player_move += automatic_move
        hrac_skupina.update(player_move, dt)


    # fill the screen with a color to wipe away anything from last frame
    # >>>>>>>> zobrazení <<<<<<<<<
    screen.blit(background_image, (0, 0))


    vsechna_jidla.draw(screen)
    hrac_skupina.draw(screen)

    if ACTUAL_STATE == STATE_PAUSE:
        # Nápis PAUZA
        text_pauza = "PAUZA - mezerník pro spuštění"
        text_picture = font_info.render(text_pauza, True, font_color)
        screen.blit(text_picture, (screen.get_width() / 2, screen.get_height() / 2))


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # >>>>>>>> pauza <<<<<<<<<
    dt = clock.tick(FPS) / 1000 # v sekundách

pygame.quit()