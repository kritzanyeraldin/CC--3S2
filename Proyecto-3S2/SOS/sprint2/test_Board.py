from Board import Board
import random
import unittest


class TestBoard(unittest.TestCase):
    #este metodo inicializa un tablero de nxn
    def setUp(self):
        self.board_size = random.randint(3, 100)
        self.board = Board(self.board_size)

    # Comprueba que el tablero se haya creado correctamente y que sus elementos sean None
    def test_create_board(self):

        # Verificamos si el tablero tiene tamaño n en cada dimension
        self.assertEqual(len(self.board.board), self.board_size)
        self.assertEqual(len(self.board.board[0]), self.board_size)
        self.assertEqual(len(self.board.board[1]), self.board_size)
        self.assertEqual(len(self.board.board[2]), self.board_size)

        # Verifica si cada casilla esta vacia para un tablero vacio
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                self.assertEqual(self.board.board[i][j], None)


    def test_insert_piece_valid(self):
        # Insertar una pieza valida en una posicion valida
        row = 0
        col = 0
        piece = 'O'
        self.board.insert_piece(row, col, piece)
        result = self.board.get_piece(row, col)
        self.assertEqual(result, 'O')

    def test_insert_piece_invalid_coordinates(self):
        # Insertar una pieza en una posicion invalida
        row = self.board_size
        col = self.board_size
        piece = 'S'
        result = self.board.insert_piece(row,col,piece)
        self.assertEqual(result, 'Coordenadas fuera del rango del tablero')
        self.assertIsNone(self.board.get_piece(row, col))

    def test_insert_piece_invalid_piece_type(self):
        # Insertar una pieza de tipo invalido entero
        row = 0
        col = 0
        piece = 4
        result = self.board.insert_piece(row, col, piece)
        self.assertEqual(result,'La pieza debe ser de tipo string')
        self.assertIsNone(self.board.get_piece(row,col))

    def test_insert_piece_invalid_piece_value(self):
        # Insertar una pieza con un valor invalido string
        row = 0
        col = 0
        piece = 'W'
        result = self.board.insert_piece(row, col, piece)
        self.assertEqual(result, 'Pieza no valida')
        self.assertIsNone(self.board.get_piece(row, col))

    def test_insert_piece_valid_position_busy(self):
        # Insertar una pieza valida en una casilla ocupada
        row = 0
        col = 0
        piece = 'S'
        # Insertamos una pieza en (0,0)
        self.board.insert_piece(row, col, piece)
        # Volvemos a insertar otra pieza en (0,0)
        result = self.board.insert_piece(row, col, piece)
        self.assertEqual(result,'Casilla ocupada')

class TestCompleteSOS(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)
    # Test
    def test_complete_row_SOS(self):
        #Comprueba si exite un SOS en 3 casillas contiguas de  una fila
        self.board.insert_piece(0, 0, 'S')
        self.board.insert_piece(0, 1, 'S')
        self.board.insert_piece(0, 2, 'O')
        self.board.insert_piece(0, 3, 'S')
        result = self.board.complete_SOS()
        self.assertTrue(result)

    def test_complete_colum_SOS(self):
        # Comprueba si exite un SOS en 3 casillas contiguas de  una columna
        self.board.insert_piece(0, 0, 'S')
        self.board.insert_piece(1, 0, 'S')
        self.board.insert_piece(2, 0, 'O')
        self.board.insert_piece(3, 0, 'S')
        result = self.board.complete_SOS()
        self.assertTrue(result)

    def test_complete_diagonal_rigth_to_left(self):
        # Comprueba si exite un SOS en 3 casillas contiguas de una diagonal que va izquierda a derecha
        self.board.insert_piece(0, 0, 'S')
        self.board.insert_piece(1, 1, 'S')
        self.board.insert_piece(2, 2, 'O')
        self.board.insert_piece(3, 3, 'S')
        result = self.board.complete_SOS()
        self.assertTrue(result)

    def test_complete_diagonal_left_to_rigth(self):
        # Comprueba si exite un SOS en 3 casillas contiguas de  una diagonal que va de derecha a izquierda
        self.board.insert_piece(0, 3, 'S')
        self.board.insert_piece(1, 2, 'S')
        self.board.insert_piece(2, 1, 'O')
        self.board.insert_piece(3, 0, 'S')
        result = self.board.complete_SOS()
        self.assertTrue(result)


class TestWinOrTie(unittest.TestCase): #Ganado Empatado
    def setUp(self):
        self.board = Board(4)
    def test_empty_board(self):
        result = self.board.win_or_tie()
        self.assertEqual(result,'Empty Board')

    def test_board_complete_SOS_incomplete(self):
        # Tablero completo pero no existe un SOS
        #lleno el tablero de S
        for row in range(self.board.get_board_size()):
            for col in range(self.board.get_board_size()):
                self.board.insert_piece(row, col, 'S')

        result = self.board.win_or_tie()
        self.assertEqual(result,'Tie')

    def test_board_complete_SOS_complete(self):
        # Tablero completo si existe un SOS
        self.board.insert_piece(0, 0, 'S')
        self.board.insert_piece(1, 0, 'O')
        self.board.insert_piece(2, 0, 'S')
        self.board.insert_piece(3, 0, 'S')

        for row in range(self.board.get_board_size()):
            for col in range(1, self.board.get_board_size()):
                self.board.insert_piece(row, col, 'S')

        result = self.board.win_or_tie()
        self.assertEqual(result, 'Win')

    def test_board_incomplete_SOS_complete(self):
        self.board.insert_piece(0, 0, 'S')
        self.board.insert_piece(1, 0, 'O')
        self.board.insert_piece(2, 0, 'S')
        self.board.insert_piece(3, 0, 'S')

        result = self.board.win_or_tie()
        self.assertEqual(result, 'Win')

    def test_board_incomplete_SOS_incomplete(self):
        self.board.insert_piece(0, 0, 'S')

        result = self.board.win_or_tie()
        self.assertEqual(result, 'Continue')


if __name__ == '__main__':
    unittest.main()

