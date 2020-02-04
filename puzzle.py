from random import shuffle

from board import Board


def puzzle_full(board):
    for row in board.grid:
        for cell in row:
            if cell == '0':
                return False
    return True


def fill_puzzle(board):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(numbers)
    for i in range(81):
        row = (i // 9) + 1
        col = (i % 9) + 1
        if board.get_cell(row, col) == '0':
            for val in numbers:
                if str(val) not in board.get_row(row) \
                        and str(val) not in board.get_col(col) \
                        and str(val) not in board.get_box(row, col):
                    board.set_cell(row, col, val)
                    break
                else:
                    fill_puzzle(board)
            if puzzle_full(board):
                return


if __name__ == '__main__':
    board = Board()
    fill_puzzle(board)
    Board.display_board(board)
