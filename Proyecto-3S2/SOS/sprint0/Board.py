class Board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self.create_board()

    def get_board_size(self):
        return self.board_size

    def create_board(self):
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]
        return self.board



