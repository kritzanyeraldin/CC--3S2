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

    def take_turn(self, turn):
        raise NotImplementedError()

    def end_game(self):
        raise NotImplementedError()


class SimpleGame(Game):
    def __init__(self, board):
        super().__init__(board)
        pass

    def take_turn(self, turn):
        if self.board.board_empty():
            return 'Empty Board', 'red'
        else:
            if self.board.board_complete():
                complete_sos, player = \
                    self.board.complete_SOS_simple()
                if complete_sos:
                    return 'Win', player
                else:
                    return 'Tie', player
            else:
                complete_sos, player= \
                    self.board.complete_SOS_simple()
                if complete_sos:
                    return 'Win', player
                else:
                    return 'Continue', player, self.player2 if turn == \
                                                               self.player1 \
                        else self.player1


class GeneralGame(Game):
    def __init__(self, board):
        super().__init__(board)
        self.count_player1 = 0
        self.count_player2 = 0
        self.dict_sos={'player1': [], 'player2': []}

    def set_count_player1(self, n):
        self.count_player1 = n

    def set_count_player2(self, n):
        self.count_player2 = n

    def save_sos(self, player, position):
        self.dict_sos[player].append(position)

    def take_turn(self, turn):
        if self.board.board_empty():
            return 'Empty Board'
        else:
            if self.board.board_complete():
                complete = self.board.complete_SOS_general()
                if complete:
                    return 'Point'
                else:
                    return 'Continue'
            else:
                complete = self.board.complete_SOS_general()
                if complete:
                    return 'Point'
                else:
                    return 'Continue'

    def get_position_line(self):
        var=self.take_turn(0)
        if var=='Point':
            return self.board.position[-1]

# main
board = Board(3)
mode = GeneralGame(board)
#Se establecen los jugadores
p1 = 'player2'
p2 = 'player1'
mode.players(p1, p2)

# Se referencia el tablero
b = mode.get_board()
print(f'a{b.get_board()}')
print(mode.get_players())

# Inicia el juego
b.insert_piece(0,0,'S','player1')
print(mode.take_turn('player1'))

b.insert_piece(0,1,'O','player2')
print(mode.take_turn('player2'))

b.insert_piece(0,2,'S','player1')
print(mode.take_turn('player1'))

b.insert_piece(1,0,'S','player1')
print(mode.take_turn('player1'))

b.insert_piece(1,1,'O','player2')
print(mode.take_turn('player2'))

b.insert_piece(1,2,'S','player1')
print(mode.take_turn('player1'))

b.insert_piece(2,0,'S','player1')
print(mode.take_turn('player1'))

b.insert_piece(2,1,'O','player2')
print(mode.take_turn('player2'))

b.insert_piece(2,2,'S','player1')
print(f'\na{b.get_board()}')

print(mode.take_turn('player1'))



