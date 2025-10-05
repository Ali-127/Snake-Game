import pygame
from game import Game


if __name__ == '__main__':
    game = Game()  # initialize game object
    game.game_on()
    pygame.quit()  # Quit pygame after the main loop ends
