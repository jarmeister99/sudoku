import os
import sys

import pygame
from board import Board
from display import display_gridlines, display_board, display_selected_number
from key import get_selected_number
from mouse import mark_board, get_hovered_cell
from puzzle import solve, generate
from util import BOARD_SIZE, Colors, CELL_SIZE, NOTE_SIZE, SETTINGS_HEIGHT


class Sudoku:
    def __init__(self):
        self.selected_number = None
        self.images = {}
        self.load_numbers()
        self.board = Board()
        #self.board.load_test_board()
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE + SETTINGS_HEIGHT))
        self.placed = []
        self.loop()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    self.selected_number = get_selected_number(event)
                    if event.key == pygame.K_r:
                        self.board.reset()
                    if event.key == pygame.K_s:
                        solve(self.board)
                    if event.key == pygame.K_g:
                        generate(self.board)
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_number:
                        loc = mark_board(event, self.board, self.selected_number, self.board.blocked_cells)
                        if loc:
                            if loc[1]:
                                self.placed.append(loc[0])
                            else:
                                self.placed.remove(loc[0])

            self.screen.fill(Colors.white)
            display_gridlines(self.screen)
            display_board(self.screen, self.images, self.board, self.placed)
            if self.selected_number:
                display_selected_number(self.screen, self.images['blocked'][self.selected_number])
            pygame.display.flip()

    def load_numbers(self):
        blocked_numbers = {}
        note_numbers = {}
        placed_numbers = {}
        for number in os.listdir('img/numbers'):
            number_img = pygame.image.load(f'img/numbers/{number}')
            blocked_numbers[number[0]] = pygame.transform.scale(number_img, (CELL_SIZE, CELL_SIZE))
            note_numbers[number[0]] = pygame.transform.scale(number_img, (NOTE_SIZE, NOTE_SIZE))
            pa = pygame.PixelArray(pygame.transform.scale(number_img, (CELL_SIZE, CELL_SIZE)))
            pa.replace(Colors.black, Colors.green)
            placed_numbers[number[0]] = pa.make_surface()
        self.images['blocked'] = blocked_numbers
        self.images['note'] = note_numbers
        self.images['placed'] = placed_numbers


if __name__ == '__main__':
    app = Sudoku()
