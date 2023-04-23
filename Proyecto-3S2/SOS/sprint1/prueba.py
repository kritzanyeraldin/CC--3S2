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




# Ejecutar el bucle principal del juego
runing=True
while runing:
    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing=False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(pygame.mouse.get_pos())



    # Actualizar la pantalla
    pygame.display.update()

pygame.quit()