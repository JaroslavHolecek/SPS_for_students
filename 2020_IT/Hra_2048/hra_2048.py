import pygame
pygame.init()

HLAVNI_OKNO_SIRKA = 400
HLAVNI_OKNO_VYSKA = 200

WHITE = pygame.Color("white")
BLUE = pygame.Color(0,0,255,255)
mraky = pygame.image.load('mrak.jpg') #.convert_alpha()
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

smer_kostek = UP

# vytvoření hlavního okna / plátna / Surface
hlavni_platno = pygame.display.set_mode((HLAVNI_OKNO_SIRKA, HLAVNI_OKNO_VYSKA))
pygame.display.set_caption('Hra 2048')

mraky = pygame.transform.scale(mraky, (HLAVNI_OKNO_SIRKA, HLAVNI_OKNO_VYSKA))
hlavni_platno.blit(mraky, (0, 0))


class Kostka(pygame.sprite.Sprite):
    def __init__(self,X,Y):
        super().__init__()

        self.image = pygame.Surface([25, 25])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect[0] = X
        self.rect[1] = Y

    def update(self ):
        if smer_kostek == RIGHT:
            self.rect[0] += 5
            if self.rect[0] + self.rect[2] > HLAVNI_OKNO_SIRKA:
                self.rect[0] = HLAVNI_OKNO_SIRKA - self.rect[2]
        elif smer_kostek == LEFT:
            self.rect[0] -= 5
            if self.rect.x <= 0:
                self.rect.x = 0
        if smer_kostek == DOWN:
            self.rect.y += 5
            if self.rect.y + self.rect.h > HLAVNI_OKNO_VYSKA:
                self.rect.y = HLAVNI_OKNO_VYSKA - self.rect.h
        elif smer_kostek == UP:
            self.rect.y -= 5
            if self.rect.y <= 0:
                self.rect.y = 0


skupina_kostek = pygame.sprite.Group()

for k in range(10):
    skupina_kostek.add(Kostka(k*30, k*30))


#vectorize pojmenovani vlastni udalosti
EVENT_POSUN_KOSTKY = pygame.USEREVENT + 1

hodiny = pygame.time.Clock()
FPS = 60

#udalost se vyvola kazdych 2000 milisekund
pygame.time.set_timer(EVENT_POSUN_KOSTKY, 100)


bezi = True
while bezi: # hlavní smyčka
    for event in pygame.event.get(): # zpracování nových událostí
        if event.type == pygame.QUIT: # událost ukončení
            bezi = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                smer_kostek = RIGHT
            if event.key == pygame.K_a:
                smer_kostek = LEFT
            if event.key == pygame.K_w:
                smer_kostek = UP
            if event.key == pygame.K_s:
                smer_kostek = DOWN
        if event.type == EVENT_POSUN_KOSTKY:
            skupina_kostek.update()

    # okamzite zpracovani klavesnice - bez udalosti
    # klavesy = pygame.key.get_pressed()
    # if klavesy[pygame.K_LEFT]:
    #     pozice_kolecka[0] += 5


    # kam.blit(odkud, dest=pozice_kam, area=velikost)
    hlavni_platno.blit(mraky, dest=(0, 0))

    skupina_kostek.draw(hlavni_platno)


    # pygame.draw.circle(hlavni_platno, BLUE, pozice_kolecka, 20)
    pygame.display.update() # vykreslení změn na monitor
    hodiny.tick(FPS)

pygame.quit()