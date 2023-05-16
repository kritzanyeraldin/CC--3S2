from board import Board
import unittest


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def tamaño_valido(self):
        self.assertEqual(self.board.tamañoValido, True)


if __name__ == '__main__':
    unittest.main()
