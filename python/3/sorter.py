import sys
import pygame
import math
import random
from pygame.locals import *

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 600
BACKGROUND_COLOUR = (0,0,0)
INVADER_WIDTH = 48
INVADER_HEIGHT = 32
INVADER_GAP = 20

class Sorter(object):
    def __init__(self, l):
        self.clock = pygame.time.Clock()
        self.l = l
        
        #Sorting
        self.numSorted = 0
        self.curr = 0

    def start(self):
        exited = 0;
        while (not exited):
            self.clock.tick(60)

            self.nextStep()
            self.display()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exited = 1
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    exited = 1

    def nextStep(self):
        #Stop once all sorted
        if self.numSorted < len(self.l):
            #Swap if greater
            if self.l[self.curr] > self.l[self.curr + 1]:
                temp = self.l[self.curr + 1]
                self.l[self.curr + 1] = self.l[self.curr]
                self.l[self.curr] = temp
    
            self.curr = self.curr + 1

            #If it's reached the sorted section, reset to start of list
            if self.curr == len(self.l) - self.numSorted - 1:
                self.numSorted = self.numSorted + 1
                self.curr = 0
    
    def display(self):
        screen.blit(background, (0,0))
        
        rectSurf = pygame.Surface((10, 600)).convert_alpha()

        for i in range(0, len(self.l)):
            rectSurf.fill((0, 0, 0))
            rectSurf.fill((0, 0, 255, self.l[i] * 2 + 20), Rect(0, 600 - self.l[i] * 5, 10, self.l[i] * 5))
            screen.blit(rectSurf, (i * 10, 0))
            
        pygame.display.flip()

pygame.init()
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size()).convert()
background.fill(BACKGROUND_COLOUR)
screen.blit(background, (0,0))
pygame.display.flip()
pygame.key.set_repeat(10)

l = range(1,100)
random.shuffle(l)
Sorter(l).start();


