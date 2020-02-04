import pygame

from util import CELL_SIZE


def get_hovered_cell():
    mouse_pos = pygame.mouse.get_pos()
    row = (mouse_pos[1] // CELL_SIZE) + 1
    col = (mouse_pos[0] // CELL_SIZE) + 1
    if row <= 9 and col <= 9:
        return row, col
    else:
        return None


def mark_board(event, board, selected_number):
    sel = get_hovered_cell()
    if not sel:
        return
    if event.button == 1:  # Left click
        if selected_number == board.get_cell(sel[0], sel[1]):
            board.unset_cell(row=sel[0], col=sel[1])
        else:
            board.set_cell(row=sel[0], col=sel[1], val=int(selected_number))
            board.clear_cell_notes(row=sel[0], col=sel[1])
    if event.button == 3:  # Right click
        if selected_number in board.get_cell_notes(sel[0], sel[1]):
            board.unnote_cell(row=sel[0], col=sel[1], note=int(selected_number))
        else:
            board.note_cell(row=sel[0], col=sel[1], note=int(selected_number))
