class Board:
    def __init__(self):
        # holds cells and their values
        self.grid = [['0' for _ in range(9)] for _ in range(9)]

        # holds cells and their notes
        self.notes = [[[] for _ in range(9)] for _ in range(9)]

        self.blocked_cells = []
        self.forbidden_cells = []

    def get_cell(self, row: int, col: int) -> str:
        """
        Return the value of the cell at the given position
        :param row: The row of the target cell
        :param col: The column of the target cell
        :return: The value of the cell at the given position
        """
        Board.validate_pos(row, col)
        return self.grid[row - 1][col - 1]

    def get_cell_notes(self, row, col) -> list:
        """
        Returns a list of notes attached to the cell at the given position
        :param row: The row of the target cell
        :param col: The column of the target cell
        :return: The list of notes attached to the cell at the given position
        """
        Board.validate_pos(row, col)
        return self.notes[row - 1][col - 1]

    def set_cell(self, row: int, col: int, val: int) -> None:
        """
        Set the cell at the given position to a particular value
        :param row: The row of the target cell
        :param col: The column of the target cell
        :param val: The value to assign to the target cell
        :return: None
        """
        Board.validate_pos(row, col)
        # validate value
        if not 0 <= val <= 9:
            raise ValueError()
        self.grid[row - 1][col - 1] = str(val)

    def unset_cell(self, row: int, col: int) -> None:
        """
        Clear the cell at the given position
        :param row: The row of the target cell
        :param col: The column of the target cell
        :return: None
        """
        Board.validate_pos(row, col)
        self.grid[row - 1][col - 1] = '0'

    def note_cell(self, row: int, col: int, note: int) -> None:
        """
        Add a note to the cell at the given position
        :param row: The row of the target cell
        :param col: The column of the target cell
        :param note: The note to add to the target cell
        :return: None
        """
        Board.validate_pos(row, col)
        # validate note
        if not 0 <= note <= 9:
            raise ValueError()
        self.notes[row - 1][col - 1].append(str(note))
        # keep notes in sorted order
        self.notes[row - 1][col - 1].sort()

    def unnote_cell(self, row: int, col: int, note: int) -> None:
        """
        Remove the given note from the cell at the given position
        :param row: The row of the target cell
        :param col: The column of the target cell
        :param note: The note to remove from the target cell
        :return: None
        """
        Board.validate_pos(row, col)
        # validate note
        if not 0 <= note <= 9:
            raise ValueError()
        # remove note if exists in notes
        if str(note) in self.notes[row - 1][col - 1]:
            self.notes[row - 1][col - 1].remove(str(note))
            self.notes[row - 1][col - 1].sort()

    def clear_cell_notes(self, row: int, col: int) -> None:
        """
        Remove all notes from the cell at the given position
        :param row: The row of the target cell
        :param col: The column of the target cell
        :return: None
        """
        Board.validate_pos(row, col)
        self.notes[row - 1][col - 1] = []

    def update_notes(self, row: int, col: int, val: int) -> None:
        """
        Update all houses affected by placing 'val' in the cell given by 'row, col'
        :param row: The row of the target cell
        :param col: The column of the target cell
        :param val: The value to remove from affected house cell notes
        :return: None
        """
        for pos in Board.get_row_positions(row) + Board.get_col_positions(col) + Board.get_box_positions(row, col):
            self.unnote_cell(pos[0], pos[1], val)

    def wipe(self) -> None:
        """
        Reset game state to blank state
        :return: None
        """
        self.grid = [['0' for _ in range(9)] for _ in range(9)]
        self.notes = [[[] for _ in range(9)] for _ in range(9)]
        self.blocked_cells = []
        self.forbidden_cells = []

    def reset(self) -> None:
        """
        Reset all cells and notes that are not currently blocked
        :return: None
        """
        for row_i, row in enumerate(self.grid):
            for col_i, col in enumerate(row):
                if (row_i + 1, col_i + 1) not in self.blocked_cells:
                    self.set_cell(row_i + 1, col_i + 1, 0)
                    self.clear_cell_notes(row_i + 1, col_i + 1)

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

    def cell_invalid(self, row: int, col: int):
        """
        Return whether the cell is allowed to have its value, based on neighbor houses
        :param row: Row of cell to test
        :param col: Col of cell to test
        :return: A boolean representing whether the cell is allowed to have its value, based on neighbor houses
        """
        # check every cell in every house
        to_check = Board.get_row_positions(row) + Board.get_col_positions(col) + Board.get_box_positions(row, col)
        # ... except for the target cell
        to_check = list(filter(lambda a: a != (row, col), to_check))
        for pos in to_check:
            # if a cell in the house has the same value as the target cell
            if self.get_cell(row, col) == self.get_cell(pos[0], pos[1]):
                # indicate cell is invalid
                return True
        # indicate cell is valid
        return False

    def get_row_values(self, row: int) -> list:
        """
        Return a list of values in a row
        :param row: The row to return values from
        :return: A list of values in a row
        """
        if not 1 <= row <= 9:
            raise ValueError()
        # only return set values
        return list(filter(lambda element: element != '0', self.grid[row - 1]))

    def get_col_values(self, col: int) -> list:
        """
        Return a list of values in a column
        :param col: The row to return values from
        :return: A list of values in a column
        """
        if not 1 <= col <= 9:
            raise ValueError()
        column = []
        for row in self.grid:
            column.append(row[col - 1])
        # only return set values
        return list(filter(lambda element: element != '0', column))

    # TODO: Make simpler. Use get_box_position code
    def get_box_values(self, row: int, col: int) -> list:
        """
        Return a list of values in a box
        :param row: The row of the box to return values from
        :param col: The column of the box to return values from
        :return: A list of values in the given box
        """
        Board.validate_pos(row, col)
        box = []
        while row % 3 != 1:
            row -= 1
        while col % 3 != 1:
            col -= 1
        while True:
            if row % 3 == 0 and col % 3 == 0:
                return box
            if self.grid[row - 1][col - 1].isdigit():
                box.append(self.grid[row - 1][col - 1])
            if col % 3 == 0:
                row += 1
                col -= 2
            else:
                col += 1

    @staticmethod
    def get_row_positions(row: int) -> list:
        """
        Return a list of cell positions (row, col) in the given row
        :param row: The row to return cell positions from
        :return: A list of cell positions (row, col) in the given row
        """
        if not 1 <= row <= 9:
            raise ValueError()
        return [(row, i) for i in range(1, 10)]

    @staticmethod
    def get_col_positions(col: int) -> list:
        """
        Return a list of cell positions (row, col) in the given column
        :param col: The column to return cell positions from
        :return: A list of cell positions (row, col) in the given column
        """
        if not 1 <= col <= 9:
            raise ValueError()
        return [(i, col) for i in range(1, 10)]

    @staticmethod
    def get_box_positions(row, col):
        """
        Return a list of cell positions (row, col) in the given box
        :param row: The row of the box to return cell positions from
        :param col: The column of the box to return cell positions from
        :return: A list of cell positions (row, col) in the given box
        """
        Board.validate_pos(row, col)
        positions = []
        if (col - 1) % 3 == 0:
            pass
        else:
            while (col - 1) % 3 != 0:
                col -= 1
        if (row - 1) % 3 == 0:
            pass
        else:
            while (row - 1) % 3 != 0:
                row -= 1
        positions += [(row, col + i) for i in range(3)]
        positions += [(row + 1, col + i) for i in range(3)]
        positions += [(row + 2, col + i) for i in range(3)]
        return positions

    def set_blocked_cells(self) -> None:
        """
        Add all non-zero cells to 'blocked cells' preventing the user from editing them
        :return: None
        """
        for row_i, row in enumerate(self.grid):
            for col_i, col in enumerate(row):
                if self.get_cell(row_i + 1, col_i + 1) != '0':
                    self.blocked_cells.append((row_i + 1, col_i + 1))

    # TODO: does this belong here? looks like a solver thing
    def set_forbidden(self, row: int, col: int) -> None:
        """
        Add the given cell to 'forbidden cells'
        :param row: The row of the targeted cell
        :param col: The column of the targeted cell
        :return: Add the targeted cell to 'forbidden cells'
        """
        self.forbidden_cells.append((row, col))

    # TODO: does this belong here? looks like a solver thing
    def is_forbidden(self, row, col) -> bool:
        """
        Return whether the given cell is in 'forbidden cells'
        :param row: The row of the targeted cell
        :param col: The column of the targeted cell
        :return: A boolean representing whether the input cell is forbidden
        """
        return (row, col) in self.forbidden_cells
