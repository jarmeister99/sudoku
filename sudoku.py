import os
import sys

import pygame
from board import Board
from display import display_gridlines, display_board, display_selected_number
from key import get_selected_number
from mouse import mark_board, get_hovered_cell
from util import BOARD_SIZE, Colors, CELL_SIZE, NOTE_SIZE, SETTINGS_HEIGHT


class Sudoku:
    def __init__(self):
        self.selected_number = None
        self.numbers = {}
        self.note_numbers = {}
        self.load_numbers()
        self.board = Board()
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE + SETTINGS_HEIGHT))
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
                    if event.key == pygame.K_c:
                        print(get_hovered_cell())
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_number:
                        mark_board(event, self.board, self.selected_number)

            self.screen.fill(Colors.white)
            display_gridlines(self.screen)
            display_board(self.screen, self.board, self.numbers, self.note_numbers)
            if self.selected_number:
                display_selected_number(self.screen, self.numbers[self.selected_number])
            pygame.display.flip()

    def load_numbers(self):
        for number in os.listdir('img/numbers'):
            number_img = pygame.image.load(f'img/numbers/{number}')
            self.numbers[number[0]] = pygame.transform.scale(number_img, (CELL_SIZE, CELL_SIZE))
            self.note_numbers[number[0]] = pygame.transform.scale(number_img, (NOTE_SIZE, NOTE_SIZE))


if __name__ == '__main__':
    app = Sudoku()
