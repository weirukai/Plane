import pygame


Speed=10
PLAYER_HP = 200
ENEMY_HP = 50
ScreenWidth = 400
ScreenHeight = 600
# 定义屏幕常量
MODE = pygame.Rect(90, 30, ScreenWidth, ScreenHeight)

screen = pygame.display.set_mode(MODE.size)

myPlane = None