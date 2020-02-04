import pygame

from util import CELL_SIZE


def get_hovered_cell():
    mouse_pos = pygame.mouse.get_pos()
    row = (mouse_pos[1] // CELL_SIZE) + 1
    col = (mouse_pos[0] // CELL_SIZE) + 1
    return row, col
