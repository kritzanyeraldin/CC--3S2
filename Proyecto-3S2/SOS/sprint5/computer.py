from Board import Board
from Game import SimpleGame, GeneralGame
import random
class Computer:
    def __init__(self, game):
        self.game = game
        self.board = game.get_board()
        self.size = self.board.get_board_size()
        self.cells = None
        self.piece = None

    def set_cells(self, row, col):
        self.cells = (row, col)

    def get_cells(self):
        return self.cells[0],self.cells[1]

    def set_piece(self,piece):
        self.piece = piece
    def get_piece(self):
        return self.piece

    def move(self,player):
        # Obtener una lista de las casillas vacías en el tablero
        empty_cells = []
        size = self.size
        for row in range(size):
            for col in range(size):
                if self.board.get_piece(row, col) == 'None':
                    empty_cells.append((row, col))

        if len(empty_cells) == 0:
            return 'No hay movimientos disponibles'
        print(empty_cells)

        # Verificar si hay algún movimiento que complete un SOS

        if self.game.type_game() == 'Simple':
            for row, col in empty_cells:
                print(row, col)
                # Probar colocando la pieza 'S'
                self.board.insert_piece(row, col, 'S', player)
                if self.board.complete_SOS_simple()[0]:
                    # Guarda las casillas
                    self.set_cells(row, col)
                    self.set_piece('S')
                    return f'La computadora ha colocado la pieza S en la casilla ({row}, {col}) y ha ganado'

                # print(self.get_piece(row,col))
                self.board.cell_empty(row, col)
                # Probar colocando la pieza 'O'
                self.board.insert_piece(row, col, 'O', player)
                # print(self.get_piece(row, col))
                if self.board.complete_SOS_simple()[0]:
                    # Guarda las casillas
                    self.set_cells(row, col)
                    self.set_piece('O')
                    return f'La computadora ha colocado la pieza O en la casilla ({row}, {col}) y ha ganado'

                # Si no completa un SOS, revertir el movimiento y seguir probando
                self.board.cell_empty(row, col)

        elif self.game.type_game() == 'General':
            # Verificar si hay algún movimiento que complete un SOS
            for row, col in empty_cells:
                print(row, col)
                # Probar colocando la pieza 'S'
                self.board.insert_piece(row, col, 'S', player)
                if 'SOS' in self.board.complete_SOS_general(row, col, computer=True)[0]:
                    # Guarda las casillas
                    self.set_cells(row, col)
                    self.set_piece('S')
                    return f'La computadora ha colocado la pieza S en la casilla ({row}, {col}) y ha ganado'

                # print(self.get_piece(row,col))
                self.board.cell_empty(row, col)
                # Probar colocando la pieza 'O'
                self.board.insert_piece(row, col, 'O', player)
                # print(self.get_piece(row, col))
                if 'SOS' in self.board.complete_SOS_general(row, col, computer=True)[0]:
                    # Guarda las casillas
                    self.set_cells(row, col)
                    self.set_piece('O')
                    return f'La computadora ha colocado la pieza O en la casilla ({row}, {col}) y ha ganado'

                # Si no completa un SOS, revertir el movimiento y seguir probando
                self.board.cell_empty(row, col)

        # Si no se puede ganar en este movimiento, seleccionar una casilla vacía al azar
        row, col = random.choice(empty_cells)
        print(row, col)
        # Determinar la pieza que colocará la computadora (S u O)
        piece = random.choice(['S', 'O'])

        # Realizar el movimiento
        self.board.insert_piece(row, col, piece, player)
        # Guarda las casillas
        self.set_piece(piece)
        self.set_cells(row, col)

        return f'La computadora ha colocado la pieza {piece} en la casilla ({row}, {col})'


'''
#main
board = Board(3)
game=GeneralGame(board)
game.set_players('red','blue')

com=Computer(game)
board.insert_piece(0,0,'S','red')
print(board.get_board())
#com.move()
print(board.get_board())

board.insert_piece(2,2,'S','red')
print(board.get_board())
#com.move()
board.insert_piece(1,1,'O','blue')
print(board.get_board())

print(board.dict_sos)
print('******')

print(game.take_turn('blue',1,1))
print(board.dict_sos)

board.insert_piece(1,2,'S','red')
com.move()
print(board.get_board())
print(board.dict_sos)
print(game.take_turn('blue',com.get_cells()[0],com.get_cells()[1]))
'''''

