import pygame
import random
from config import IMAGE_PATH, ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self, shooting=False):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + 'Player2.png')
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.speed = ENEMY_SPEED + random.random() * 2
        self.shooting = shooting

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

