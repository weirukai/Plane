from pyCode.GlobalVar import screen, PLAYER_HP, ENEMY_HP, Speed ,enemyPlaneGroup
from pyCode.ImagesClass import Images
import pygame
from pygame.locals import *



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

    def move(self, key: pygame.key):
        if key == K_RIGHT:
            self.rect.x += Speed
        elif key == K_LEFT:
            self.rect.x -= Speed
        elif key == K_DOWN:
            self.rect.y += Speed
        elif key == K_UP:
            self.rect.y -= Speed


# 敌方
class enemyPlane(Plane):
    def __init__(self, x: int, y: int, images_path: str):
        super().__init__(x, y, images_path)
        self.life = ENEMY_HP
        enemyPlaneGroup.add(self)

    @staticmethod
    def drawEnemyPlane():
        for enemyMember in enemyPlaneGroup:
            enemyMember.drawPlane()