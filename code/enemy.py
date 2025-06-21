# enemy.py

import pygame
import random
from config import IMAGE_PATH, ENEMY_SPEED


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + 'enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.randint(50, 300)
        self.rect.y = random.randint(50, 550)
        self.speed = ENEMY_SPEED + random.random() * 2

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
