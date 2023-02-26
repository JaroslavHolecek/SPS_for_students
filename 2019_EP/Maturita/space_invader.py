import pygame

pygame.init()
vyska = 600
sirka = 1000
background_colour = (234, 212, 252)
black = (0, 0, 0)
screen = pygame.display.set_mode((sirka, vyska))

pygame.display.set_caption('Spaceinvader')

screen.fill(background_colour)



class Hrac(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hrac.jpg")
        self.rect = self.image.get_rect()
        self.rect[0] = sirka//2
        self.rect[1] = vyska-self.rect[3]
        self.rychlost = 10


obrazek_enemy = pygame.image.load("enemy.jpg")
enemy_rect = obrazek_enemy.get_rect()
enemy_pozice = [sirka//2, 0]
rychlost_enemy = 1

obrazek_strela = pygame.Rect(sirka//2, vyska-50, 19, 10)
rychlost_strely = 1

pygame.display.flip()
clock = pygame.time.Clock()
FPS = 60

dt = clock.tick(FPS)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    klavesy = pygame.key.get_pressed()
    if klavesy[pygame.K_a]:

        hrac_pozice[0] = hrac_pozice[0] - rychlost * (dt//10)
    if klavesy[pygame.K_d]:
        hrac_pozice[0] = hrac_pozice[0] + rychlost * (dt//10)
        #výpočty
    enemy_pozice[1] = enemy_pozice[1] + rychlost_enemy * (dt//10)

    #vykreslovani
    screen.blit(obrazek_hrac,dest = hrac_pozice)
    screen.blit(obrazek_enemy, dest=enemy_pozice)
    pygame.draw.rect(screen, black, obrazek_strela)
    pygame.display.flip()
    dt = clock.tick(FPS)
pygame.quit()