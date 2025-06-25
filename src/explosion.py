
import pygame
import os
import sys


from config import IMAGE_PATH


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        full_image_path = os.path.join(IMAGE_PATH, 'Explosion.png')
        self.image = pygame.image.load(full_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.timer = 30

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.kill()