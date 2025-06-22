import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGE_PATH = os.path.join(BASE_DIR, 'assets', 'images') + os.sep
SOUND_PATH = os.path.join(BASE_DIR, 'assets', 'sounds') + os.sep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 4
