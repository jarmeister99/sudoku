import unittest

from src.grid.board import Board


class BoardAccess(unittest.TestCase):
    def test_get_board(self):
        board = Board.get_board()
        self.assertEqual(9, len(board))
        for row in board:
            self.assertEqual(9, len(row))


if __name__ == '__main__':
    unittest.main()
