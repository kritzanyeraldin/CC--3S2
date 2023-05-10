class Board:
    def __init__(self, board_size):
        self.board_size = board_size
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
        if self.get_piece(row,col)==None:
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

    def create_board(self):
        if self.size_verification():
            self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]
            return self.board

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

    def complete_SOS(self):
        size = self.get_board_size()
        # Verifica en fila
        for row in range(size):
            for col in range(size - 2):
                if self.get_piece(row, col) == ('S',self.get_player(row,col)) and self.get_piece(row, col + 1) == ('O',self.get_player(row,col)) and self.get_piece(row,
                                                                                                                 col + 2) == ('S',self.get_player(row,col)):
                    return True, self.get_player(row, col)

        # verifica en columna
        for row in range(size - 2):
            for col in range(size):
                if self.get_piece(row, col) == ('S',self.get_player(row,col)) and self.get_piece(row + 1, col) ==('O',self.get_player(row,col)) and self.get_piece(
                        row + 2,
                        col) == ('S',self.get_player(row,col)):
                    return True, self.get_player(row, col)

        # Verifica en diagonal(es) de izquierda a derecha
        for row in range(size - 2):
            for col in range(size - 2):
                if self.get_piece(row, col) == ('S', self.get_player(row,col)) and self.get_piece(row + 1, col + 1) == ('O',self.get_player(row,col)) and self.get_piece(
                        row + 2, col + 2) == ('S',self.get_player(row,col)):
                    return True, self.get_player(row, col)
        # Verifica en diagonal(es) de derecha a izquierda
        for row in range(2, size):
            for col in range(size - 2):
                if self.get_piece(row, col) == ('S',self.get_player(row,col)) and self.get_piece(row - 1, col + 1) == ('O',self.get_player(row,col)) and self.get_piece(
                        row - 2, col + 2) == ('S',self.get_player(row,col)):
                    return True, self.get_player(row, col)
        return False,'None'

    def win_or_tie(self):
        if self.board_empty():
            return 'Empty Board','red'
        else:
            if self.board_complete():
                complete,player = self.complete_SOS()
                if complete:
                    return 'Win',player
                else:
                    return 'Tie',player
            else:
                complete,player = self.complete_SOS()
                if complete:
                    return 'Win', player
                else:
                    return 'Continue',player




