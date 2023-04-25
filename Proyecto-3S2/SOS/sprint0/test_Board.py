from unittest import TestCase
from Board import Board
import random
import unittest


class TestBoard(TestCase):
    def test_empty_board(self):
        board_size = random.randint(3, 100)
        board = Board(board_size)

        # Verificamos si el tablero tiene tamaño n en cada dimension
        self.assertEqual(len(board.board), board_size)
        self.assertEqual(len(board.board[0]), board_size)
        self.assertEqual(len(board.board[1]), board_size)
        self.assertEqual(len(board.board[2]), board_size)

        # Verifica si cada casilla esta vacia para un tablero vacio
        for i in range(board.board_size):
            for j in range(board.board_size):
                self.assertEqual(board.board[i][j], None)


if __name__ == '__main__':
    unittest.main()
