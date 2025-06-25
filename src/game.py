
import pygame
import random
import time
import os



from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, BLACK,
    IMAGE_PATH, SOUND_PATH, PLAYER_HEALTH, PLAYER_SPEED, BULLET_SPEED,
    ENEMY_SPEED, ENEMY_BULLET_SPEED
)


from .player import Player
from .enemy import Enemy
from .bullet import Bullet
from .enemy_bullet import EnemyBullet
from .explosion import Explosion


class Game:
    def __init__(self, screen):

        self.screen = screen
        self.clock = pygame.time.Clock()

        self.phase = 1
        self.score = 0
        self.phase_name = ""
        self.phase_transition_timer = 0

        self.load_background()
        self.load_music()


        self.shoot_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'shoot.wav'))
        self.enemy_shoot_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'enemy_shoot.wav'))
        self.explosion_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'explosion.wav'))
        self.phase_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, 'phase_transition.wav'))

        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()


        self.font = pygame.font.SysFont('Arial', 24)
        self.running = True

    def load_background(self):
        bg_prefix = 'Level1Bg' if self.phase == 1 else 'Level2Bg'
        self.background_layers = []
        for i in range(12):

            full_image_path = os.path.join(IMAGE_PATH, f'{bg_prefix}{i}.png')
            image = pygame.image.load(full_image_path)

            self.background_layers.append({"image": image, "x": 0, "speed": i * 0.2})

    def load_music(self):
        pygame.mixer.music.stop()
        music_file = 'level1_music.wav' if self.phase == 1 else 'level2_music.wav'

        full_music_path = os.path.join(SOUND_PATH, music_file)
        pygame.mixer.music.load(full_music_path)
        pygame.mixer.music.play(-1)

    def spawn_enemy(self):
        if random.random() < 0.02:
            shoot = self.phase == 2
            self.enemies.add(Enemy(shooting=shoot))

    def handle_collisions(self):

        hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for hit in hits:
            self.explosion_sound.play()
            self.explosions.add(Explosion(hit.rect.centerx, hit.rect.centery))
            self.score += 10


        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.explosion_sound.play()
            self.explosions.add(Explosion(self.player.rect.centerx, self.player.rect.centery))
            self.running = False
            self.show_game_over()


        bullets_hit = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
        if bullets_hit:
            self.player.health -= len(bullets_hit)
            if self.player.health <= 0:
                self.explosion_sound.play()
                self.explosions.add(Explosion(self.player.rect.centerx, self.player.rect.centery))
                self.running = False
                self.show_game_over()

    def scroll_background(self):
        for layer in self.background_layers:
            layer["x"] -= layer["speed"]
            if layer["x"] <= -SCREEN_WIDTH:
                layer["x"] = 0

    def draw_background(self):
        for layer in self.background_layers:
            self.screen.blit(layer["image"], (layer["x"], 0))
            self.screen.blit(layer["image"], (layer["x"] + SCREEN_WIDTH, 0))

    def show_game_over(self):
        game_over_font = pygame.font.SysFont('arial', 60, bold=True)
        orange_yellow = (255, 200, 0)

        text = game_over_font.render("GAME OVER!", True, orange_yellow)

        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)

        pygame.display.flip()
        time.sleep(5)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            keys = pygame.key.get_pressed()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        bullet = self.player.shoot()
                        self.bullets.add(bullet)
                        self.shoot_sound.play()


            self.spawn_enemy()
            self.scroll_background()

            self.player.update(keys)
            self.bullets.update()
            self.enemies.update()
            self.enemy_bullets.update()
            self.explosions.update()
            self.handle_collisions()


            for enemy in self.enemies:
                if self.phase == 2 and random.random() < 0.01:
                    bullet = EnemyBullet(enemy.rect.centerx - 20, enemy.rect.centery)
                    self.enemy_bullets.add(bullet)
                    self.enemy_shoot_sound.play()


            if self.score >= 100 and self.phase == 1:
                self.phase = 2
                self.load_background()
                self.load_music()
                self.enemies.empty()
                self.enemy_bullets.empty()
                self.phase_sound.play()
                self.phase_name = "FASE 2"
                self.phase_transition_timer = FPS * 3


            self.draw_background()

            self.player_group.draw(self.screen)
            self.bullets.draw(self.screen)
            self.enemies.draw(self.screen)
            self.enemy_bullets.draw(self.screen)
            self.explosions.draw(self.screen)


            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))

            health_text = self.font.render(f"Health: {self.player.health}", True, WHITE)
            self.screen.blit(health_text, (10, 40))


            if self.phase_transition_timer > 0:
                phase_text = self.font.render(self.phase_name, True, (255, 255, 0))

                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
                self.screen.blit(phase_text, phase_text_rect)
                self.phase_transition_timer -= 1

            pygame.display.flip()

        pygame.quit()