from functools import reduce
from typing import List
from models.water import Water

class Bottle(object):
    waters: List[Water] = []

    def __init__(self,waters: List[Water]):
        self.waters = waters


    def __str__(self):
        return str(self.waters)


