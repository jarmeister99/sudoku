import pygame

from src.grid.board import Board
from src.util import Colors, CELL_SIZE, BOARD_SIZE, NOTE_SIZE


def display_selected_number(screen: pygame.Surface, number_img: pygame.Surface) -> None:
    """
    Display the current selected number at the cursor
    :param screen: A Pygame surface to draw a number onto
    :param number_img: The image to draw at the cursor's location
    :return: None
    """
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(source=number_img, dest=mouse_pos)


def display_gridlines(screen: pygame.Surface):
    """
    Display the gridlines on the screen
    :param screen: A Pygame surface to draw gridlines onto
    :return: A Pygame surface with drawn gridlines
    """
    for i in range(8):
        pygame.draw.line(screen, Colors.black if (i + 1) % 3 == 0 else Colors.gray, (CELL_SIZE * (i + 1), 0),
                         (CELL_SIZE * (i + 1), BOARD_SIZE))
        pygame.draw.line(screen, Colors.black if (i + 1) % 3 == 0 else Colors.gray, (0, CELL_SIZE * (i + 1)),
                         (BOARD_SIZE, CELL_SIZE * (i + 1)))


def display_board(screen: pygame.Surface, images: dict, board: Board):
    """
    Display the game state on the screen
    :param screen: A Pygame surface to draw the board onto
    :param board: A Board representing a Sudoku puzzle
    :param images: A dict of image lists. Contains 'placed', 'blocked', and 'note' image lists
    :return: A Pygame surface with a drawn Sudoku game-state
    """
    for row in range(1, 10):  # for every row
        for col in range(1, 10):  # for every column
            cell = board.get_cell(row=row, col=col)
            if cell.val:  # if the cell has a value
                if cell.valid:
                    screen.blit(images['placed'][cell.val], ((col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE))
                elif cell.blocked:
                    screen.blit(images['blocked'][cell.val], ((col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE))
                else:
                    screen.blit(images['invalid'][cell.val], ((col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE))
            elif cell.notes:
                for i in range(9):
                    potential_note = i + 1
                    note_pos = (i // 3, i % 3)
                    note_x_location = ((col - 1) * CELL_SIZE) + (note_pos[1] * NOTE_SIZE)
                    note_y_location = ((row - 1) * CELL_SIZE) + (note_pos[0] * NOTE_SIZE)
                    if potential_note in cell.notes:
                        screen.blit(images['note'][potential_note], (note_x_location, note_y_location))
