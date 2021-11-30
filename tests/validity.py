import unittest

from src.grid.board import Board


class Validity(unittest.TestCase):
    # Test a board with one filled cell
    def test_row_1(self):
        board = Board.get_board()
        board[0][0] = '1'
        self.assertTrue(board.row_valid(0))

    # Test a board with two filled identical cells on different rows and boxes
    def test_row_2(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[4][0] = '1'
        self.assertTrue(board.row_valid(0) and board.row_valid(4))

    # Test a board with two filled identical cells on different rows but the same box
    def test_row_3(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[1][0] = '1'
        self.assertFalse(board.row_valid(0) or board.row_valid(1))

    # Test a board with two filled identical cells on the same row but different boxes
    def test_row_4(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[0][4] = '1'
        self.assertFalse(board.row_valid(0))

    # Test a board with two filled identical cells on the same row and box
    def test_row_5(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[0][1] = '1'
        self.assertFalse(board.row_valid(0))

    # Test a board with one filled identical cell
    def test_col_1(self):
        board = Board.get_board()
        board[0][0] = '1'
        self.assertFalse(board.col_valid(0))

    # Test a board with two filled identical cells on different columns and boxes
    def test_col_2(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[0][4] = '1'
        self.assertTrue(board.col_valid(0) or board.col_valid(4))

    # Test a board with two filled identical cells on different columns but the same box
    def test_col_3(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[0][1] = '1'
        self.assertFalse(board.col_valid(0) or board.col_valid(1))

    # Test a board with two filled identical cells on the same column but different boxes
    def test_col_4(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[4][0] = '1'
        self.assertFalse(board.col_valid(0))

    # Test a board with two filled identical cells on the same column and box
    def test_col_5(self):
        board = Board.get_board()
        board[0][0] = '1'
        board[1][0] = '1'
        self.assertFalse(board.col_valid(0))


if __name__ == '__main__':
    unittest.main()
