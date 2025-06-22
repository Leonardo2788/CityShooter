import pygame
import random
import time
from config import SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_PATH, SOUND_PATH, FPS
from player import Player
from enemy import Enemy
from bullet import Bullet
from explosion import Explosion


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

        # Fundo com múltiplas camadas (agora horizontal)
        self.background_layers = [
            {"image": pygame.image.load(IMAGE_PATH + f'Level1Bg{i}.png'), "x": 0, "speed": i * 0.2}
            for i in range(0, 7)
        ]

        # Sprites
        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        self.score = 0
        self.font = pygame.font.SysFont('Arial', 30)
        self.running = True

    def spawn_enemy(self):
        if random.random() < 0.02:
            self.enemies.add(Enemy())

    def handle_collisions(self):
        # Tiros acertando inimigos
        hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for hit in hits:
            self.explosion_sound.play()
            explosion = Explosion(hit.rect.centerx, hit.rect.centery)
            self.explosions.add(explosion)
            self.score += 10

        # Jogador colidindo com inimigos
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.explosion_sound.play()
            explosion = Explosion(self.player.rect.centerx, self.player.rect.centery)
            self.explosions.add(explosion)
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
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        time.sleep(10)
        pygame.quit()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            keys_pressed = pygame.key.get_pressed()

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

            self.player.update(keys_pressed)
            self.bullets.update()
            self.enemies.update()
            self.explosions.update()
            self.handle_collisions()

            self.draw_background()
            self.player_group.draw(self.screen)
            self.bullets.draw(self.screen)
            self.enemies.draw(self.screen)
            self.explosions.draw(self.screen)

            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()

        pygame.quit()
