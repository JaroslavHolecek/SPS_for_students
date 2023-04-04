import pygame

x = [10, 15, 14, 1, 2, 6, 48]

def bubble(pole):
    print("Jsem uvnitř bubble")
    for opakovani in range(0, len(x)-1):
        print("Jsem uvnitř opakování ", opakovani)
        for i in range(0, len(x)-1-opakovani):
            print("Jsem uvnitř i ", i)
            pozice1 = i
            pozice2 = i+1
            if pole[pozice2] > pole[pozice1]:
                pole[pozice1], pole[pozice2] = pole[pozice2], pole[pozice1]
            print("Končím i")
        print("Končím opakovaní")

# print(x)
# bubble(x)
# print(x)
jednotka = 10

pygame.init()
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

background_colour = (255,255,255)
RED = pygame.Color("red")

(width, height) = (1000, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bubble')
screen.fill(background_colour)

pocatek_x = 50
pocatek_y = 50
sirka_obdelniku = 50
mezera = 2

i = 0
running = True
hodiny = pygame.time.Clock()
while running:
    # Zpracování vstupu
    for event in pygame.event.get(): # fronta událostí
        if event.type == pygame.QUIT:
          running = False

    #vykreslení
    screen.fill(background_colour) # vymazání předchozího framu

    souradnice_x = pocatek_x
    for obdelnik in range(0, len(x)):
        pygame.draw.rect(screen, RED, pygame.Rect(souradnice_x, pocatek_y, sirka_obdelniku, x[obdelnik]*jednotka), 0 )
        souradnice_x += sirka_obdelniku + mezera

    pozice1 = i
    pozice2 = i + 1
    if x[pozice2] > x[pozice1]:
        x[pozice1], x[pozice2] = x[pozice2], x[pozice1]

    if i < len(x)-2:
        i += 1
    else:
        i = 0

    pygame.display.flip()
    hodiny.tick(1)

pygame.quit()
