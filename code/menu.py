import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_PATH, SOUND_PATH, BLACK


def menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('City Shooter - Menu')
    clock = pygame.time.Clock()

    background = pygame.image.load(IMAGE_PATH + 'MenuBg.png')
    pygame.mixer.music.load(SOUND_PATH + 'menu_music.wav')
    pygame.mixer.music.play(-1)

    # Cores e fontes
    orange_yellow = (255, 200, 0)
    title_font = pygame.font.SysFont('arial', 60, bold=True, italic=True)
    button_font = pygame.font.SysFont('arial', 32, bold=True)

    # Textos
    title = title_font.render('CITY SHOOTER', True, orange_yellow)
    play_text = button_font.render('PLAY', True, orange_yellow)
    exit_text = button_font.render('EXIT', True, orange_yellow)

    # Áreas clicáveis com base nos textos
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, 160))
    exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH // 2, 220))

    while True:
        screen.blit(background, (0, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))
        screen.blit(play_text, play_rect.topleft)
        screen.blit(exit_text, exit_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    return 'play'
                if exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)
