from menu import menu
from game import Game

if __name__ == '__main__':
    escolha = menu()
    if escolha == 'play':
        jogo = Game()
        jogo.run()
