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

#Collisions demo
aSprites = pygame.sprite.RenderUpdates()
bSprites = pygame.sprite.RenderUpdates()

aSprites.add(ship.Ship((screen.get_width() / 2, screen.get_height() - 10)))
aSprites.add(ship.Ship((screen.get_width() / 4, screen.get_height() - 10)))
bSprites.add(ship.Ship((screen.get_width() / 2, 0)))
bSprites.add(ship.Ship((screen.get_width() / 4, 0)))

exited = False
while not exited:
    clock.tick(30)

    aSprites.clear(screen, background)
    aSprites.update()
    rects = aSprites.draw(screen)

    bSprites.clear(screen, background)
    bSprites.update()
    rects.extend(bSprites.draw(screen))

    pygame.display.update(rects)

    #Checking for collisions:
    collisions = pygame.sprite.groupcollide(aSprites, bSprites, True, True)
    if collisions:
        print "The sprites from aSprites that were in the collision:", collisions.keys()
        print "The sprites from bSprites that were in the collision:", collisions.values()
        for k in collisions.keys():
            print k, "from aSprites collided with", collisions[k], "from bSprites"

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
