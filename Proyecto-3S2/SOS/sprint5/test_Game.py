from unittest import TestCase
from Game import SimpleGame, GeneralGame
from Board import Board

class TestSimpleGame(TestCase):
    def setUp(self):
        self.game=SimpleGame(Board(3))
        self.board=self.game.get_board()
    def test_take_turn_empty_board(self):
        result=self.game.take_turn('red',0,0)
        self.assertEqual(('Empty Board','red'),result)

    def test_take_turn_continue(self):
        # Inicia el juego
        self.board.insert_piece(0, 0, 'S', 'red')
        result = self.game.take_turn('red', 0, 0)
        self.assertEqual(('Continue', 'blue'), result)

    def test_take_turn_win(self):
        self.board.insert_piece(0, 0, 'S', 'red')
        self.board.insert_piece(0, 1, 'O', 'blue')
        self.board.insert_piece(0, 2, 'S', 'red')
        result = self.game.take_turn('red', 0, 2)
        self.assertEqual(('Win', 'red'), result)

    def test_take_turn_Tie(self):
        self.board.insert_piece(0, 0, 'S', 'red')
        self.board.insert_piece(0, 1, 'S', 'blue')
        self.board.insert_piece(0, 2, 'S', 'red')
        self.board.insert_piece(1, 0, 'S', 'red')
        self.board.insert_piece(1, 1, 'S', 'blue')
        self.board.insert_piece(1, 2, 'S', 'red')
        self.board.insert_piece(2, 0, 'S', 'red')
        self.board.insert_piece(2, 1, 'S', 'blue')
        self.board.insert_piece(2, 2, 'S', 'red')
        result = self.game.take_turn('red', 2, 2)
        self.assertEqual(('Tie', 'None'), result)


class TestGeneralGame(TestCase):
    def setUp(self):
        self.game = GeneralGame(Board(3))
        self.board = self.game.get_board()
    def test_take_turn_continue(self):
        # Inicia el juego
        self.board.insert_piece(0, 0, 'S', 'red')
        self.game.take_turn('red', 0, 0)
        self.board.insert_piece(0, 1, 'O', 'blue')
        self.game.take_turn('blue', 0, 1)
        self.board.insert_piece(0, 2, 'S', 'red')
        result = self.game.take_turn('red', 0, 2)
        self.assertEqual(('Continue', 'red'), result)

    def test_take_turn_win(self):
        self.board.insert_piece(0, 0, 'S', 'red')
        self.game.take_turn('red', 0, 0)
        self.board.insert_piece(0, 1, 'O', 'blue')
        self.game.take_turn('blue', 0, 1)
        self.board.insert_piece(0, 2, 'S', 'red')
        self.game.take_turn('red', 0, 2)
        self.board.insert_piece(1, 0, 'S', 'red')
        self.game.take_turn('red', 1, 0)
        self.board.insert_piece(1, 1, 'O', 'blue')
        self.game.take_turn('blue', 1,1)
        self.board.insert_piece(1, 2, 'S', 'red')
        self.game.take_turn('red', 1,2)
        self.board.insert_piece(2, 0, 'S', 'red')
        self.game.take_turn('red', 2, 0)
        self.board.insert_piece(2, 1, 'O', 'blue')
        self.game.take_turn('blue', 2, 1)
        self.board.insert_piece(2, 2, 'S', 'red')
        self.game.take_turn('red', 2, 2)

        result = self.game.take_turn('red', 2, 2)
        self.assertEqual(('Win', 'red'), result)

    def test_take_turn_Tie(self):
        self.board.insert_piece(0, 0, 'S', 'red')
        self.game.take_turn('red', 0, 0)
        self.board.insert_piece(0, 1, 'S', 'blue')
        self.game.take_turn('blue', 0, 1)
        self.board.insert_piece(0, 2, 'S', 'red')
        self.game.take_turn('red', 0, 2)
        self.board.insert_piece(1, 0, 'S', 'red')
        self.game.take_turn('red', 1, 0)
        self.board.insert_piece(1, 1, 'S', 'blue')
        self.game.take_turn('blue', 1, 1)
        self.board.insert_piece(1, 2, 'S', 'red')
        self.game.take_turn('red', 1, 2)
        self.board.insert_piece(2, 0, 'S', 'red')
        self.game.take_turn('red', 2, 0)
        self.board.insert_piece(2, 1, 'S', 'blue')
        self.game.take_turn('blue', 2, 1)
        self.board.insert_piece(2, 2, 'S', 'red')
        self.game.take_turn('red', 2, 2)
        result = self.game.take_turn('red', 2, 2)
        self.assertEqual(('Tie', 'None'), result)

