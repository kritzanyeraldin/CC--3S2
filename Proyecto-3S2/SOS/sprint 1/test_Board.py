from unittest import TestCase
from Board import Board
import random
import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_size = random.randint(3, 100)
        self.board = Board(self.board_size)

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
        #Insertar una pieza valida en una posicion valida
        row = 0
        col = 0
        piece = 'O'
        result = self.board.insert_piece(row, col, piece)
        self.assertEqual(self.board.get_piece(row, col), 'O')

    def test_insert_piece_invalid_coordinates(self):
        # Insertar una pieza en una posicion invalida
        row = self.board_size
        col = self.board_size
        piece = 'S'
        result = self.board.insert_piece(row,col,piece)
        self.assertEqual(result, 'Coordenadas fuera del rango del tablero')
        self.assertIsNone(self.board.get_piece(row, col))

    def test_insert_piece_invalid_piece_type(self):
        # Insertar una pieza de tipo invalido
        row = 0
        col = 0
        piece = 4
        result = self.board.insert_piece(row, col, piece)
        self.assertEqual(result,'La pieza debe ser de tipo string')
        self.assertIsNone(self.board.get_piece(row,col))

    def test_insert_piece_invalid_piece_value(self):
        # Insertar una pieza con un valor invalido
        row = 0
        col = 0
        piece = 'W'
        result = self.board.insert_piece(row, col, piece)
        self.assertEqual(result, 'Pieza no valida')
        self.assertIsNone(self.board.get_piece(row, col))





if __name__ == '__main__':
    unittest.main()

