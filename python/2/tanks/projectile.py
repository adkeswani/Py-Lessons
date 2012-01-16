import pygame
import loader
from pygame.locals import *

PROJECTILE_WIDTH = 10
PROJECTILE_HEIGHT = 10

class Projectile(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)

        self.image = loader.load_image("projectile.png")
        self.image = pygame.transform.smoothscale(self.image, (PROJECTILE_WIDTH, PROJECTILE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = xPos
        self.rect.centery = yPos

        self.xVel = 1.0
        self.yVel = -2.0

    def update(self):
        self.rect.centerx = self.rect.centerx + self.xVel
        self.rect.centery = self.rect.centery + self.yVel
