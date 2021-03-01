import pygame
from math import sin
from random import randint
from classes import Board, Apple, Status
from functions import eat_apple, hit_the_wall, redact_coords

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (36, 255, 0)
c_wall = (255, 100, 0)
c_circle = (120, 0, 255)

start_or_stop = [0, 2]
r_apple = 15
r_circle = 20
step = 0
size = 10

dist = 10 + r_circle
delta_x_y = int(r_circle * sin(45))

apples = list()


class Ball:
    def __init__(self, x_pos, y_pos):
        self.centre_x = int(x_pos)
        self.centre_y = int(y_pos)
        self.points_on_a_circle = list()
        redact_coords(self)

    def drawing(self, screen):
        pygame.draw.circle(screen, c_circle, (self.centre_x, self.centre_y), r_circle)


if __name__ == '__main__':
    pygame.init()

    score = 0

    cells = 70
    y_pos = 40
    x_pos = 40
    route = 2
    count = 0
    pause = False
    v = 100

    screen = pygame.display.set_mode((cells * size + 20, cells * size + 20))
    pygame.display.flip()

    board = Board(cells)
    ball = Ball(x_pos, y_pos)
    status = Status(screen)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif status.game not in start_or_stop and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if board.get_coord(event.pos) is not None and board.get_coord(event.pos) not in board.walls:
                        board.walls.append(board.get_coord(event.pos))
                elif event.button == 3:
                    if board.get_coord(event.pos) in board.walls:
                        del board.walls[board.walls.index(board.get_coord(event.pos))]

            elif event.type == pygame.KEYDOWN:
                if not pause and event.key == pygame.K_r:
                    clock = pygame.time.Clock()
                    status.game = 0
                    ball = Ball(x_pos, y_pos)
                    board.walls = list()
                    apples = list()
                    score = 0
                    route = 2
                    v = 100
                    r_circle = 20
                elif event.key == pygame.K_ESCAPE:
                    if status.game == 2:
                        running = False
                    elif status.game != 0:
                        pause = not pause
                        if not pause:
                            clock = pygame.time.Clock()
                            status.pause = False
                        else:
                            status.pause = True
                if status.game != 2:
                    if event.key == pygame.K_BACKSPACE:
                        clock = pygame.time.Clock()
                        status.game = 1
                    elif status.game != 0:
                        if (not pause) and event.key == pygame.K_UP:
                            route = 1
                        elif (not pause) and event.key == pygame.K_RIGHT:
                            route = 2
                        elif (not pause) and event.key == pygame.K_DOWN:
                            route = 3
                        elif (not pause) and event.key == pygame.K_LEFT:
                            route = 4

        screen.fill(c_wall)
        pygame.draw.rect(screen, green, (10, 10, cells * size, cells * size))
        # screen.fill((127, 255, 0))
        # board.render(screen)
        for cell in board.walls:
            j = cell[0]
            i = cell[1]
            pygame.draw.rect(screen, c_wall,
                             (board.left + board.size * j, board.top + board.size * i,
                              board.size, board.size))
        status.draw_score(score)
        status.draw_pause()
        status.draw_game_over()
        status.draw_start()

        if not pause and status.game not in start_or_stop:
            count += 1
            if count == 1000:
                apples.append(Apple((randint(r_apple + 20, board.long - (r_apple + 20)),
                                     randint(r_apple + 20, board.long - (r_apple + 20)))))
                count = 0

            for_delite = list()
            for i in range(len(apples)):
                apple = apples[i]
                if eat_apple(board, ball, apple, step, r_apple):
                    for_delite.append(i)

            delta_ind = 0
            for i in sorted(for_delite):
                i -= delta_ind
                delta_ind += 1
                v += 15
                r_circle += 2
                step += 2
                dist = 10 + r_circle
                score += 1

                del apples[i]

        for apple in apples:
            pygame.draw.circle(screen, red, apple.coords, r_apple)
        ball.drawing(screen)

        if not pause and status.game not in start_or_stop:
            if route == 1:
                ball.centre_y -= v * clock.tick() / 1000
            elif route == 2:
                ball.centre_x += v * clock.tick() / 1000
            elif route == 3:
                ball.centre_y += v * clock.tick() / 1000
            elif route == 4:
                ball.centre_x -= v * clock.tick() / 1000
            redact_coords(ball, r_circle)

        if hit_the_wall(board, ball, dist):
            status.game = 2
        pygame.display.flip()
    print('Game over, good bye')
