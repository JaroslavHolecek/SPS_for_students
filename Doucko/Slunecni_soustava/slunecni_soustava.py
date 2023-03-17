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
sirka = int(input("Zadej sirku okna"))
vyska = int(input("Zadej vysku okna"))
SCREEN_SIZE = (sirka, vyska)

pozice_slunce = [SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2]
polomer_slunce = 20

class Planeta(pygame.sprite.Sprite):
    def __init__(self, polomer, vzdalenost_od_slunce, rychlost_obehu): # initialization - vytvoření
        pygame.sprite.Sprite.__init__(self) #super.__init__(self)
        self.polomer = polomer
        self.image = pygame.Surface([2*polomer, 2*polomer])
        self.image.fill(background_colour)
        pygame.draw.circle(self.image, BLUE, [polomer, polomer], polomer)

        # rectangle -> [levy_horni_x, levy_horni_y, sirka, vyska]
        self.rect = self.image.get_rect()

        self.vzdalenost_od_slunce = vzdalenost_od_slunce
        self.rychlost_obehu = rychlost_obehu

    def update(self, ubehnuty_cas):
        self.rect.x = -self.polomer + int(
            pozice_slunce[0] + self.vzdalenost_od_slunce * math.sin(self.rychlost_obehu * ubehnuty_cas))  # x
        self.rect.y = -self.rect.w//2 + int(
            pozice_slunce[1] + self.vzdalenost_od_slunce * math.cos(self.rychlost_obehu * ubehnuty_cas))  # y


vsechny_planety = pygame.sprite.Group()
while True:
    volba = input("Načíst planety ze souboru - s\nPřidat další planetu - p\nKonec zadávání - k")
    if volba == "p":
        p = int(input("Zadej polomer: "))
        v = int(input("Zadej vzdalenost: "))
        r = float(input("Zadej rychlost: "))
        vsechny_planety.add(Planeta(polomer=p, vzdalenost_od_slunce=v, rychlost_obehu=r))
    elif volba == "s":
        with open("planety.txt") as soubor:
            for radek in soubor:
                rozdelene = radek.split(" ") # ["20", "100", "0.003"]
                p = int(rozdelene[0])
                v = int(rozdelene[1])
                r = float(rozdelene[2])
                vsechny_planety.add(Planeta(polomer=p, vzdalenost_od_slunce=v, rychlost_obehu=r))
    elif volba == "k":
        break
# vsechny_planety.add(Planeta(polomer=20, vzdalenost_od_slunce=100, rychlost_obehu=0.001))
# vsechny_planety.add(Planeta(10, 50, 0.002))
# for i in range(1,10):
#     vsechny_planety.add(Planeta(5, 100, i*0.001))

screen = pygame.display.set_mode(SCREEN_SIZE)
# Set the caption of the screen
pygame.display.set_caption('Sluneční soustava')
# Fill the background colour to the screen
screen.fill(background_colour)

hodiny = pygame.time.Clock()
FPS = 100

POZASTAVENA = 0
BEZI = 1
stav = BEZI

start_time = pygame.time.get_ticks()
running = True
# game loop
while running:
    # ZPRACOVANI VSTUPU
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if stav == BEZI:
                    stav = POZASTAVENA
                elif stav == POZASTAVENA:
                    stav = BEZI

    # VYPOCTY
    if stav == BEZI:
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