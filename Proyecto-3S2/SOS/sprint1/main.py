import pygame
from GUI import Game

if __name__ == "__main__":
    width = 800
    alto = 600
    name = 'SOS'
    pygame.init()

    my_screen = Game(width, alto, name)
    my_screen.run()
