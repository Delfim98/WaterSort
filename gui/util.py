from tracemalloc import start
from typing import List, Tuple
import pygame
import math
from pygame.rect import Rect
from config.graphic_conf import GraphicConfig

from models.board import Board
from models.bottle import Bottle
from functools import reduce


class GUIUtil(object):

    config: GraphicConfig
    height: int
    width: int
    cellHeight: int
    cellWidth: int

    def __init__(self) -> None:
        super().__init__()
        self.config = GraphicConfig()

    def initScreen(self) -> pygame.Surface:
        pygame.init()
        screen = pygame.display.set_mode(
            [self.config.windowWidth, self.config.windowHeight])
        pygame.display.set_caption(self.config.windowCaption)
        screen.fill(self.config.backgroundColor)
        self.height = screen.get_height()
        self.width = screen.get_width()

        return screen

    def getBottleRect(self, index: int) -> Rect:
        return Rect(
            (((index * (self.config.bottleWidth+self.config.cellBorderSize)) + self.config.cellBorderSize),
             self.config.cellBorderSize), (self.config.bottleWidth, self.config.bottleHeight)
        )

    def getWaterRect(self, index: int, bottleRect: Rect) -> Rect:
        waterHeight = (self.config.bottleHeight -
                       (2*self.config.cellBorderSize))/4
        return Rect(
            (bottleRect.left + self.config.cellBorderSize, bottleRect.top +
             ((3-index) * waterHeight) + self.config.cellBorderSize),
            (self.config.bottleWidth - self.config.cellBorderSize * 2, waterHeight)
        )

    def drawBoard(self, board: Board, screen: pygame.Surface):
        pygame.draw.rect(screen, self.config.backgroundColor,
                         Rect(0, 0, self.width, self.height))
        for bIndex, water in enumerate(board.bottles):
            bottleRect =  self.getBottleRect(bIndex)
            pygame.draw.rect(screen, self.config.cellBorderColor,
                            bottleRect, self.config.cellBorderSize)
            for wIndex, water in enumerate(board.bottles[bIndex].waters):
                pygame.draw.rect(screen, self.config.colors.get(
                    water.color), self.getWaterRect(wIndex,bottleRect))

    def getBottleIndex(self, pos: Tuple[int, int], board: Board) -> int:
        for index,bottle in enumerate(board.bottles):
            startX = ((index * (self.config.bottleWidth+self.config.cellBorderSize)
                       ) + self.config.cellBorderSize)
            endX = startX + \
                (((self.config.bottleWidth+self.config.cellBorderSize)) +
                 self.config.cellBorderSize)
            if(pos[0] > startX and pos[0] < endX):
                return index
        return None
