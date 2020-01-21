from pyCode.GlobalVar import screen, PLAYER_HP, ENEMY_HP
from pyCode.ImagesClass import Images
import pygame


class Plane(Images):
    def __init__(self, x: int, y: int, image_path: str):
        super().__init__(image_path)
        self.rect.x = x
        self.rect.y = y
        self.life = None

    def drawPlane(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.display.update()


# 玩家
class playerPlane(Plane):
    def __init__(self, x: int, y: int, images_path: str):
        super().__init__(x, y, images_path)
        self.life = PLAYER_HP


# 敌方
class enemyPlane(Plane):
    def __init__(self, x: int, y: int, images_path: str):
        super().__init__(x, y, images_path)
        self.life = ENEMY_HP
