from idlelib.configdialog import font_sample_text

import pygame
import sys
import time
import math
import mapa_vzdalenost

pygame.init()

# --- Konfigurace ---
track = mapa_vzdalenost.nacti_mapu("mapy/mapa2.txt")

CELL_SIZE = 50
GRID_WIDTH = len(track[0])
GRID_HEIGHT = len(track)
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

font = pygame.font.SysFont(None, 40)

# Mapa trati (0=start, 1=dráha, 2=překážka, 9=cíl)

vzdalenosti = mapa_vzdalenost.compute_distance(track)

start_pos = mapa_vzdalenost.najdi_start(track)

# --- Třída pro autíčko ---
class Car(pygame.sprite.Sprite):
    def __init__(self, y, x):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x * CELL_SIZE
        self.y = y * CELL_SIZE
        self.rect.topleft = (int(self.x), int(self.y))
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
                if cell == mapa_vzdalenost.MapElement.PREKAZKA.value:
                    print("Náraz! Hra končí.")
                    return False
                elif cell == mapa_vzdalenost.MapElement.CIL.value:
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
            if track[y][x] == mapa_vzdalenost.MapElement.PREKAZKA.value:
                pygame.draw.rect(screen, BLACK, rect)
            elif track[y][x] == mapa_vzdalenost.MapElement.CESTA.value:
                pygame.draw.rect(screen, BLUE, rect)
            elif track[y][x] == mapa_vzdalenost.MapElement.CIL.value:
                pygame.draw.rect(screen, GREEN, rect)

    pozice = (car.rect.center[0] // CELL_SIZE, car.rect.center[1] // CELL_SIZE)
    vzdalenost = vzdalenosti[pozice[1]][pozice[0]]
    text_vzdalenost = font.render(f"{vzdalenost}", True, WHITE)
    screen.blit(text_vzdalenost, (0,0))

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

mapa_vzdalenost.show_2d(vzdalenosti)
