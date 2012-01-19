import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((0,0), FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exited = 1
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = 1
