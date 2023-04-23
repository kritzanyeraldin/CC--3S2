class Board:
    def __init__(self):
        self.board_size = 3
        self.cell_size = 100
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]

    def place_piece(self, row, col, piece):
        print('{row} {col} {piece}')
        print(self.board)
        if self.board[row][col] is None:
            print('esta vacia')
            self.board[row][col] = piece
            return True
        else:
            print(f'La casilla ({row},{col}) ya está ocupada')
            return False
