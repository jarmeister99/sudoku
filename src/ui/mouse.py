import pygame

from src.grid.board import Board
from src.util import CELL_SIZE


def get_hovered_cell(board: Board):
    """
    Return a cell that is being hovered
    :param board: The game board
    :return: The cell being hovered
    """
    mouse_pos = pygame.mouse.get_pos()
    row = (mouse_pos[1] // CELL_SIZE) + 1
    col = (mouse_pos[0] // CELL_SIZE) + 1
    if row <= 9 and col <= 9:
        return board.get_cell(row=row, col=col)
    else:
        return None


def mark_board(event, board: Board, selected_number: int):
    """

    :param event: A Pygame mouse listener event
    :param board: A board representing a Sudoku puzzle
    :param selected_number: The number with which to mark the board
    :return:
    """
    cell = get_hovered_cell(board=board)
    if cell and not cell.blocked:
        if event.button == 1:  # left click
            # clicked cell already has selected val
            if selected_number == cell.val:
                cell.unset()
            # clicked cell does NOT have selected val
            else:
                cell.set(val=selected_number)
                board.clear_house_notes(row=cell.row, col=cell.col, note=selected_number)
            board.update_house_validity(row=cell.row, col=cell.col)

        if event.button == 3:  # right click
            # clicked cell already have selected note
            if selected_number in cell.notes:
                cell.remove_note(note=selected_number)
            # clicked cell does NOT have selected note
            else:
                cell.add_note(note=selected_number)
