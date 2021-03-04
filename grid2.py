import pygame
import os

letterX = pygame.image.load(os.path.join('res', 'letraX.png'))
letterO = pygame.image.load(os.path.join('res', 'letraO.png'))


class Grid:
    def __init__(self):
        self.grid_lines = [((0, 200), (600, 200)),  # first horizontal line
                           ((0, 400), (600, 400)),  # second horizontal line
                           ((200, 0), (200, 600)),  # first vertical line
                           ((400, 0), (400, 600))]  # second vertical line

        self.grid = [[0 for x in range(3)] for y in range(3)]
        self.game_over = False

    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_value(x, y) == "X":
                    surface.blit(letterX, (x * 200, y * 200))
                elif self.get_value(x, y) == "O":
                    surface.blit(letterO, (x * 200, y * 200))

    def get_value(self, x, y):
        return self.grid[y][x]

    def set_value(self, x, y, value):
        self.grid[y][x] = value

    def get_mouse_position(self, x, y, player):
        if self.get_value(x, y) == 0:
            self.set_value(x, y, player)
            self.check_winner()

    def check_winner(self):
        winX = False
        winO = False

        # X's Row

        if self.get_value(0, 0) == "X" and self.get_value(1, 0) == "X" and self.get_value(2, 0) == "X":
            winX = True
        elif self.get_value(0, 1) == "X" and self.get_value(1, 1) == "X" and self.get_value(2, 1) == "X":
            winX = True
        elif self.get_value(0, 2) == "X" and self.get_value(1, 2) == "X" and self.get_value(2, 2) == "X":
            winX = True

        # X's Column

        elif self.get_value(0, 0) == "X" and self.get_value(0, 1) == "X" and self.get_value(0, 2) == "X":
            winX = True
        elif self.get_value(1, 0) == "X" and self.get_value(1, 1) == "X" and self.get_value(1, 2) == "X":
            winX = True
        elif self.get_value(2, 0) == "X" and self.get_value(2, 1) == "X" and self.get_value(2, 2) == "X":
            winX = True

        # X's Diagonal

        elif self.get_value(0, 0) == "X" and self.get_value(1, 1) == "X" and self.get_value(2, 2) == "X":
            winX = True
        elif self.get_value(2, 0) == "X" and self.get_value(1, 1) == "X" and self.get_value(0, 2) == "X":
            winX = True

        # O's Row

        elif self.get_value(0, 0) == "O" and self.get_value(1, 0) == "O" and self.get_value(2, 0) == "O":
            winO = True
        elif self.get_value(0, 1) == "O" and self.get_value(1, 1) == "O" and self.get_value(2, 1) == "O":
            winO = True
        elif self.get_value(0, 2) == "O" and self.get_value(1, 2) == "O" and self.get_value(2, 2) == "O":
            winO = True

        # O's Column

        elif self.get_value(0, 0) == "O" and self.get_value(0, 1) == "O" and self.get_value(0, 2) == "O":
            winO = True
        elif self.get_value(1, 0) == "O" and self.get_value(1, 1) == "O" and self.get_value(1, 2) == "O":
            winO = True
        elif self.get_value(2, 0) == "O" and self.get_value(2, 1) == "O" and self.get_value(2, 2) == "O":
            winO = True

        # O's Diagonal

        elif self.get_value(0, 0) == "O" and self.get_value(1, 1) == "O" and self.get_value(2, 2) == "O":
            winO = True
        elif self.get_value(2, 0) == "O" and self.get_value(1, 1) == "O" and self.get_value(0, 2) == "O":
            winO = True

        if winX:
            print('X wins!')
            self.game_over = True
        elif winO:
            print('O wins!')
            self.game_over = True
        else:
            self.game_over = self.is_game_full()

    def is_game_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
        return True

    def clear_game(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.set_value(x, y, 0)

    def print_game(self):
        for row in self.grid:
            print(row)
