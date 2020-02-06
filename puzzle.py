from random import shuffle


def generate(board):
    """

    :param board: An empty board representing an empty Sudoku puzzle
    :return: A board representing a playable Sudoku puzzle
    """
    board.wipe()
    vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    shuffle(vals)
    board.grid[0] = vals
    solve(board)


def solve(board):
    """

    :param board: A board representing an unsolved Sudoku puzzle
    :return: The solved input board
    """
    # Base case: no empty spaces
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    # --------------------------
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(vals)
    for val in vals:
        if valid(board, row, col, val):
            board.set_cell(row, col, val)
            if solve(board):
                # Base case: no empty spaces
                return True
            # Unset the cell
            board.set_cell(row, col, 0)
            # ... continue the loop, checking the next value in the range
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
    return str(val) not in board.get_row(row) and \
           str(val) not in board.get_col(col) and \
           str(val) not in board.get_box(row, col)
