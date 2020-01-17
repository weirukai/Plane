"""
飞机类，包括己方和敌方飞机，敌方boss飞机等等等
"""
from Code.ImagesClass import Images


class Plane(Images):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

# 玩家
class playerPlane(Plane):
    def __init__(self):
        super().__init__()
        self.life=PLAYER_HP


# 敌方
class enemyPlane(Plane):
    def __init__(self):
        super().__init__()
        self.life=ENEMY_HP

