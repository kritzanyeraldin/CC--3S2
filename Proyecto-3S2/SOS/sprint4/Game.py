from Board import Board


class Game:
    def __init__(self, board):
        self.board = board
        self.player1 = None
        self.player2 = None

    def players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def get_players(self):
        return self.player1, self.player2

    def get_board(self):
        return self.board

    def take_turn(self):
        raise NotImplementedError()

    def check_winner(self):
        raise NotImplementedError()

    def end_game(self):
        raise NotImplementedError()


class SimpleGame(Game):
    def __init__(self, board):
        super().__init__(board)
        pass

    def print(self):
        print(self.board.get_board())

    def take_turn(self):
        pass



class GeneralGame(Game):
    def __init__(self, board):
        super().__init__(board)
        pass


# main
board = Board(3)
mode = SimpleGame(board)
#Se establecen los jugadores
p1 = 'red'
p2 = 'blue'
mode.players(p1, p2)
mode.print()
# Se referencia el tablero
b = mode.get_board()
print(f'a{b.get_board()}')
print(mode.get_players())

# Inicia el juego
b.insert_piece(0, 0, 'S', p1)
print(f'a{b.get_board()}')