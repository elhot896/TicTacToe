import pygame
from grid2 import Grid
import random
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-tac-toe')

grid = Grid()

running = True
player = "X"
comp_move = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if player == "X":
                    grid.get_mouse_position(pos[0] // 200, pos[1] // 200, player)
                elif player == "O":
                    grid.get_mouse_position(random.randint(0, 2), random.randint(0, 2), player)
                if grid.player_switch:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_game()
                grid.game_over = False
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((0, 0, 0))

    grid.draw(surface)

    pygame.display.flip()
