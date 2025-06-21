# player.py

import pygame
from config import IMAGE_PATH, PLAYER_SPEED, BULLET_SPEED
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + 'player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.speed = PLAYER_SPEED

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_s] and self.rect.bottom < 600:
            self.rect.y += self.speed
        if keys_pressed[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_d] and self.rect.right < 800:
            self.rect.x += self.speed

    def shoot(self):
        return Bullet(self.rect.centerx + 40, self.rect.centery)
