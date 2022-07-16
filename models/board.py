
from typing import List
from models.bottle import Bottle


class Board(object):
    bottles: List[Bottle] = []
    
    
    def isSorted(self) -> bool:
        result = True
        for bottle in self.bottles:
            if(len(bottle.waters) > 0):
                color = bottle.waters[0].color
                for water in bottle.waters:
                    if(color != water.color):
                        result = False
        return result


    def __init__(self,bottles: List[Bottle]):
        self.bottles = bottles


    def __str__(self):
        return str(self.bottles)
