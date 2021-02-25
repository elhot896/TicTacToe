import pygame
import os
from tkinter import messagebox

letterX = pygame.image.load(os.path.join('res', 'letraX.png'))
letterO = pygame.image.load(os.path.join('res', 'letraO.png'))


class Grid:
    def __init__(self):
        self.grid_lines = [((0, 200), (600, 200)),  # first horizontal line
                           ((0, 400), (600, 400)),  # second horizontal line
                           ((200, 0), (200, 600)),  # first vertical line
                           ((400, 0), (400, 600))]  # second vertical line

        self.grid = [[0 for x in range(3)] for y in range(3)]
        self.switch_player = True
        # search directions  N         NW        W       SW       S       SE      E       NE
        self.search_pos = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
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
            self.switch_player = True
            if player == "X":
                self.set_value(x, y, "X")
            elif player == "O":
                self.set_value(x, y, "O")
            self.check_winner(x, y, player)
        else:
            self.switch_player = False

    def is_in_bounds(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def check_winner(self, x, y, player):
        count = 1
        for index, (pos_x, pos_y) in enumerate(self.search_pos):
            if self.is_in_bounds(x + pos_x, y + pos_y) and self.get_value(x + pos_x, y + pos_y) == player:
                count += 1
                xx = x + pos_x
                yy = y + pos_y
                if self.is_in_bounds(xx + pos_x, yy + pos_y) and self.get_value(xx + pos_x, yy + pos_y) == player:
                    count += 1
                    if count == 3:
                        break
                if count < 3:
                    new_dir = 0
                    # mapping the indices to opposite direction: 0-4 1-5 2-6 3-7 4-0 5-1 6-2 7-3
                    if index == 0:
                        new_dir = self.search_pos[4]  # N to S
                    elif index == 1:
                        new_dir = self.search_pos[5]  # NW to SE
                    elif index == 2:
                        new_dir = self.search_pos[6]  # W to E
                    elif index == 3:
                        new_dir = self.search_pos[7]  # SW to NE
                    elif index == 4:
                        new_dir = self.search_pos[0]  # S to N
                    elif index == 5:
                        new_dir = self.search_pos[1]  # SE to NW
                    elif index == 6:
                        new_dir = self.search_pos[2]  # E to W
                    elif index == 7:
                        new_dir = self.search_pos[3]  # NE to SW

                    if self.is_in_bounds(x + new_dir[0], y + new_dir[1]) \
                            and self.get_value(x + new_dir[0], y + new_dir[1]) == player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1

        if count == 3:
            print(player, 'wins!')
            messagebox.showinfo("Tic Tac Toe", player + " wins!")
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
