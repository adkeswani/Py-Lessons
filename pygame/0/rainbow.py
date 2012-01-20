import pygame
import math
from pygame.locals import *

BACKGROUND_COLOUR = (0, 0, 0)

pygame.init()
pygame.display.set_mode((0,0))
screen = pygame.display.get_surface()

background = pygame.Surface((screen.get_height(), screen.get_width())).convert()
background.fill(BACKGROUND_COLOUR)
screen.blit(background, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()

exited = False
while not exited:
    clock.tick(30)

    screen.blit(background, (0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True

#frequency = 0.3
#for loop, 32 times
#red = math.sin(frequency * i + 0) * 127 + 128;
#green = math.sin(frequency * i + 2 * math.pi / 3) * 127 + 128;
#blue = math.sin(frequency * i + 4 * math.pi / 3) * 127 + 128;
