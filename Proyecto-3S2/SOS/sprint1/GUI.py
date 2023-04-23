import pygame
import sys
from Board import Board


class Game(pygame.Surface):
    def __init__(self, width, height, name):
        super().__init__((width, height), flags=pygame.SRCALPHA)
        pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        self.width = width
        self.height = height

    def drawBoard(self):
        board = Board()
        white = (255, 255, 255)
        for row in range(board.board_size):
            for col in range(board.board_size):
                rect = pygame.Rect(col * board.cell_size + (self.width - board.board_size * board.cell_size) / 2,
                                   row * board.cell_size + (self.height - board.board_size * board.cell_size) / 2,
                                   board.cell_size, board.cell_size)
                pygame.draw.rect(self, white, rect, 2)
        pygame.display.get_surface().blit(self, (0, 0))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.drawBoard()
            #pygame.display.get_surface().blit(self, (0, 0))
        # Actualiza la pantalla
            pygame.display.update()


