import pygame
from pygame.locals import *

BACKGROUND_COLOUR = (0, 0, 170)

pygame.init()
pygame.display.set_mode((0,0), FULLSCREEN)
screen = pygame.display.get_surface()

background = pygame.Surface((100, 100)).convert()
background.fill(BACKGROUND_COLOUR)
screen.blit(background, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()
    
exited = False
while not exited:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
