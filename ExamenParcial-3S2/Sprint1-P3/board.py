class board:
    def __init__(self):
        self.tamaño = None
        self.tablero = None

    def insertTamaño(self, tamaño):
        if self.tamañoValido(tamaño):
            self.tamaño=tamaño
    def tamañoValido(self,n):
        if n <3:
            return False
        return True

    def crear_tablero_vacio(self):
        self.tablero = [[None for i in range(self.tamaño)] for j in
                      range(self.tamaño)]

    def insert_pieza(self, fila, col, pieza):
        # Validación del rango de las coordenadas
        if not (0 <= fila < self.tamaño) or not (0 <= col < self.tamaño):
            return 'Coordenadas fuera del rango del tablero'

        # Validación del tipo de dato de la pieza
        if not isinstance(pieza, str):
            return 'La pieza debe ser de tipo string'

        # Validación de valores válidos para la pieza
        valid_piezas = ['S', 'O']

        if pieza not in valid_piezas:
            return 'Pieza no valida'

        if not (self.obtener_pieza(fila, col) == None):
            return 'Casilla ocupada'

        # Asignación de la pieza al tablero
        self.tablero[fila][col] = pieza

    def obtener_pieza(self, fila, col):
        return self.tablero[fila][col]


