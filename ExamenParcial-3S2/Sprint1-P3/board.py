class Board:
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

