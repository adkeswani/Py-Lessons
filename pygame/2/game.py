#Initialising pygame
import pygame
from pygame.locals import *
import loader
import ship

pygame.init()
pygame.display.set_mode((0,0))

screen = pygame.display.get_surface()

background = pygame.Surface((screen.get_width(), screen.get_height())).convert()
background.fill((0,0,0))
screen.blit(background, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()

#Creating sprites
player = ship.Ship((screen.get_width() / 2, screen.get_height() / 2))

exited = False
while not exited:
    clock.tick(30)

    screen.blit(background, (0,0))

    #Displaying sprites
    screen.blit(player.image, player.rect.center)
    pygame.display.flip()

    #Experiments
    player.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
