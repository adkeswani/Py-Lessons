import pygame
import loader
import projectile
from pygame.locals import *

TANK_WIDTH = 50
TANK_HEIGHT = 40

class Tank(pygame.sprite.Sprite):
    def __init__(self, isPlayer, xPos):
        pygame.sprite.Sprite.__init__(self)

        if isPlayer:
            self.image = loader.load_image("greenTank.png")
            self.image = pygame.transform.smoothscale(self.image, (TANK_WIDTH, TANK_HEIGHT))
        else:
            self.image = loader.load_image("redTank.png")
            self.image = pygame.transform.smoothscale(self.image, (TANK_WIDTH, TANK_HEIGHT))
            
        screen = pygame.display.get_surface()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (xPos, screen.get_height())
        
    def update(self):
        print "Tank update must be implemented by a subclass"

class PlayerTank(Tank):
    def __init__(self, projectiles):
        super(PlayerTank, self).__init__(True, 50)
        self.projectiles = projectiles

    def update(self):
        if not self.projectiles:
            self.projectiles.add(projectile.Projectile(self.rect.centerx, self.rect.centery))

class EnemyTank(Tank):
    def __init__(self):
        screen = pygame.display.get_surface()
        super(EnemyTank, self).__init__(False, screen.get_width() - 50)

    def update(self):
        pass
