import pygame
from pygame.locals import *

import loader
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.smoothscale(loader.load_image("ship.png"), (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = pos

    #Input
    def update(self):
        k = pygame.key.get_pressed()

        if k[K_UP]:
            self.rect.y = self.rect.y - 1

        if k[K_m]:
            pos = pygame.mouse.get_pos()
            a = -math.atan2(pos[1] - self.rect.y, pos[0] - self.rect.x)
            print "Mouse pos relative to ship is:", a
         
