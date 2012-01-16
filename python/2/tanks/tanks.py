import pygame
from pygame.locals import *
import tank

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOUR = (0,0,0)

class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.projectileSprites = pygame.sprite.RenderUpdates()
        self.tankSprites = pygame.sprite.RenderUpdates()

        self.tankSprites.add(tank.EnemyTank())
        self.tankSprites.add(tank.PlayerTank(self.projectileSprites))

    def start(self):
        self.doGameLoop()

    def doGameLoop(self):
        exited = 0;
        while (not exited):
            self.clock.tick(60)

            self.displayAll()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exited = 1
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    exited = 1

    def displayAll(self):
        self.projectileSprites.clear(screen, background)
        self.tankSprites.clear(screen, background)

        self.projectileSprites.update()
        self.tankSprites.update()

        rects = self.projectileSprites.draw(screen)
        rects.extend(self.tankSprites.draw(screen))

        pygame.display.update(rects)

pygame.init()
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size()).convert()
background.fill(BACKGROUND_COLOUR)
screen.blit(background, (0,0))
pygame.display.flip()
pygame.key.set_repeat(10)
Game().start();


