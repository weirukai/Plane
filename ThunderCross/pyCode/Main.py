from threading import Thread
import pygame
import time
from pyCode.PlaneClass import enemyPlane
from pygame.constants import QUIT, KEYDOWN, MOUSEBUTTONDOWN

from pyCode import PlaneClass
from pyCode import GlobalVar
from pyCode.GlobalVar import screen, myPlane

"""
定义全局常量部分
"""

background = pygame.image.load("../images/background.png")
myPlane = PlaneClass.playerPlane(20, 20, "../images/me1.png")


class Game(object):

    def __init__(self):
        pass
        # self.myPlane:PlaneClass.playerPlane=None

    def eventAddress(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            else:
                if event.type == KEYDOWN:
                    myPlane.move(event.key)
                if event.type == MOUSEBUTTONDOWN:
                    # 预留给鼠标处理的
                    pass

    def startGame(self):

        while True:
            # 主线程循环
            pygame.init()
            screen.blit(background, (0, 0))  # 贴背景图
            self.eventAddress()
            pygame.display.update()

    # 生成敌方飞机
    def createEnemyPlane(self):
        enemyPlane(30,10,"../images/enemy2.png")





class Draw(Thread):
    def run(self) -> None:
        while True:
            # 绘制己方飞机
            myPlane.drawPlane()
            # 绘制敌方飞机
            enemyPlane.drawEnemyPlane()
            time.sleep(0.001)


if __name__ == '__main__':
    print("游戏开始的地方")
    game = Game()
    # game.createEnemyPlane()
    enemyPlane(30, 10, "../images/enemy2.png")
    enemyPlane(150, 10, "../images/enemy2.png")
    try:
        Draw().start()
    except InterruptedError:
        print("线程错误")

    game.startGame()
