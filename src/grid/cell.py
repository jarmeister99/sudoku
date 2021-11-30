class Cell:
    def __init__(self, row: int, col: int, val: int = None):
        self.val = val
        self.notes = []
        self.row, self.col = row, col
        self.valid = True
        self.blocked = False
        self.forbidden = False

    def add_note(self, note: int) -> None:
        """
        Add the given note to the cell and sort
        :param note: The note to add to the cell
        :return: None
        """
        self.notes.append(note)
        self.notes.sort()

    def remove_note(self, note: int) -> None:
        """
        Remove the given note from the cell
        :param note: The note to remove from the cell
        :return: None
        """
        self.notes.remove(note)

    def reset(self) -> None:
        """
        Reset the cell to its default state
        :return: None
        """
        self.val = None
        self.notes = []
        self.blocked = False
        self.forbidden = False

    def unset(self) -> None:
        """
        Remove value and notes from cell
        :return: None
        """
        self.val = None
        self.notes = []

    def set(self, val: int) -> None:
        """
        Remove value and notes from cell
        :param val: The value to assign to the cell
        :return: None
        """
        self.val = val
        self.notes = []

