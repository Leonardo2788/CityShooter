import pygame
from config import IMAGE_PATH, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + 'Player1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.speed = PLAYER_SPEED

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def shoot(self):
        return Bullet(self.rect.centerx + 40, self.rect.centery)

