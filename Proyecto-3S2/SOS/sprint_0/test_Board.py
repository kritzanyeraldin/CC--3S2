import unittest
from unittest import TestCase
from Board import Board


class TestBoard(TestCase):
    def test_board_empty(self):
        board = Board()

        # Verificamos si el tablero tiene tamaño 3 en cada dimension
        self.assertEqual(len(board.board), 3)
        self.assertEqual(len(board.board[0]), 3)
        self.assertEqual(len(board.board[1]), 3)
        self.assertEqual(len(board.board[2]), 3)

        # Verifica si cada casilla esta vacia para un tablero vacio
        for i in range(board.board_size):
            for j in range(board.board_size):
                self.assertEqual(board.board[i][j], None)


if __name__ == '__main__':
    unittest.main()
