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


def mark_board(event, board, selected_number, blocked_cells):
    """

    :param event: A Pygame mouse listener event
    :param board: A board representing a Sudoku puzzle
    :param selected_number: The number with which to mark the board
    :param blocked_cells: A list of positions representing cells that may not be marked
    :return:
    """
    sel = get_hovered_cell()
    if not sel:
        return
    if sel not in blocked_cells:
        # Left click
        if event.button == 1:
            # If the selected number already occupies the cell chosen
            if selected_number == board.get_cell(sel[0], sel[1]):
                board.unset_cell(row=sel[0], col=sel[1])
                return (sel[1], sel[0]), False
            # If the selected number does not occupy the cell chosen
            else:
                board.set_cell(row=sel[0], col=sel[1], val=int(selected_number))
                board.update_notes(sel[0], sel[1], int(selected_number))
                return (sel[1], sel[0]), True
        # Right click
        if event.button == 3:
            # If the selected number is already noted in the cell chosen
            if selected_number in board.get_cell_notes(sel[0], sel[1]):
                board.unnote_cell(row=sel[0], col=sel[1], note=int(selected_number))
            # If the selected number is not already noted in the cell chosen
            else:
                board.note_cell(row=sel[0], col=sel[1], note=int(selected_number))
