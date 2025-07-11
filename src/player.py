
import pygame
import os



from config import IMAGE_PATH, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_HEALTH

from .bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        full_image_path = os.path.join(IMAGE_PATH, 'Player1.png')
        self.image = pygame.image.load(full_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.speed = PLAYER_SPEED
        self.health = PLAYER_HEALTH

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def shoot(self):
        return Bullet(self.rect.centerx + 40, self.rect.centery)