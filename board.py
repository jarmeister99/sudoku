class Board:
    def __init__(self):
        self.grid = [['~' for j in range(9)] for i in range(9)]
        self.notes = [[[] for j in range(9)] for i in range(9)]

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
        self.grid[row - 1][col - 1] = '~'

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
        self.notes[row - 1][col - 1].remove(str(note))
        self.notes[row - 1][col - 1].sort()

    def clear_cell_notes(self, row, col):
        Board.validate_pos(row, col)
        self.notes[row - 1][col - 1] = []

    def reset(self):
        self.clear_notes()
        self.clear_grid()

    def clear_notes(self):
        self.notes = [[[] for j in range(9)] for i in range(9)]

    def clear_grid(self):
        self.grid = [['~' for j in range(9)] for i in range(9)]

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

    def get_invalid_rows(self):
        invalid_rows = []
        for row_i in range(9):
            if len(set(self.get_row(row_i + 1))) != len(self.get_row(row_i + 1)):
                invalid_rows.append(row_i + 1)
        return invalid_rows

    def get_invalid_cols(self):
        invalid_cols = []
        for col_i in range(9):
            if len(set(self.get_col(col_i + 1))) != len(self.get_col(col_i + 1)):
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
            if len(set(self.get_box(row, col))) != len(self.get_box(row, col)) and box not in invalid_boxes:
                invalid_boxes.append(box)
            if col % 3 == 0:
                row += 1
                col -= 2
            else:
                col += 1

    def get_row(self, row):
        if not 1 <= row <= 9:
            raise ValueError()
        return list(filter(lambda element: element != '~', self.grid[row - 1]))

    def get_col(self, col):
        if not 1 <= col <= 9:
            raise ValueError()
        column = []
        for row in self.grid:
            column.append(row[col - 1])
        return list(filter(lambda element: element != '~', column))

    def get_box(self, row, col):
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
