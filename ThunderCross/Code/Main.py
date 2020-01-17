"""
游戏中的全局常量请定义在Main.py文件中
游戏的开始请从Main开始
绘图线程操作请在Main中定义
"""
import pygame
from code import *
import time
"""
定义全局常量
"""
PLAYER_HP = 200
ENEMY_HP = 50
# 定义屏幕常量
SCREEN_RECT = pygame.Rect(30, 0, 700, 480)


class Game(object):
    def __init__(self):
        self._screenWidth = 300
        self._screenHeight = 600
        pygame.display.set_mode(SCREEN_RECT.size)

    def startGame(self):
        pygame.init()
        while True:
            pygame.display.update()
            time.sleep(200)


if __name__ == '__main__':
    print("游戏开始的敌方")
    game = Game()
    game.startGame()
