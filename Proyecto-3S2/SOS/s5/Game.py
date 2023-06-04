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

    def take_turn(self, turn,row,col):
        raise NotImplementedError()


class SimpleGame(Game):
    def __init__(self, board):
        super().__init__(board)
        pass

    def take_turn(self, turn,row,col):
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
                complete_sos, player = \
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

    def set_count_player1(self, n):
        self.count_player1 = n

    def set_count_player2(self, n):
        self.count_player2 = n

    def take_turn(self, turn,row, col):
        if self.board.board_empty():
            return 'Empty Board', 'red'
        else:
            if self.board.board_complete():
                self.set_count_player1(len(self.board.dict_sos['red']))
                self.set_count_player2(len(self.board.dict_sos['blue']))
                if self.count_player2 > self.count_player1:
                    return 'Win', self.player2
                elif self.count_player1 > self.count_player2:
                    return 'Win', self.player1
                else:
                    return 'Tie', 'None'
            else:
                complete, player = self.board.complete_SOS_general(row, col)
                if 'SOS' in complete:
                    return 'Continue', player
                else:
                    return 'Continue', self.player2 if player != self.player2 else self.player1



'''
# main
board = Board(3)

mode = GeneralGame(board)
a=mode.board.get_board_size()
print(a)


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

'''''
