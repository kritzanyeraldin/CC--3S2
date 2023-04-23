class Board:
    def __init__(self):
        self.board_size = 3
        self.cell_size = 100
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]