"""
飞机类，包括己方和敌方飞机，敌方boss飞机等等等
"""
from Code.ImagesClass import Images


class Plane(Images):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
