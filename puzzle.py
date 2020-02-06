from random import shuffle

from board import Board


def puzzle_full(board):
    for row in board.grid:
        for cell in row:
            if cell == '0':
                return False
    return True


def fill_puzzle(board):
    pass


if __name__ == '__main__':
    board = Board()
    fill_puzzle(board)
    Board.display_board(board)
