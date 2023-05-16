from board import Board
import unittest


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_tamaño_Valido(self):
        n=2
        self.assertEqual(self.board.tamañoValido(n), False)

    def test_tablero_vacio(self):

        # Creamos un tablero 3x3 y verificamos si esta vacia cada casilla
        self.board.insertTamaño(3)
        self.board.crear_tablero_vacio()

        # Verifica si cada casilla esta vacia para un tablero vacio
        for i in range(self.board.tamaño):
            for j in range(self.board.tamaño):
                self.assertEqual(self.board.tablero[i][j], None)

    def test_insertar_pieza_valida_casilla_valida(self):
        # Insertar una pieza valida en una posicion valida
        fila = 0
        col = 0
        pieza = 'O'
        resultado=self.board.insertar_pieza(fila, col, pieza)
        self.assertEqual(resultado, 'Coordenadas fuera del rango del tablero')
        self.assertIsNone(self.board.obtener_piece(fila, col))

    def test_insertar_pieza_valida_coordenadas_invalidas




if __name__ == '__main__':
    unittest.main()
