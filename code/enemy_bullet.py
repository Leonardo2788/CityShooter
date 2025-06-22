import pygame
from config import IMAGE_PATH, ENEMY_BULLET_SPEED


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH + 'EnemyShot.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= ENEMY_BULLET_SPEED
        if self.rect.right < 0:
            self.kill()