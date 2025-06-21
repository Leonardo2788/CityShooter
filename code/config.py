# config.py

import os

# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminhos dos assets (imagens e sons)
IMAGE_PATH = os.path.join(BASE_DIR, 'assets', 'images') + os.sep
SOUND_PATH = os.path.join(BASE_DIR, 'assets', 'sounds') + os.sep

# Dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Frames por segundo
FPS = 60

# Cores RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Velocidades
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 3
