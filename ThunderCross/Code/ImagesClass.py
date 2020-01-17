import pygame
from pygame import image


class Images(pygame.sprite.Sprite):
    def __init__(self, image_path: str):
        super().__init__()  # 子类的构造方法的第一行要调用父类的构造方法
        self.image = pygame.image.load(image_path)  # 添加一个属性图片（image是pygame的一个类）
        self.rect = self.image.get_rect()  # 获得这个图片的rect属性（rect是pygame提供的一个属性）

    pass
