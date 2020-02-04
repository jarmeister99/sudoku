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


def display_board(screen, board, numbers, note_numbers):
    pos = [0, 0]
    for row_i, row in enumerate(board.grid):
        for col_i, cell in enumerate(row):
            if cell != '~':
                screen.blit(numbers[cell], (pos[1], pos[0]))
            elif board.notes[row_i][col_i]:
                notes = board.notes[row_i][col_i]
                note_pos = pos.copy()
                note_i = 1
                while note_i < 10:
                    if str(note_i) in notes:
                        screen.blit(note_numbers[str(note_i)], (note_pos[1], note_pos[0]))
                    if note_i % 3 == 0:
                        note_pos[1] -= 2 * NOTE_SIZE
                        note_pos[0] += NOTE_SIZE
                    else:
                        note_pos[1] += NOTE_SIZE
                    note_i += 1

            pos[1] += CELL_SIZE
        pos[1] = 0
        pos[0] += CELL_SIZE
