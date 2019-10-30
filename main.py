import os
import sys
import pygame
from pygame.locals import *

sys.path.insert(0, 'src')
from src import *
from config import *

# Setup
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1200, 720
screen = pygame.display.set_mode((width, height))


class Board:

    def __init__(self, win):

        pass

    def setBoard(self):
        
        pass


while True:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.

    pygame.display.flip()
    fpsClock.tick(fps)

