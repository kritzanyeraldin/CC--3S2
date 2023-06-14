import random


class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        if not self.size_verification():
            raise ValueError('Ingrese un tamaño valido.')
        self.board = self.create_board()
        self.dict_sos = {'red': [], 'blue': []}

    def get_board_size(self):
        return self.board_size

    def set_board_size(self, size):
        self.board_size = size

    def get_piece(self, row, col):
        if (0 <= row < self.board_size) and (0 <= col < self.board_size):
            return self.board[row][col]
        else:
            return 'None'

    def get_letter(self, row, col):
        if self.get_piece(row, col) == 'None':
            return 'None'
        else:
            if (0 <= row < self.board_size) and (0 <= col < self.board_size):
                return self.board[row][col][0]

    def get_player(self, row, col):
        if self.get_piece(row, col) == 'None':
            return 'None'
        else:
            if (0 <= row < self.board_size) and (0 <= col < self.board_size):
                return self.board[row][col][1]

    def get_board(self):
        return self.board

    def size_verification(self):
        if self.board_size < 3:
            return False
        else:
            return True

    def create_board(self):
        self.board = [['None' for i in range(self.board_size)] for j in range(
            self.board_size)]
        return self.board

    # Retorna True si todas las casillas del tablero estan llenas
    def board_complete(self):
        size = self.get_board_size()
        for row in range(size):
            for col in range(size):
                piece = self.get_piece(row, col)
                if piece != 'None':
                    continue
                else:
                    return False
        return True

    # Retorna True si el tablero esta vacio
    def board_empty(self):
        size = self.get_board_size()
        for row in range(size):
            for col in range(size):
                piece = self.get_piece(row, col)
                if piece == 'None':
                    continue
                else:
                    return False
        return True

    def cell_empty(self,row,col):
        self.board[row][col]='None'

    def insert_piece(self, row, col, piece, player):
        # Validación del rango de las coordenadas
        if not (0 <= row < self.board_size) or not (0 <= col < self.board_size):
            return 'Coordenadas fuera del rango del tablero'

        # Validación del tipo de dato de la pieza
        if not isinstance(piece, str):
            return 'La pieza debe ser de tipo string'

        # Validación de valores válidos para la pieza
        valid_pieces = ['S', 'O']

        if piece not in valid_pieces:
            return 'Pieza no valida'

        if  self.get_piece(row, col) != 'None':
            return 'Casilla ocupada'

        # Asignación de la pieza al tablero
        self.board[row][col] = (piece, player)  

    # Retorna si completo un SOS y el jugador que lo hizo
    def complete_SOS_simple(self):
        size = self.get_board_size()
        # Verifica en fila
        for row in range(size):
            for col in range(size - 2):
                if self.get_letter(row, col) == 'S' and self.get_letter(row,
                                                                        col +
                                                                        1) == 'O' and self.get_letter(row, col + 2) == 'S':
                    return True, self.get_player(row, col)

        # verifica en columna
        for row in range(size - 2):
            for col in range(size):
                if self.get_letter(row, col) == 'S' and self.get_letter(row + 1, col) == 'O' and self.get_letter(row + 2,
                                                                                                                 col) == 'S':
                    return True, self.get_player(row, col)

        # Verifica en diagonal(es) de izquierda a derecha
        for row in range(size - 2):
            for col in range(size - 2):
                if self.get_letter(row, col) == 'S' and self.get_letter(row + 1, col + 1) == 'O' and self.get_letter(
                        row + 2, col + 2) == 'S':
                    return True, self.get_player(row, col)

        # Verifica en diagonal(es) de derecha a izquierda
        for row in range(2, size):
            for col in range(size - 2):
                if self.get_letter(row, col) == 'S' and self.get_letter(row - 1, col + 1) == 'O' and self.get_letter(
                        row - 2, col + 2) == 'S':
                    return True, self.get_player(row, col)
        return False, 'None'

    def complete_SOS_general(self, row, col,computer=False):
        # Tamaño del tablero
        size = self.get_board_size()

        # Guarda el jugador actual
        player = self.get_player(row, col)

        # Guarda la posicion de la jugada actual
        jugada = None

        # esta lista almacena temporalmente las letras de la fila
        sos = []

        # Lista
        complete = []

        # Verificacion en fila
        for j in range(col - 2, col + 1):
            if j >= 0 and j + 2 < size:
                jugada = ((row, j), (row, j + 1), (row, j + 2))
                if (jugada not in self.dict_sos['red']) and (jugada not in
                                                             self.dict_sos[
                                                                 'blue']):
                    sos.append(self.get_letter(row, j))
                    sos.append(self.get_letter(row, j + 1))
                    sos.append(self.get_letter(row, j + 2))
                    # print('fila')
                    # print(j,sos)
                    if "".join(sos) == 'SOS':
                        if computer:
                            complete.append("".join(sos))
                            break
                        else:
                            self.dict_sos[player].append(jugada)
                            complete.append("".join(sos))
                            break
                    sos = []  # Reiniciar la lista sos

        # Verificacion en columna
        for i in range(row - 2, row + 1):
            if i >= 0 and i + 2 < size:
                jugada = ((i, col), (i + 1, col), (i + 2, col))
                if (jugada not in self.dict_sos['red']) and (jugada not in
                                                             self.dict_sos[
                                                                 'blue']):
                    sos.append(self.get_letter(i, col))
                    sos.append(self.get_letter(i + 1, col))
                    sos.append(self.get_letter(i + 2, col))
                    # print('col')
                    # print(i,sos)
                    if "".join(sos) == 'SOS':
                        if computer:
                            complete.append("".join(sos))
                            break
                        else:
                            self.dict_sos[player].append(jugada)
                            complete.append("".join(sos))
                            break
                    sos = []  # Reiniciar la lista sos

        # Verfificar en diagonal principal
        colum = col - 2
        for i in range(row - 2, row + 1):
            if i >= 0 and i + 2 < size and colum >= 0:
                jugada = ((i, colum), (i + 1, colum + 1), (i + 2, colum + 2))
                if (jugada not in self.dict_sos['red']) and (jugada not in
                                                             self.dict_sos[
                                                                 'blue']):
                    sos.append(self.get_letter(i, colum))
                    sos.append(self.get_letter(i + 1, colum + 1))
                    sos.append(self.get_letter(i + 2, colum + 2))
                    # print('diagonal')
                    # print(i,sos)
                    if "".join(sos) == 'SOS':
                        if computer:
                            complete.append("".join(sos))
                            break
                        else:
                            self.dict_sos[player].append(jugada)
                            complete.append("".join(sos))
                            break
                    sos = []  # Reiniciar la lista sos
            colum += 1

        # Verfificar diagonal inversa
        fila = row - 2
        for j in range(col + 2, col - 1, -1):
            # print(fila,j)
            if j < size and j - 2 >= 0 and fila >= 0:
                jugada = ((fila, j), (fila + 1, j - 1), (fila + 2,
                                                         j - 2))
                if (jugada not in self.dict_sos['red']) and (jugada not in
                                                             self.dict_sos[
                                                                 'blue']):
                    sos.append(self.get_letter(fila, j))
                    sos.append(self.get_letter(fila + 1, j - 1))
                    sos.append(self.get_letter(fila + 2, j - 2))
                    # print('segunda diagonal')
                    # print(fila, sos)
                    if "".join(sos) == 'SOS':
                        if computer:
                            complete.append("".join(sos))
                            break
                        else:
                            self.dict_sos[player].append(jugada)
                            complete.append("".join(sos))
                            break
                    sos = []  # Reiniciar la lista sos
            fila += 1

            print(complete,player)

        return complete, player



