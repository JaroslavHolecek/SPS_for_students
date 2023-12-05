import pygame
import pygame.locals as konstanty
pygame.init()

FPS = 50
hodiny = pygame.time.Clock()

sirka_okna = 300
vyska_okna = 300

hlavni_okno = pygame.display.set_mode( (sirka_okna, vyska_okna) )
pygame.display.set_caption('Had')

CERVENA = (255,0,0)
BLACK = (0,0,0)

hra_bezi = True
while hra_bezi:
    # Zpracování vstupu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hra_bezi = False
        elif event.type == konstanty.KEYDOWN:
            if event.key == konstanty.K_a:
                print("Stisknuto A")

    # Výpočty ve hře

    # Zobrazení změn
    hlavni_okno.fill(BLACK)
    pygame.draw.circle(hlavni_okno, CERVENA, [50, 50], 30, 5)

    # Aktualizace obrazovky
    pygame.display.flip()
    # Počkat pro požadované fps
    hodiny.tick(FPS)
pygame.quit()
