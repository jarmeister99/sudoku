class Board:
    def __init__(self):
        self.grid = [['0' for j in range(9)] for i in range(9)]
        self.notes = [[[] for j in range(9)] for i in range(9)]
        self.blocked_cells = []

    def get_cell(self, row, col):
        Board.validate_pos(row, col)
        return self.grid[row - 1][col - 1]

    def get_cell_notes(self, row, col):
        Board.validate_pos(row, col)
        return self.notes[row - 1][col - 1]

    def set_cell(self, row, col, val):
        Board.validate_pos(row, col)
        if not 0 <= val <= 9:
            raise ValueError()
        self.grid[row - 1][col - 1] = str(val)

    def unset_cell(self, row, col):
        Board.validate_pos(row, col)
        self.grid[row - 1][col - 1] = '0'

    def note_cell(self, row, col, note):
        Board.validate_pos(row, col)
        if not 0 <= note <= 9:
            raise ValueError()
        self.notes[row - 1][col - 1].append(str(note))
        self.notes[row - 1][col - 1].sort()

    def unnote_cell(self, row, col, note):
        Board.validate_pos(row, col)
        if not 0 <= note <= 9:
            raise ValueError()
        if str(note) in self.notes[row - 1][col - 1]:
            self.notes[row - 1][col - 1].remove(str(note))
            self.notes[row - 1][col - 1].sort()

    def clear_cell_notes(self, row, col):
        Board.validate_pos(row, col)
        self.notes[row - 1][col - 1] = []

    def update_notes(self, row, col, val):
        """

        :param row: An index representing the row for which notes should be updated
        :param col: An index representing the col for which notes should be updated
        :param val: The value to remove from appropriate cell notes
        :return: Removes the input value from appropriate cell notes, centered on the input cell
        """
        for pos in Board.get_row_positions(row) + Board.get_col_positions(col) + Board.get_box_positions(row, col):
            self.unnote_cell(pos[0], pos[1], val)

    def wipe(self):
        self.grid = [['0' for j in range(9)] for i in range(9)]
        self.notes = [[[] for j in range(9)] for i in range(9)]
        self.blocked_cells = []

    def reset(self):
        for row_i, row in enumerate(self.grid):
            for col_i, col in enumerate(row):
                if (row_i + 1, col_i + 1) not in self.blocked_cells:
                    self.set_cell(row_i + 1, col_i + 1, 0)
                    self.clear_cell_notes(row_i + 1, col_i + 1)

    @staticmethod
    def display_board(board):
        for row in board.grid:
            print(' '.join(str(cell) for cell in row))

    @staticmethod
    def display_notes(board, row, col):
        Board.validate_pos(row, col)
        for notes in board.notes[row - 1][col - 1]:
            print(f'{notes}', end=' ')

    @staticmethod
    def validate_pos(row, col):
        if not 1 <= row <= 9:
            raise ValueError()
        if not 1 <= col <= 9:
            raise ValueError()

    def validate(self):
        return not self.get_invalid_rows() and \
               not self.get_invalid_cols() and \
               not self.get_invalid_boxes()

    def cell_invalid(self, row, col):
        """

        :param row: An index representing the row of the cell to validate
        :param col: An index representing the col of the cell to validate
        :return: A boolean representing   whether the cell has a legal value within
        """
        to_check = Board.get_row_positions(row) + Board.get_col_positions(col) + Board.get_box_positions(row, col)
        to_check = list(filter(lambda a: a != (row, col), to_check))
        for pos in to_check:
            if self.get_cell(row, col) == self.get_cell(pos[0], pos[1]):
                return True
        return False

    def get_invalid_rows(self):
        invalid_rows = []
        for row_i in range(9):
            if len(set(self.get_row_values(row_i + 1))) != len(self.get_row_values(row_i + 1)):
                invalid_rows.append(row_i + 1)
        return invalid_rows

    def get_invalid_cols(self):
        invalid_cols = []
        for col_i in range(9):
            if len(set(self.get_col_values(col_i + 1))) != len(self.get_col_values(col_i + 1)):
                invalid_cols.append(col_i + 1)
        return invalid_cols

    def get_invalid_boxes(self):
        invalid_boxes = []
        box = 1
        row = 1
        col = 1
        while True:
            if box == 9 and row % 3 == 0 and col % 3 == 0:
                return invalid_boxes
            elif row % 3 == 0 and col % 3 == 0:
                box += 1
                if col == 9:
                    row += 1
                    col -= 8
                else:
                    row -= 2
                    col += 1
            if len(set(self.get_box_values(row, col))) != len(
                    self.get_box_values(row, col)) and box not in invalid_boxes:
                invalid_boxes.append(box)
            if col % 3 == 0:
                row += 1
                col -= 2
            else:
                col += 1

    def get_row_values(self, row):
        if not 1 <= row <= 9:
            raise ValueError()
        return list(filter(lambda element: element != '0', self.grid[row - 1]))

    @staticmethod
    def get_row_positions(row):
        """

        :param row: An index representing the row to grab cell positions from
        :return: A list of tuples (row, col) representing cell positions of the row
        """
        if not 1 <= row <= 9:
            raise ValueError()
        return [(row, i) for i in range(1, 10)]

    @staticmethod
    def get_col_positions(col):
        """

        :param col: An index representing the col to grab cell positions from
        :return: A list of tuples (row, col) representing cell positions of the col
        """
        if not 1 <= col <= 9:
            raise ValueError()
        return [(i, col) for i in range(1, 10)]

    @staticmethod
    def get_box_positions(row, col):
        """

        :param row: An index representing the col of the box to grab cell positions from
        :param col: An index representing the row of the box to grab cell positions from
        :return: A list of tuples (row, col) representing cell positions of the box
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

    def get_col_values(self, col):
        if not 1 <= col <= 9:
            raise ValueError()
        column = []
        for row in self.grid:
            column.append(row[col - 1])
        return list(filter(lambda element: element != '0', column))

    # TODO: Make simpler. Use get_box_position code
    def get_box_values(self, row, col):
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

    def load_test_board(self):
        self.grid = [
            ['0', '0', '0', '2', '6', '0', '7', '0', '1'],
            ['6', '8', '0', '0', '7', '0', '0', '9', '0'],
            ['1', '9', '0', '0', '0', '4', '5', '0', '0'],
            ['8', '2', '0', '1', '0', '0', '0', '4', '0'],
            ['0', '0', '4', '6', '0', '2', '9', '0', '0'],
            ['0', '5', '0', '0', '0', '3', '0', '2', '8'],
            ['0', '0', '9', '3', '0', '0', '0', '7', '4'],
            ['0', '4', '0', '0', '5', '0', '0', '3', '6'],
            ['7', '0', '3', '0', '1', '8', '0', '0', '0']
        ]
        self.set_blocked_cells()

    def set_blocked_cells(self):
        for row_i, row in enumerate(self.grid):
            for col_i, col in enumerate(row):
                if self.get_cell(row_i + 1, col_i + 1) != '0':
                    self.blocked_cells.append((row_i + 1, col_i + 1))
