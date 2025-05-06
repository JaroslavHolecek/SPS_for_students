import pygame
import sys
import time
import math

# --- Konfigurace ---
CELL_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 10
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 60

# Barvy
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

# Mapa trati (0=start, 1=dráha, 2=překážka, 9=cíl)
track = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 9, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

# Najdi startovní pozici
for y in range(len(track)):
    for x in range(len(track[y])):
        if track[y][x] == 0:
            start_pos = (x, y)

# --- Třída pro autíčko ---
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x * CELL_SIZE
        self.y = y * CELL_SIZE
        self.speed = 0.0
        self.angle = 0  # počáteční směr dolů (ve stupních)

    def update(self):
        if self.speed != 0:
            rad = math.radians(self.angle)
            dx = math.cos(rad) * self.speed
            dy = math.sin(rad) * self.speed
            self.x += dx
            self.y += dy
            self.rect.topleft = (int(self.x), int(self.y))

            grid_x = int(self.x / CELL_SIZE)
            grid_y = int(self.y / CELL_SIZE)

            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                cell = track[grid_y][grid_x]
                if cell == 2:
                    print("Náraz! Hra končí.")
                    return False
                elif cell == 9:
                    print("Cíl dosažen!")
                    return False
            else:
                print("Mimo trať! Hra končí.")
                return False
        return True

    def accelerate(self, value):
        self.speed = max(0.0, min(5.0, self.speed + value))

    def rotate(self, angle_delta):
        self.angle = (self.angle + angle_delta) % 360

# --- Inicializace PyGame ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jednoduchá závodní hra")
clock = pygame.time.Clock()

# --- Inicializace autíčka ---
car = Car(*start_pos)
all_sprites = pygame.sprite.Group()
all_sprites.add(car)

# --- Měření času ---
start_time = time.time()

# --- Hlavní smyčka ---
running = True
while running:
    screen.fill(WHITE)

    # --- Vykreslení mapy ---
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if track[y][x] == 2:
                pygame.draw.rect(screen, BLACK, rect)
            elif track[y][x] == 1:
                pygame.draw.rect(screen, GRAY, rect)
            elif track[y][x] == 0:
                pygame.draw.rect(screen, GREEN, rect)
            elif track[y][x] == 9:
                pygame.draw.rect(screen, BLUE, rect)

    all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        car.accelerate(0.05)
    if keys[pygame.K_s]:
        car.accelerate(-0.05)
    if keys[pygame.K_a]:
        car.rotate(-5)  # otoč doleva
    if keys[pygame.K_d]:
        car.rotate(5)   # otoč doprava

    running = car.update()
    pygame.display.flip()
    clock.tick(FPS)

# --- Výpis času ---
end_time = time.time()
print(f"Čas jízdy: {end_time - start_time:.2f} s")

pygame.quit()
