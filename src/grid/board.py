from collections import defaultdict

from src.grid.cell import Cell


class Board:
    def __init__(self):
        # holds cells
        self.grid = [[Cell(row=row, col=col) for col in range(1, 10)] for row in range(1, 10)]

    """
    --- Various Cell getters and setters ---
    We use these methods so that we can sideeffect the board when we act on cells
    For example, setting a cell may mark the cell and other cells as invalid based on board state
    Another example, setting a cell may clear the notes of other cells
    """

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Return the cell at the given position
        :param row: The row of the target cell
        :param col: The column of the target cell
        :return: The cell at the given position
        """
        Board.validate_pos(row, col)
        return self.grid[row - 1][col - 1]

    """
    --- Cell aggregators ---
    Functions to get all cells in a particular house
    """

    def get_cells_in_row(self, row: int) -> list:
        """
        Return a list of cells in the given row
        :param row: The row from which cells are returned
        :return: A list of cells in the given row
        """
        if not 1 <= row <= 9:
            raise ValueError
        return [self.grid[row - 1][i - 1] for i in range(1, 10)]

    def get_cells_in_col(self, col: int) -> list:
        """
        Return a list of cells in the given column
        :param col: The column from which cells are returned
        :return: A list of cells in the given column
        """
        if not 1 <= col <= 9:
            raise ValueError()
        return [self.grid[i - 1][col - 1] for i in range(1, 10)]

    # TODO: Make simpler. Use get_box_position code
    def get_cells_in_box(self, row: int, col: int) -> list:
        """
        Return a list of cells in a box
        :param row: The row of the box from which cells are returned
        :param col: The column of the box from which cells are returned
        :return: A list of cells in the given box
        """
        Board.validate_pos(row, col)
        box = []
        # move to top-left corner of box
        while row % 3 != 1:
            row -= 1
        while col % 3 != 1:
            col -= 1
        while True:
            # if we are at a row boundary and a column boundary
            if row % 3 == 0 and col % 3 == 0:
                # return all the cells we have seen
                return box
            cell = self.get_cell(row=row, col=col)
            # copy cell if it has a value
            if cell.val:
                box.append(cell)
            # if we are at a row boundary
            # .. move to next row
            if col % 3 == 0:
                row += 1
                col -= 2
            # otherwise, simply move across row
            else:
                col += 1

    """
    --- Cell group modifiers ---
    Functions that act on a group of cells
    """

    def wipe(self) -> None:
        """
        Reset game state to blank state
        :return: None
        """
        self.grid = [[Cell for _ in range(9)] for _ in range(9)]

    def reset(self) -> None:
        """
        Reset all cells and notes that are not currently blocked
        :return: None
        """
        for row in self.grid:
            for cell in row:
                if not cell.blocked:
                    cell.reset()

    @staticmethod
    def validate_pos(row: int, col: int):
        """
        Raise ValueError if given cell is invalid
        :param row: Row of cell to test
        :param col: Column of cell to test
        :return: None
        """
        if not 1 <= row <= 9:
            raise ValueError()
        if not 1 <= col <= 9:
            raise ValueError()

    def update_house_validity(self, row: int, col: int):
        """
        Mark house members as invalid or valid
        :param row: The row of the target house
        :param col: The col of the target house
        :return: None
        """
        row_cells = self.get_cells_in_row(row=row)
        col_cells = self.get_cells_in_col(col=col)
        box_cells = self.get_cells_in_box(row=row, col=col)

        marked = []
        for group in [row_cells, col_cells, box_cells]:
            seen = []
            bad_numbers = []
            for cell in group:
                # if we have seen this value in this col
                if cell.val in seen:
                    # mark number as bad
                    bad_numbers.append(cell.val)
                elif cell.val:
                    # mark number as seen
                    seen.append(cell.val)
            for cell in group:
                # the col contained a duplicate
                if cell.val in bad_numbers:
                    cell.valid = False
                    marked.append(cell)
                elif cell not in marked:
                    cell.valid = True


