class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        if not self.size_verification():
            raise ValueError('Ingrese un tamaño valido.')
        self.board = self.create_board()

    def get_board_size(self):
        return self.board_size

    def set_board_size(self, size):
        self.board_size = size

    def get_piece(self, row, col):
        if (0 <= row < self.board_size) and (0 <= col < self.board_size):
            return self.board[row][col]
        else:
            return None

    def get_letter(self, row, col):
        if self.get_piece(row, col) == None:
            return None
        else:
            if (0 <= row < self.board_size) and (0 <= col < self.board_size):
                return self.board[row][col][0]

    def get_player(self, row, col):
        if self.get_piece(row, col) == None:
            return None
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
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]
        return self.board

    # Retorna True si todas las casillas del tablero estan llenas
    def board_complete(self):
        size = self.get_board_size()
        for row in range(size):
            for col in range(size):
                piece = self.get_piece(row, col)
                if not piece is None:
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
                if piece is None:
                    continue
                else:
                    return False
        return True

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

        if not self.get_piece(row, col) == None:
            return 'Casilla ocupada'

        # Asignación de la pieza al tablero
        self.board[row][col] = (piece, player)

    #Retorna si completo un SOS y el jugador que lo hizo
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
                if self.get_letter(row, col) == 'S' and self.get_letter(row +
                                                                      1, col) == 'O' and self.get_letter(
                        row + 2,
                        col) == 'S':
                    return True, self.get_player(row,col)

        # Verifica en diagonal(es) de izquierda a derecha
        for row in range(size - 2):
            for col in range(size - 2):
                if self.get_letter(row, col) == 'S' and self.get_letter(row + 1,col + 1) == 'O' and self.get_letter(
                        row + 2, col + 2) == 'S':
                    return True, self.get_player(row,col)
        # Verifica en diagonal(es) de derecha a izquierda
        for row in range(2, size):
            for col in range(size - 2):
                if self.get_letter(row, col) == 'S' and self.get_letter(row - 1, col + 1) == 'O' and self.get_letter(
                        row - 2, col + 2) == 'S':
                    return True, self.get_player(row,col)
        return False, 'None'

    def complete_SOS_general(self, row, col):
        size = self.get_board_size()

        # Verifica en fila
        if col < size - 2:
            if self.get_letter(row, col) == 'S' and self.get_letter(row,
                                                                    col + 1) == 'O' and self.get_letter(
                    row, col + 2) == 'S':
                return 'True', self.get_player(row, col), (
                (row, col), (row, col + 1), (row, col + 2))

        # verifica en columna
        if row < size - 2:
            if self.get_letter(row, col) == 'S' and self.get_letter(row + 1,
                                                                    col) == 'O' and self.get_letter(
                    row + 2, col) == 'S':
                return 'True', self.get_player(row, col), (
                (row, col), (row + 1, col), (row + 2, col))

        # Verifica en diagonal de izquierda a derecha
        if row < size - 2 and col < size - 2:
            if self.get_letter(row, col) == 'S' and self.get_letter(row + 1,
                                                                    col + 1) == 'O' and self.get_letter(
                    row + 2, col + 2) == 'S':
                return 'True', self.get_player(row, col), (
                (row, col), (row + 1, col + 1), (row + 2, col + 2))

        # Verifica en diagonal de derecha a izquierda
        if row >= 2 and row < size and col < size - 2:
            if self.get_letter(row, col) == 'S' and self.get_letter(row - 1,
                                                                    col + 1) == 'O' and self.get_letter(
                    row - 2, col + 2) == 'S':
                return 'True', self.get_player(row, col), (
                (row, col), (row - 1, col + 1), (row - 2, col + 2))

        return False, 'None', 'None'


''''
    def win_or_tie(self, turn):
        if self.board_empty():
            return 'Empty Board', 'red', 'None'
        else:
            if self.board_complete():
                complete, player = self.complete_SOS()
                if complete:
                    return 'Win', player, 'None'
                else:
                    return 'Tie', player, 'None'
            else:
                complete, player = self.complete_SOS()
                if complete:
                    return 'Win', player, 'None'
                else:
                    return 'Continue', player, self.player2 if turn == self.player1 else self.player1





#main
board = Board(3)
print(board.create_board())
board.insert_piece(0,0,'S','blue')
board.insert_piece(0,1,'O','red')
board.insert_piece(0,2,'S','blue')
print(board.get_board())
print(board.win_or_tie())
'''''


