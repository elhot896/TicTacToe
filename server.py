import pygame
from grid2 import Grid
import threading
import socket

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-tac-toe-SERVER')


def thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()


HOST = socket.gethostname()
PORT = 65432
connection_established = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)


def receive_data():
    global turn
    while True:
        data = conn.recv(1024).decode()
        data = data.split('-')
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_value(x, y) == 0:
            grid.set_value(x, y, 'O')


def waiting_connection():
    global connection_established, conn, addr
    conn, addr = sock.accept()  # wait for a connection, it is a blocking method
    print('client is connected')
    connection_established = True
    receive_data()


# run the blocking functions in a separate thread
thread(waiting_connection)

grid = Grid()
running = True
player = "X"
turn = True
playing = 'True'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and connection_established:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    X, Y = pos[0] // 200, pos[1] // 200
                    grid.get_mouse_position(X, Y, player)
                    if grid.game_over:
                        playing = 'False'
                    send_data = '{}-{}-{}-{}'.format(X, Y, 'yourturn', playing).encode()
                    conn.send(send_data)
                    turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_game()
                grid.game_over = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((224, 156, 18))

    grid.draw(surface)

    pygame.display.flip()
