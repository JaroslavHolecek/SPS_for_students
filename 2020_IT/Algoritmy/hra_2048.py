import pygame
pygame.init()

HLAVNI_OKNO_SIRKA = 400
HLAVNI_OKNO_VYSKA = 200

WHITE = pygame.Color("white")
BLUE = pygame.Color(0,0,255,255)
mraky = pygame.image.load('mrak.jpg') #.convert_alpha()

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
        self.rect[0] += 5
        if self.rect[0] + self.rect[2] > HLAVNI_OKNO_SIRKA:
            self.rect[0] = HLAVNI_OKNO_SIRKA - self.rect[2]

skupina_kostek = pygame.sprite.Group()

for k in range(10):
    skupina_kostek.add(Kostka(k*30, k*30))


#vectorize pojmenovani vlastni udalosti
EVENT_POSUN_KOSTKY = pygame.USEREVENT + 1

hodiny = pygame.time.Clock()
FPS = 60

#udalost se vyvola kazdych 2000 milisekund
pygame.time.set_timer(EVENT_POSUN_KOSTKY, 1000)



bezi = True
while bezi: # hlavní smyčka
    for event in pygame.event.get(): # zpracování nových událostí
        if event.type == pygame.QUIT: # událost ukončení
            bezi = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                # vyvolani udalosti pomoci prikazu
                pygame.event.post(pygame.event.Event(EVENT_POSUN_KOSTKY))

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