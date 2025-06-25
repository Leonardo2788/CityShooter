
import pygame
import random
import os
import sys


from config import IMAGE_PATH, ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self, shooting=False):
        super().__init__()

        full_image_path = os.path.join(IMAGE_PATH, 'Player2.png')
        self.image = pygame.image.load(full_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.speed = ENEMY_SPEED + random.random() * 2
        self.shooting = shooting

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()