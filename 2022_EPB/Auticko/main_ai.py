import pygame
import sys
import time
import math
import numpy as np
import tensorflow as tf
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

# Mapa
vzdalenosti = mapa_vzdalenost.compute_distance(track)
vzdalenosti_prekazek = mapa_vzdalenost.vzdalenosti_od_okraju_a_prekazek(track)
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
        self.angle = 0

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
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Autonomní jízda")
clock = pygame.time.Clock()

# --- Inicializace autíčka ---
car = Car(*start_pos)
all_sprites = pygame.sprite.Group()
all_sprites.add(car)

# --- Měření času ---
start_time = time.time()

# --- Model ---
model = tf.keras.models.load_model("auticko_model.h5")

# --- Záznam dat ---
train_data = []
train_labels = []

# --- Hlavní smyčka ---
running = True
while running:
    screen.fill(WHITE)

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
    vzdalenost_od_prekazek = vzdalenosti_prekazek[pozice[1]][pozice[0]]

    input_vector = [
        car.speed,
        car.angle / 360.0,
        vzdalenost,
        vzdalenost_od_prekazek['up'],
        vzdalenost_od_prekazek['down'],
        vzdalenost_od_prekazek['left'],
        vzdalenost_od_prekazek['right']
    ]

    input_np = np.array([input_vector])
    prediction = model.predict(input_np, verbose=0)[0]

    if prediction[0] > 0.5: car.accelerate(0.05)
    if prediction[1] > 0.5: car.rotate(-5)
    if prediction[2] > 0.5: car.accelerate(-0.05)
    if prediction[3] > 0.5: car.rotate(5)

    label = (prediction > 0.5).astype(int).tolist()
    train_data.append(input_vector)
    train_labels.append(label)

    all_sprites.draw(screen)
    running = car.update()
    pygame.display.flip()
    clock.tick(FPS)

end_time = time.time()
print(f"Čas jízdy: {end_time - start_time:.2f} s")

# Uložení dat
np.save("train_data.npy", np.array(train_data))
np.save("train_labels.npy", np.array(train_labels))
print("Trénovací data uložena.")

pygame.quit()
