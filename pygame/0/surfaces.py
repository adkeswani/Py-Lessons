import pygame
from pygame.locals import *

BACKGROUND_COLOUR = (0, 0, 170.4)

pygame.init()
pygame.display.set_mode((0,0))
screen = pygame.display.get_surface()

surf = pygame.Surface((100, 100)).convert()
surf.fill(BACKGROUND_COLOUR)
screen.blit(surf, (0,0))
pygame.display.flip()
    
exited = False
while not exited:
    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
