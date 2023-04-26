class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self.create_board()

    def get_board_size(self):
        return self.board_size

    def create_board(self):
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]
        return self.board

    def get_piece(self, row, col):
        if (0 <= row < self.board_size) and (0 <= col < self.board_size):
            return self.board[row][col]
        else:
            return None

    def get_board(self):
        return self.board

    def insert_piece(self, row, col, piece):
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

        if not (self.get_piece(row, col) == None):
            return 'Casilla ocupada'

        # Asignación de la pieza al tablero
        self.board[row][col] = piece

    def rows(self):
        row = 0
        m = ''
        while row < self.get_board_size():
            for col in range(self.get_board_size()):
                m += self.get_piece(row, col)
            if m == 'SOS':
                return True
                break
            else:
                m=''
                row += 1
                continue
        return False

    def cols(self):
        col=0
        m=''
        while col<self.get_board_size():
            for row in range(self.get_board_size()):
                m+=self.get_piece(row,col)
            if m=='SOS':
                return True
                break
            else:
                m=''
                col+=1
                continue
        return False

    def check_diagonals(self):
        size = self.get_board_size()
        for i in range(size):
            for j in range(size):
                for k in range(4, min(size - i, size - j) + 1):
                    # diagonal desde la esquina superior izquierda hasta la inferior derecha
                    m = ""
                    for x in range(k):
                        m += self.get_piece(i+x,j+x)
                    if m == "SOS":
                        return True
                    # diagonal desde la esquina inferior izquierda hasta la superior derecha
                    if i >= k - 1:
                        n = ""
                        for x in range(k):
                            n += self.get_piece(i-x,j+x)
                        if n == "SOS":
                            return True
        return False


    def complete_SOS(self):

            if m=='SOS':
                print(f'complete')



board = Board(4)
print(board.get_board())


for m in range(4):
    i = int(input('Ingrese fila: '))
    j = int(input('Ingrese columna: '))
    p = input('Ingrese una pieza: ')
    board.insert_piece(i, j, p)

print(board.get_board())
if board.rows():
    print('win')

else:
    print('lose')
