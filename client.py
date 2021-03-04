import pygame
from grid import Grid
import threading
import socket
import pickle


surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-tac-toe-CLIENT')



def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()



HOST = socket.gethostname()
PORT = 65431

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def receive_data():
    global turn
    while True:
        data = sock.recv(1024)
        print(data)
        data = pickle.loads(data)
        x = data[0]
        y = data[1]
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_value(x, y) == 0:
            grid.set_value(x, y, "X")

create_thread(receive_data)

grid = Grid()
running = True
player = "O"
turn = False
playing = 'True'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellX, cellY = pos[0] // 200, pos[1] // 200
                    grid.get_mouse_position(cellX, cellY, player)
                    if grid.game_over:
                        playing = 'False'
                    send_data = [cellX, cellY, 'yourturn', playing]
                    send_data = pickle.dumps(send_data)
                    print(send_data)
                    sock.send(send_data)
                    turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((224, 156, 18))

    grid.draw(surface)

    pygame.display.flip()
