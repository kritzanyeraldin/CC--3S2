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
        if player==self.player1:
            self.dict_sos['player1'].append(position)
        elif player==self.player2:
            self.dict_sos['player2'].append(position)
        return self.dict_sos

    def take_turn(self, turn,row,col):
        if self.board.board_empty():
            return 'Empty Board', 'red', 'None'
        else:
            if self.board.board_complete():
                if self.count_player1 > self.count_player2:
                    return 'Win', self.player1, 'None'
                elif self.count_player1 < self.count_player2:
                    return 'Win', self.player2, 'None'
                else:
                    return 'Tie', 'None', 'None'
            else:
                complete_sos, player, position = \
                    self.board.complete_SOS_general(row,col)
                arr = [i for i in range(self.board.get_board_size())]
                if complete_sos:
                    if player == self.player1:
                        for pos in self.dict_sos['player1']:
                            if pos == position:
                                if position[0][0] in arr:
                                    arr.remove(position[0][0])
                            else:
                                self.save_sos(player, position)
                    elif player == self.player2:
                        for pos in self.dict_sos['player2']:
                            if pos == position:
                                if position[0][0] in arr:
                                    arr.remove(position[0][0])
                            else:
                                self.save_sos(player, position)
                else:
                    return 'Continue', player, self.player2 if turn == self.player1 else self.player1


''''
# main
board = Board(3)
mode = GeneralGame(board)
#Se establecen los jugadores
p1 = 'blue'
p2 = 'red'
mode.players(p1, p2)

# Se referencia el tablero
b = mode.get_board()
print(f'a{b.get_board()}')
print(mode.get_players())

# Inicia el juego
b.insert_piece(0,0,'S','blue')
print(mode.take_turn('blue'))

b.insert_piece(0,1,'O','red')
print(mode.take_turn('red'))

b.insert_piece(0,2,'S','blue')
print(mode.take_turn('blue'))

b.insert_piece(1,0,'S','blue')
print(mode.take_turn('blue'))

b.insert_piece(1,1,'O','red')
print(mode.take_turn('red'))

b.insert_piece(1,2,'S','blue')
print(mode.take_turn('blue'))

b.insert_piece(2,0,'S','blue')
print(mode.take_turn('blue'))

b.insert_piece(2,1,'O','red')
print(mode.take_turn('red'))

b.insert_piece(2,2,'S','blue')
print(f'\na{b.get_board()}')

print(mode.take_turn('blue'))
[(0, 0), (0, 1), (0, 2)]
'''''

sos_completados = {'player1': [], 'player2': [[(1, 1), (2, 2), (3, 3)]]}
a = ((0, 0), (0, 1), (0, 2))

sos_completados['player1'].append(((0, 0), (0, 1), (0, 2)))

ad=sos_completados['player1']
for s in ad:
    print(s[0][0])

arr = [i for i in range(3)]
if 2 in arr:
    arr.remove(2)
    print(arr)