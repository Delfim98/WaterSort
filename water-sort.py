# Simple pygame program


# Import and initialize the pygame library

import random
from typing import List
import pygame
from action.movement import moveWater
from gui.util import GUIUtil
from models.board import Board
from models.water import Water
from models.bottle import Bottle

# Set up the drawing window
guiUtil = GUIUtil()
screen = guiUtil.initScreen()


# Run until the user asks to quit

running = True

bottleNum = len(guiUtil.config.colors)
bottles: List[Bottle] = []
for i in range(bottleNum):
    bottles.append(Bottle([]))
for color in guiUtil.config.colors:
    for i in range(4):
        randomIndex = None
        while(True):
            randomIndex = random.randint(0, len(bottles)-1)
            if(len(bottles[randomIndex].waters) < 4):
                bottles[randomIndex].waters.append(Water(color))
                break
        
for i in range(2):
    bottles.append(Bottle([]))

board = Board(bottles)
selectedBottle: int = None
guiUtil.drawBoard(board,screen)
pygame.display.flip()
pygame.time.set_timer(pygame.event.Event(pygame.USEREVENT),300)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            index = guiUtil.getBottleIndex(pos,board)
            if(selectedBottle != None):
                if(index == None):
                    selectedBottle = None
                else:
                    if(moveWater(selectedBottle,index,board)):
                        guiUtil.drawBoard(board,screen)
                        pygame.display.flip()
                if(board.isSorted()):
                    print('win')
                selectedBottle = None
            else:
                selectedBottle = index

# Done! Time to quit.

pygame.quit()