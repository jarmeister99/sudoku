from random import shuffle, randint
from copy import deepcopy


def generate(board, num_remove):
    """

    :param board: An empty board representing an empty Sudoku puzzle
    :param num_remove: The number of cells that should be empty
    :return: A board representing a playable Sudoku puzzle
    """
    board.wipe()
    vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    shuffle(vals)
    board.grid[0] = vals
    solve(board, [int(val) for val in vals])

    # TODO: Make this more efficient
    while True:
        board_copy = deepcopy(board)
        if generate_attempt(board_copy, num_remove):
            board.grid = board_copy.grid
            board.set_blocked_cells()
            break


def generate_attempt(board, num_remove):
    """

    :param board: A full board representing a completed Sudoku puzzle
    :param num_remove: The number of cells that should be empty
    :return: A boolean representing whether the board has only one unique solution
    """
    for i in range(num_remove):
        row = randint(1, 9)
        col = randint(1, 9)
        while board.get_cell(row, col) == '0':
            row = randint(1, 9)
            col = randint(1, 9)
        board.set_cell(row, col, 0)
    return check_uniqueness(board)


def check_uniqueness(board):
    """

    :param board: A board representing a playable Sudoku puzzle
    :return: A boolean representing whether the puzzle has only one unique solution
    """
    copy_1 = deepcopy(board)
    copy_2 = deepcopy(board)
    solve(copy_1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    solve(copy_2, [9, 8, 7, 6, 5, 4, 3, 2, 1])
    return copy_1.grid == copy_2.grid


def solve(board, vals):
    """

    :param board: A board representing a playable Sudoku puzzle
    :param vals: An ordered list representing the sequence of values to check in the backtracking algorithm
    :return: The solved input board
    """

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for val in vals:
        if valid(board, row, col, val):
            board.set_cell(row, col, val)
            if solve(board, vals):
                return True
            board.set_cell(row, col, 0)
    return False


def find_empty(board):
    """

    :param board: A board representing a Sudoku puzzle
    :return: The location of an empty cell in the board in the form (row, col). Returns None if no empty cells exist.
    """
    for row_i, row in enumerate(board.grid):
        for col_i, col in enumerate(row):
            if board.get_cell(row_i + 1, col_i + 1) == '0':
                return row_i + 1, col_i + 1
    return None


def valid(board, row, col, val):
    """

    :param board: A board representing a Sudoku puzzle
    :param row: The row of the cell to check
    :param col: The column of the cell to check
    :param val: The value to be potentially placed in the selected cell
    :return: A boolean indicating whether the value can be placed in the selected cell according to Sudoku's constraints
    """
    return str(val) not in board.get_row_values(row) and \
           str(val) not in board.get_col_values(col) and \
           str(val) not in board.get_box_values(row, col)
