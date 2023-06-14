import unittest
from unittest import TestCase
from computer import Computer
from Game import SimpleGame, GeneralGame
from Board import Board
class TestComputer(TestCase):
    def setUp(self):
        self.board=Board(3)
    def test_move_simple_game(self):
        computer=Computer(SimpleGame(self.board))

        self.board.insert_piece(0, 0, 'S', 'red')
        self.board.insert_piece(0,1,'O','blue')
        computer.move('blue')
        piece = computer.get_piece()
        row,col = computer.get_cells()
        self.assertEqual(piece,'S')
        self.assertEqual((row,col),(0,2))

    def test_move_general_game(self):
        computer = Computer(GeneralGame(self.board))
        self.board.insert_piece(0, 0, 'S', 'red')
        self.board.insert_piece(0, 1, 'O', 'blue')
        computer.move('blue')
        piece = computer.get_piece()
        row, col = computer.get_cells()
        self.assertEqual(piece, 'S')
        self.assertEqual((row, col), (0, 2))

if __name__ == '__main__':
    unittest.main()