from random import shuffle, randint, seed
from copy import deepcopy

from src.grid.board import Board
from src.grid.cell import Cell


def generate(board):
    """
    :param board: An empty board representing an empty Sudoku puzzle
    :param num_remove: The number of cells that should be empty
    :return: A board representing a playable Sudoku puzzle
    """
    board.wipe()  # reset board

    # create randomized first row of cells
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(vals)
    first_row = []
    for i, val in enumerate(vals):
        first_row.append(Cell(row=1, col=i + 1, val=val))
    board.grid[0] = first_row
    solve(board=board)


def check_uniqueness(board: Board):
    """

    :param board: A board representing a playable Sudoku puzzle
    :return: A boolean representing whether the puzzle has only one unique solution
    """
    copy_1 = deepcopy(board)
    copy_2 = deepcopy(board)
    solve(copy_1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    solve(copy_2, [9, 8, 7, 6, 5, 4, 3, 2, 1])
    return copy_1.grid == copy_2.grid


def solve(board: Board) -> None or bool:
    """

    :param board: A board representing a playable Sudoku puzzle
    :param vals: An ordered list representing the sequence of values to check in the backtracking algorithm
    :return: None
    """
    # base case: we are out of empty slots
    if not (cell := find_empty(board=board)):
        return True
    for num in range(1, 10):
        if not board.is_val_in_house(row=cell.row, col=cell.col, val=num):
            cell.set(val=num)
            # return if success
            if solve(board=board):
                return True
            # unmake and try again if fail
            cell.set(val=None)
    # trigger backtracking
    return False


def find_empty(board: Board) -> Cell or None:
    """
    Return the first empty cell
    :param board: A board representing a Sudoku puzzle
    :return: The first empty cell
    """
    for row in board.grid:
        for cell in row:
            if not cell.val:
                return cell
    return None
