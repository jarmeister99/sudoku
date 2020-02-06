import pygame

from util import Colors, BOARD_SIZE, CELL_SIZE, NOTE_SIZE


def display_selected_number(screen, number_img):
    """

    :param screen: A Pygame surface to draw a number onto
    :param number_img: The image to draw at the cursor's location
    :return: A Pygame surface with the input image drawn at the cursor's location
    """
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(number_img, mouse_pos)


def display_gridlines(screen):
    """

    :param screen: A Pygame surface to draw gridlines onto
    :return: A Pygame surface with drawn gridlines
    """
    for i in range(8):
        pygame.draw.line(screen, Colors.black if (i + 1) % 3 == 0 else Colors.gray, (CELL_SIZE * (i + 1), 0),
                         (CELL_SIZE * (i + 1), BOARD_SIZE))
        pygame.draw.line(screen, Colors.black if (i + 1) % 3 == 0 else Colors.gray, (0, CELL_SIZE * (i + 1)),
                         (BOARD_SIZE, CELL_SIZE * (i + 1)))


def display_board(screen, images, board, placed):
    """

    :param screen: A Pygame surface to draw the board onto
    :param board: A Board representing a Sudoku puzzle
    :param images: A list of image lists. Contains 'placed', 'blocked', and 'note' image lists
    :param placed: A list of positions representing which cells the user has placed values in
    :return: A Pygame surface with a drawn Sudoku game-state
    """
    for row in range(1, 10):
        for col in range(1, 10):
            cell_val = board.get_cell(row, col)
            cell_notes = board.get_cell_notes(row, col)

            if cell_val != '0':
                if (col, row) in placed:
                    screen.blit(images['placed'][cell_val], ((col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE))
                else:
                    screen.blit(images['blocked'][cell_val], ((col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE))
            elif cell_notes:
                for i in range(9):
                    potential_note = i + 1
                    note_pos = (i // 3, i % 3)
                    note_x_location = ((col - 1) * CELL_SIZE) + (note_pos[1] * NOTE_SIZE)
                    note_y_location = ((row - 1) * CELL_SIZE) + (note_pos[0] * NOTE_SIZE)
                    if str(potential_note) in cell_notes:
                        screen.blit(images['note'][str(potential_note)], (note_x_location, note_y_location))
