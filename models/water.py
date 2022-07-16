class Water(object):
    color: str = ''

    def __init__(self,color: str):
        self.color = color

    def __str__(self):
        return str(self.color)