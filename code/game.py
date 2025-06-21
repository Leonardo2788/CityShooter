# game.py

import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_PATH, SOUND_PATH, FPS
from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()

        # Sons
        pygame.mixer.music.load(SOUND_PATH + 'background_music.wav')
        pygame.mixer.music.play(-1)
        self.shoot_sound = pygame.mixer.Sound(SOUND_PATH + 'shoot.wav')
        self.explosion_sound = pygame.mixer.Sound(SOUND_PATH + 'explosion.wav')

        # Background
        self.background = pygame.image.load(IMAGE_PATH + 'background.png')

        # Sprites
        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.score = 0
        self.font = pygame.font.SysFont('Arial', 30)
        self.running = True

    def spawn_enemy(self):
        if random.random() < 0.02:
            self.enemies.add(Enemy())

    def handle_collisions(self):
        hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if hits:
            self.explosion_sound.play()
            self.score += len(hits)

        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.running = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            keys_pressed = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = self.player.shoot()
                        self.bullets.add(bullet)
                        self.shoot_sound.play()

            self.spawn_enemy()
            self.player.update(keys_pressed)
            self.bullets.update()
            self.enemies.update()
            self.handle_collisions()

            self.screen.blit(self.background, (0, 0))
            self.player_group.draw(self.screen)
            self.bullets.draw(self.screen)
            self.enemies.draw(self.screen)

            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()

        pygame.quit()
