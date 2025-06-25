
import os
import sys


SCREEN_WIDTH = 576
SCREEN_HEIGHT = 324
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 4
ENEMY_BULLET_SPEED = 6

PLAYER_HEALTH = 10


BASE_PATH = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))


IMAGE_PATH = os.path.join(BASE_PATH, 'assets', 'images')
SOUND_PATH = os.path.join(BASE_PATH, 'assets', 'sounds')
