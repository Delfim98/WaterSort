import configparser


class GraphicConfig(object):
    windowWidth: int = 400
    windowHeight: int = 400
    bottleWidth = 40
    bottleHeight = 80
    windowCaption:str = ""
    backgroundColor = (255,255,255)
    cellBorderSize:int = 4
    cellBorderColor = (255,255,255)
    colors = dict({"white": (255,255,255), "black": (0,0,0),
    "red": (255,0,0),
    "lime": (0,255,0),
    "blue": (0,0,255),
    "yellow": (255,255,0),
    "mangenta": (255,0,255),
    "silver": (192,192,192),
    "purple": (128,0,128)}) 

    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read('resources/config.cfg')
        graphicConfig = config['graphic']
        self.windowWidth = int(graphicConfig['windowWidth'])
        self.windowHeight = int(graphicConfig['windowHeight'])
        self.windowCaption = graphicConfig['windowCaption']
        self.cellBorderSize = int(graphicConfig['cellBorderSize'])
        self.cellBorderColor = [int(c) for c in graphicConfig['cellBorderColor'].split(',')]
        self.backgroundColor = [int(c) for c in graphicConfig['backgroundColor'].split(',')]
        self.snakeColor = [int(c) for c in graphicConfig['snakeColor'].split(',')]
        self.fruitColor = [int(c) for c in graphicConfig['fruitColor'].split(',')]