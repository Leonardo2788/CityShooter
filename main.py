
import pygame
import sys


import config


from src.menu import menu
from src.game import Game

if __name__ == '__main__':

    pygame.init()



    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("City Shooter")


    chosen_option = menu(screen)

    if chosen_option == 'play':

        game_instance = Game(screen)
        game_instance.run()


    pygame.quit()
    sys.exit()