from Board import Board


class Game:
    def __init__(self, board):
        self.board = board

    
class SimpleGame(Game):
    def __init__(self, board):
        super().__init__(board)
        pass

    def print(self):
        print(self.board.get_board())


class GeneralGame(Game):
    def __init__(self, board):
        super().__init__(board)
        pass


# main
board = Board(3)
mode = SimpleGame(board)
mode.print()
