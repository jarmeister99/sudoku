import os
import sys

import pygame
from src.grid.board import Board
from src.ui.display import display_gridlines, display_board, display_selected_number
from src.ui.key import get_selected_number
from src.ui.mouse import mark_board
from src.puzzle import solve, generate
from src.util import BOARD_SIZE, Colors, CELL_SIZE, NOTE_SIZE, SETTINGS_HEIGHT


class Sudoku:
    def __init__(self):
        self.selected_number = None
        self.images = {}
        self.load_numbers()
        self.board = Board()
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE + SETTINGS_HEIGHT))
        self.placed = []
        self.loop()

    def loop(self):
        while True:
            # handle input
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
                        self.placed = []
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_number:
                        mark_board(event, self.board, self.selected_number)

            # update graphics
            self.screen.fill(Colors.white)
            display_gridlines(self.screen)
            display_board(screen=self.screen, images=self.images, board=self.board)
            if self.selected_number:
                display_selected_number(self.screen, self.images['blocked'][self.selected_number])
            pygame.display.flip()

    def load_numbers(self):
        """
        Load all images from image directory to image store in memory
        :return:
        """
        blocked_numbers = {}
        note_numbers = {}
        placed_numbers = {}
        invalid_numbers = {}

        # load images from image directory
        for number in os.listdir('img/numbers'):
            number_img = pygame.image.load(f'img/numbers/{number}')
            blocked_numbers[int(number[0])] = pygame.transform.scale(number_img, (CELL_SIZE, CELL_SIZE))
            note_numbers[int(number[0])] = pygame.transform.scale(number_img, (NOTE_SIZE, NOTE_SIZE))

            pa = pygame.PixelArray(pygame.transform.scale(number_img, (CELL_SIZE, CELL_SIZE)))
            pa.replace(Colors.black, Colors.green)
            placed_numbers[int(number[0])] = pa.make_surface()
            pa.replace(Colors.green, Colors.red)
            invalid_numbers[int(number[0])] = pa.make_surface()

        # load all images to image store
        # store[blocked | note ...][1 ... 9] -> img
        self.images['blocked'] = blocked_numbers
        self.images['note'] = note_numbers
        self.images['placed'] = placed_numbers
        self.images['invalid'] = invalid_numbers


if __name__ == '__main__':
    app = Sudoku()
