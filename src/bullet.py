
import pygame
import os
import sys


from config import IMAGE_PATH, BULLET_SPEED


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        full_image_path = os.path.join(IMAGE_PATH, 'Player1Shot.png')
        self.image = pygame.image.load(full_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += BULLET_SPEED

        if self.rect.left > 800:
            self.kill()