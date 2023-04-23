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
        self.board = Board()

        self.fill((255, 255, 255))

    def drawBoard(self):
        black = (0, 0, 0)
        for row in range(self.board.board_size):
            for col in range(self.board.board_size):
                rect = pygame.Rect(col * self.board.cell_size + (self.width - self.board.board_size * self.board.cell_size) / 2,
                                   row * self.board.cell_size + (self.height - self.board.board_size * self.board.cell_size) / 2,
                                   self.board.cell_size, self.board.cell_size)
                pygame.draw.rect(self, black, rect, 2)
                if self.board.board[row][col] == "S":
                    font = pygame.font.Font(None, self.board.cell_size)
                    text = font.render("S", True, black)
                    text_rect = text.get_rect(center=rect.center)
                    self.blit(text, text_rect)
                    print(f'S en({row},{col})')
                elif self.board.board[row][col] == "O":
                    font = pygame.font.Font(None, self.board.cell_size)
                    text = font.render("O", True, black)
                    text_rect = text.get_rect(center=rect.center)
                    self.blit(text, text_rect)
                    print(f'O en({row},{col})')
        pygame.display.get_surface().blit(self, (0, 0))

    def events(self):
        print('a')

        pos = pygame.mouse.get_pos()
        print(pos)
        row = int((pos[1] - (self.height - self.board.board_size * self.board.cell_size) / 2) / self.board.cell_size)
        col = int((pos[0] - (self.width - self.board.board_size * self.board.cell_size) / 2) / self.board.cell_size)

        if 0 <= row < self.board.board_size and 0 <= col < self.board.board_size:
            print(f'{row} {col}')
            if self.board.place_piece(row, col, 'S'):
                print(f'Se coloco una S en la casilla, {row}, {col}')

            else:
                print(f'La casilla', row, col, 'ya esta ocupada')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.events()

            self.drawBoard()

            # Actualiza la pantalla
            pygame.display.update()


