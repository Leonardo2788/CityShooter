
import pygame
import os



from config import IMAGE_PATH, ENEMY_BULLET_SPEED


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        full_image_path = os.path.join(IMAGE_PATH, 'EnemyShot.png')
        self.image = pygame.image.load(full_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= ENEMY_BULLET_SPEED
        if self.rect.right < 0:
            self.kill()