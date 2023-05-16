from board import board
import unittest


class Testboard(unittest.TestCase):

    def setUp(self):
        self.board = board()

    def test_tamaño_Valido(self):
        n=2
        self.assertEqual(self.board.tamañoValido(n), False)

    def test_board_vacio(self):

        # Creamos un board 3x3 y verificamos si esta vacia cada casilla
        self.board.insertTamaño(3)
        self.board.crear_tablero_vacio()

        # Verifica si cada casilla esta vacia para un board vacio
        for i in range(self.board.tamaño):
            for j in range(self.board.tamaño):
                self.assertEqual(self.board.tablero[i][j], None)

    def test_insertar_pieza_valida_casilla_invalida(self):
        # Creamos un board 3x3 y verificamos si esta vacia cada casilla
        self.board.insertTamaño(3)
        self.board.crear_tablero_vacio()

        # Insertar una pieza valida en una posicion valida
        fila = 3
        col = 2
        pieza = 'O'
        resultado=self.board.insert_pieza(fila, col, pieza)
        self.assertEqual(resultado, 'Coordenadas fuera del rango del tablero')


    def test_insertar_pieza_invalida_no_string(self):
        # Creamos un board 3x3 y verificamos si esta vacia cada casilla
        self.board.insertTamaño(3)
        self.board.crear_tablero_vacio()
        # Insertar una pieza de tipo invalido
        fila = 0
        col = 0
        pieza = 4
        resultado = self.board.insert_pieza(fila, col, pieza)
        self.assertEqual(resultado, 'La pieza debe ser de tipo string')
        self.assertIsNone(self.board.obtener_pieza(fila, col))
        
    def test_isnertar_piezaz_invalida_pieza_cualquier_string(self):
        # Creamos un board 3x3 y verificamos si esta vacia cada casilla
        self.board.insertTamaño(3)
        self.board.crear_tablero_vacio()

        # Insertar una pieza con un valor invalido
        fila = 0
        col = 0
        pieza = 'W'
        resultado = self.board.insert_pieza(fila, col, pieza)
        self.assertEqual(resultado, 'Pieza no valida')
        self.assertIsNone(self.board.obtener_pieza(fila, col))
        
    def test_insertar_pieza_valida_casilla_ocupada(self):
        # Creamos un board 3x3 y verificamos si esta vacia cada casilla
        self.board.insertTamaño(3)
        self.board.crear_tablero_vacio()

        # Insertar una pieza valida en una casilla ocupada
        fila = 0
        col = 0
        pieza = 'S'
        # Insertamos una pieza en (0,0)
        self.board.insert_pieza(fila, col, pieza)
        # Volvemos a insertar otra pieza en (0,0)
        resultado = self.board.insert_pieza(fila, col, pieza)
        self.assertEqual(resultado, 'Casilla ocupada')



if __name__ == '__main__':
    unittest.main()
