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

        self.direction = True

    def update(self):
        if self.direction:
            self.rect.y = self.rect.y - 20
        else:
            self.rect.y = self.rect.y + 20
         
        if self.rect.y < 0:
            self.direction = False
        
        if self.rect.y > pygame.display.get_surface().get_height():
            self.direction = True 
