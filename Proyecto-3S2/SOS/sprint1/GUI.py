import pygame
import sys


class Game(pygame.Surface):
    def __init__(self, width, height, name):
        super().__init__((width, height), flags=pygame.SRCALPHA)
        pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        self.width = width
        self.height = height

    def drawBoard(self):
        BOARD_SIZE = 3
        CELL_SIZE = 100
        WHITE = (255, 255, 255)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                rect = pygame.Rect(col * CELL_SIZE + (self.width - BOARD_SIZE * CELL_SIZE)/2,
                                   row * CELL_SIZE + (self.height - BOARD_SIZE * CELL_SIZE)/2,
                                   CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self, WHITE, rect, 2)
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


