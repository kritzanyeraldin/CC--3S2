class board:
    # Definir las dimensiones del tablero y el tamaño de cada celda
    BOARD_SIZE = 3
    CELL_SIZE = 100

    # Crear el tablero
    board = [[None for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]