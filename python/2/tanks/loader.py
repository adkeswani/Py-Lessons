import os, pygame, sys
from pygame.locals import *

#A bit of code you can copy and paste to load images for you
def load_image(name, colorkey=None):
    #Get the path of the image
    #This assumes the image is in an 'images' directory
    fullname = os.path.join(sys.path[0], 'images', name)

    #Who's seen try-catch blocks?
    try:
        #Get python to load the image
        image = pygame.image.load(fullname)
    except pygame.error, message:
        #Crash and burn.
        print 'Cannot load image:', name
        raise SystemExit, message

    #Allows you to use alpha channel in images
    #Remember the Red, Green, Blue?
    #Alpha is a 4th number that allows you to make stuff transparent, you add it when you create the image
    #This basically takes into account that alpha value, only works with formats that support transparency
    image = image.convert_alpha()

    #The below allows us to add more transparent parts to an image
    #colorkey is a colour that we want to remove and replace with transparency
    #So if we wanted an empty circle that we could see through, you could could the inside with 'colorkey'
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)

    #Sends back an image and the size of the image in a rect
    return image

def load_sound(name):
    #Object type to return if mixer not enabled
    class NoneSound:
        def play(self): pass

    if not pygame.mixer:
        return NoneSound()

    fullname = os.path.join(sys.path[0], 'sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname 
        raise SystemExit, message

    return sound

def load_font(name, size):
    fullname = os.path.join(sys.path[0], 'fonts', name)
    try:
        font = pygame.font.Font(fullname, size)
    except pygame.error, message:
        print 'Cannot load font:', fullname
        raise SystemExit, message

    return font
    
