import pygame
from config import IMAGE_PATH


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + 'Enemy1Shot.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.timer = 30  # frames da explosão (~0,5 segundos)

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
