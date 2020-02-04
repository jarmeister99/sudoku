import os
import sys

import pygame
from board import Board
from display import display_gridlines, display_board, display_selected_number
from mouse import get_hovered_cell
from util import SIZE, Colors, CELL_SIZE, NOTE_SIZE


class Sudoku:
    def __init__(self):
        self.selected_number = None
        self.numbers = {}
        self.note_numbers = {}
        self.load_numbers()
        self.board = Board()
        self.screen = pygame.display.set_mode((SIZE, SIZE))
        self.loop()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        self.selected_number = '1'
                    if event.key == pygame.K_2:
                        self.selected_number = '2'
                    if event.key == pygame.K_3:
                        self.selected_number = '3'
                    if event.key == pygame.K_4:
                        self.selected_number = '4'
                    if event.key == pygame.K_5:
                        self.selected_number = '5'
                    if event.key == pygame.K_6:
                        self.selected_number = '6'
                    if event.key == pygame.K_7:
                        self.selected_number = '7'
                    if event.key == pygame.K_8:
                        self.selected_number = '8'
                    if event.key == pygame.K_9:
                        self.selected_number = '9'
                    if event.key == pygame.K_ESCAPE:
                        self.selected_number = None
                    if event.key == pygame.K_r:
                        self.board.reset()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_number:
                        sel = get_hovered_cell()
                        if event.button == 1:  # Left click
                            if self.selected_number == self.board.get_cell(sel[0], sel[1]):
                                self.board.unset_cell(row=sel[0], col=sel[1])
                            else:
                                self.board.set_cell(row=sel[0], col=sel[1], val=int(self.selected_number))
                                self.board.clear_cell_notes(row=sel[0], col=sel[1])
                        if event.button == 3:  # Right click
                            if self.selected_number in self.board.get_cell_notes(sel[0], sel[1]):
                                self.board.unnote_cell(row=sel[0], col=sel[1], note=int(self.selected_number))
                            else:
                                self.board.note_cell(row=sel[0], col=sel[1], note=int(self.selected_number))
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
