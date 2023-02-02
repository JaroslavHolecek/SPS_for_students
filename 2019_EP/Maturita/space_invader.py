import pygame

pygame.init()
vyska = 600
sirka = 1000
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((sirka, vyska))

pygame.display.set_caption('Spaceinvader')

screen.fill(background_colour)
obrazek_hrac = pygame.image.load("hrac.jpg")
hrac_rect=obrazek_hrac.get_rect()
hrac_pozice = [sirka//2, vyska-hrac_rect[3]]
rychlost = 10

obrazek_enemy = pygame.image.load("enemy.jpg")
enemy_rect = obrazek_enemy.get_rect()
enemy_pozice = [sirka//2, 0]
rychlost_enemy = 10

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    klavesy = pygame.key.get_pressed()
    if klavesy[pygame.K_a]:
        hrac_pozice[0] = hrac_pozice[0] - rychlost
    if klavesy[pygame.K_d]:
        hrac_pozice[0] = hrac_pozice[0] + rychlost
    
    screen.blit(obrazek_hrac,dest = hrac_pozice)
    screen.blit(obrazek_enemy, dest=enemy_pozice)
    pygame.display.flip()
pygame.quit()