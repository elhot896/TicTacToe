import pygame
from grid2 import Grid

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-tac-toe')

grid = Grid()

running = True
player = "X"
comp_move = False


def ai_comp(value):
    pos_move = 1
    if not grid.game_over:
        while True:
            if pos_move == 1 and grid.get_value(0, 0) == 0:
                grid.get_mouse_position(0, 0, value)
                break
            else:
                pos_move += 1
            if pos_move == 2 and grid.get_value(0, 1) == 0:
                grid.get_mouse_position(0, 1, value)
                break
            else:
                pos_move += 1
            if pos_move == 3 and grid.get_value(0, 2) == 0:
                grid.get_mouse_position(0, 2, value)
                break
            else:
                pos_move += 1
            if pos_move == 4 and grid.get_value(1, 0) == 0:
                grid.get_mouse_position(1, 0, value)
                break
            else:
                pos_move += 1
            if pos_move == 5 and grid.get_value(1, 1) == 0:
                grid.get_mouse_position(1, 1, value)
                break
            else:
                pos_move += 1
            if pos_move == 6 and grid.get_value(1, 2) == 0:
                grid.get_mouse_position(1, 2, value)
                break
            else:
                pos_move += 1
            if pos_move == 7 and grid.get_value(2, 0) == 0:
                grid.get_mouse_position(2, 0, value)
                break
            else:
                pos_move += 1

            if pos_move == 8 and grid.get_value(2, 1) == 0:
                grid.get_mouse_position(2, 1, value)
                break
            else:
                pos_move += 1
            if pos_move == 9 and grid.get_value(2, 2) == 0:
                grid.get_mouse_position(2, 2, value)
                break
            else:
                pos_move = 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if player == "X":
                    grid.get_mouse_position(pos[0] // 200, pos[1] // 200, player)
                    comp_move = True
                    player = "O"
                else:
                    player = "X"
                    comp_move = False
        if comp_move:
            ai_comp(player)
            comp_move = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_game()
                grid.game_over = False
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((224, 156, 18))

    grid.draw(surface)

    pygame.display.flip()
