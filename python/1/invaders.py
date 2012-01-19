import sys
import pygame
import loader
import math
from pygame.locals import *

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOUR = (0,0,0)
INVADER_WIDTH = 48
INVADER_HEIGHT = 32
INVADER_GAP = 20

class Invader(pygame.sprite.Sprite):
    #TODO Exercise 1c:
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = loader.load_image("invader2.png")
        self.image = pygame.transform.smoothscale(self.image, (INVADER_WIDTH, INVADER_HEIGHT))
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
        self.direction = True
        
    #TODO Exercise 1c:
    def update(self):
        if self.rect.centerx > SCREEN_WIDTH:
            self.direction = False
        elif self.rect.centerx < 0:
            self.direction = True

        if self.direction:
            self.rect.centerx = self.rect.centerx + 5
        else:
            self.rect.centerx = self.rect.centerx - 5

class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.invaderSprites = pygame.sprite.RenderUpdates()
        self.createInvaders()

    #TODO Exercise 1c:
    def createInvaders(self):
        for i in range(0,10):
            inv = Invader((INVADER_WIDTH + INVADER_GAP) * i, SCREEN_HEIGHT / 2)
            self.invaderSprites.add(inv)

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
        self.invaderSprites.clear(screen, background)
        self.invaderSprites.update()
        rects = self.invaderSprites.draw(screen)
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


