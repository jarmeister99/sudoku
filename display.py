import pygame

from util import Colors, BOARD_SIZE, CELL_SIZE, NOTE_SIZE


def display_selected_number(screen, number_img):
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(number_img, mouse_pos)


def display_gridlines(screen):
    for i in range(8):
        pygame.draw.line(screen, Colors.black if (i + 1) % 3 == 0 else Colors.gray, (CELL_SIZE * (i + 1), 0),
                         (CELL_SIZE * (i + 1), BOARD_SIZE))
        pygame.draw.line(screen, Colors.black if (i + 1) % 3 == 0 else Colors.gray, (0, CELL_SIZE * (i + 1)),
                         (BOARD_SIZE, CELL_SIZE * (i + 1)))


def display_board(screen, board, numbers, note_numbers, placed, placed_numbers):
    for row in range(1, 10):
        for col in range(1, 10):
            cell_val = board.get_cell(row, col)
            cell_notes = board.get_cell_notes(row, col)

            if cell_val != '0':
                if (col, row) in placed:
                    screen.blit(placed_numbers[cell_val], ((col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE))
                else:
                    screen.blit(numbers[cell_val], ((col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE))
            elif cell_notes:
                for i in range(9):
                    potential_note = i + 1
                    note_pos = (i // 3, i % 3)
                    note_x_location = ((col - 1) * CELL_SIZE) + (note_pos[1] * NOTE_SIZE)
                    note_y_location = ((row - 1) * CELL_SIZE) + (note_pos[0] * NOTE_SIZE)
                    if str(potential_note) in cell_notes:
                        screen.blit(note_numbers[str(potential_note)], (note_x_location, note_y_location))
