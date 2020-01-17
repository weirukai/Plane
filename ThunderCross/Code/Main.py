"""
游戏中的全局常量请定义在Main.py文件中
游戏的开始请从Main开始
绘图线程操作请在Main中定义
"""
import pygame
from code import *
import time
import tkinter
from tkinter import *

from pygame import surface

"""
定义全局常量部分
"""
PLAYER_HP = 200
ENEMY_HP = 50
ScreenWidth = 400
ScreenHeight = 600
# 定义屏幕常量
MODE = pygame.Rect(90, 30, ScreenWidth, ScreenHeight)

# 加载所有用到的图像资源
background = pygame.image.load("../images/background.png")


class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(MODE.size)

    def startGame(self):
        while True:
            # 主线程循环
            pygame.init()
            self.screen.blit(background, (0, 0))  # 贴背景图

            pygame.display.update()
            time.sleep(20000)


if __name__ == '__main__':
    print("游戏开始的敌方")
    game = Game()
    game.startGame()