'''

    def win_or_tie_general(self,row,col):
        if self.board_empty():
            return 'Empty Board', 'red'
        else:
            if self.board_complete():
                count_red = len(self.dict_sos['red'])
                count_blue = len(self.dict_sos['blue'])
                if count_blue>count_red:
                    return 'Win', 'red'
                elif count_red>count_blue:
                    return 'Win', 'blue'
                else:
                    return 'Tie', 'None'
            else:
                complete, player=self.complete_SOS_general(row,col)
                if 'SOS' in complete:
                    return 'Continue', player
                else:
                    return 'Continue', 'otro'

    
    def win_or_tie(self):
        if self.board_empty():
            return 'Empty Board', 'red'
        else:
            if self.board_complete():
                complete, player = self.complete_SOS_simple()
                if complete:
                    return 'Win', player
                else:
                    return 'Tie', player
            else:
                complete, player = self.complete_SOS_simple()
                if complete:
                    return 'Win', player
                else:
                    return 'Continue', player
 
#main
board = Board(4)
print(board.create_board())
#board.insert_piece(0,0,'S','blue')
#board.insert_piece(0,1,'O','red')
#primera ronda
board.insert_piece(1,1,'S','blue')
state,player=board.win_or_tie_general(1,1)
print(f'{state}\n{player}\n')

board.insert_piece(1,3,'S','red')
state,player=board.win_or_tie_general(1,3)
print(f'{state}\n{player}\n')

board.insert_piece(1,2,'O','blue')
print(board.get_board())
state,player=board.win_or_tie_general(1,2)
print(f'{state}\n{player}\n')

print(board.dict_sos)
print('\n')



board = Board(4)

board.insert_piece(0,0,'S','blue')
board.insert_piece(0,1,'O','red')
board.insert_piece(0,2,'S','blue')
print(board.get_board())
board.complete_SOS_general(0,2)
print(board.dict_sos)



#segunda ronda




board.insert_piece(2,2,'S','red')
print(board.get_board())
board.complete_SOS_general(2,2)
print(board.dict_sos)
print('\n')
#tercera ronda
board.insert_piece(0,3,'S','red')
board.insert_piece(2,1,'S','blue')
print(board.get_board())
board.complete_SOS_general(2,1)
print(board.dict_sos)
print('\n')
#cuarta ronda
board.insert_piece(2,3,'S','blue')
board.insert_piece(0,1,'S','red')
print(board.get_board())
board.complete_SOS_general(0,1)
print(board.dict_sos)
'''''
