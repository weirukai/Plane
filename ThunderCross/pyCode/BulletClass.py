"""
子弹类，子弹的属性以及子弹的对应的方法
"""
from pyCode.ImagesClass import Images


class Bullet(Images):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
