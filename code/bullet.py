# bullet.py

import pygame
from config import IMAGE_PATH, BULLET_SPEED


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + 'bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += BULLET_SPEED
        if self.rect.left > 800:
            self.kill()
