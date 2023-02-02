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
pygame.draw.circle(hlavni_platno, BLUE, [25,40], 20)

bezi = True
while bezi: # hlavní smyčka
    for event in pygame.event.get(): # zpracování nových událostí
        if event.type == pygame.QUIT: # událost ukončení
            bezi = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hlavni_platno.fill(BLUE)
        
    pygame.display.update() # vykreslení změn na monitor

pygame.quit()