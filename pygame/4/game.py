#Initialising pygame
import pygame
from pygame.locals import *
import loader
import ship

pygame.init()
pygame.display.set_mode((0,0))

screen = pygame.display.get_surface()

background = pygame.transform.smoothscale(loader.load_image("background.png"), (screen.get_width(), screen.get_height()))
screen.blit(background, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()

#Creating a sprite group
shipSprites = pygame.sprite.RenderUpdates()
for i in range(0,10):
    shipSprites.add(ship.Ship((screen.get_width() / 10 * i, screen.get_height() / 2)))

exited = False
while not exited:
    clock.tick(30)

    #Displaying a sprite group
    shipSprites.clear(screen, background)
    shipSprites.update()
    rects = shipSprites.draw(screen)

    #rects.extend(anotherSprites.draw(screen))
    
    pygame.display.update(rects)

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
