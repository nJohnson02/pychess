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

    #Piece Movement
    def movePawn(dir,dist):
        pass
    def moveRook(dir,dist):
        pass
    def moveKnight(dir,dist):
        pass
    def moveBishop(dir,dist):
        pass
    def moveQueen(dir,dist):
        pass
    def moveKing(dir,dist):
        pass

    """
        Distance could be the number of spaces to move, ither diagonally or straight.
        The distance variable could just be ignored in the case of pieces like the king or knight that can only move a definate number of spaces.
        Directions could be based on unit circle or something.
        Ex:               Or:
             3                 1 = right
          4 ---- 2             2 = up and right
          5 |  | 1             3 = up
          6 ---- 8             4 = up and left
              7                5 = left
                               6 = down and left
                               7 = down
                               8 = down and right
    """