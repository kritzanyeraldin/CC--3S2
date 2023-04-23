import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width = 600
height = 400

# Crear una instancia de la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SOS")

# Tamaño del tablero y dimension de cada celda
BOARD_SIZE = 3
CELL_SIZE = 100

# Crear el tablero
board = [[None for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

#colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Función para dibujar el tablero en la pantalla
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = pygame.Rect(col * CELL_SIZE + (400 - BOARD_SIZE * CELL_SIZE), row * CELL_SIZE + (350 - BOARD_SIZE * CELL_SIZE),
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 2)


# Ejecutar el bucle principal del juego
runing=True
while runing:
    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing=False

    draw_board()

    # Actualizar la pantalla
    pygame.display.update()

pygame.quit()