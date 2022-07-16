
from models.board import Board


def moveWater(origin: int, target: int, board: Board) -> bool:
    result: bool = False
    while(canMove(origin,target,board)):
         board.bottles[target].waters.append(
                board.bottles[origin].waters.pop())
         result = True
         print('moved origin->target: '+str(origin)+'->'+str(target))
    return result


def canMove(origin: int, target: int, board: Board) -> bool:
    result = False
    if(len(board.bottles) < origin or len(board.bottles) < target):
        print('Can\'t move: invalid origin->target: ' + str(origin) + '->' + str(target))
    elif(len(board.bottles[origin].waters) == 0):
        print('Can\'t move: origin empty')
    elif(len(board.bottles[target].waters) == 0 or
         (len(board.bottles[target].waters) < 4 and 
         board.bottles[target].waters[len(board.bottles[target].waters)-1].color ==
         board.bottles[origin].waters[len(board.bottles[origin].waters)-1].color)):
        result = True
    return result