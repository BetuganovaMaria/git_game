from math import sin


def eat_apple(board, ball, apple, step, r_apple):
    if max(0, apple.left_up_x - 2 * step) <= int(ball.centre_x) <= \
            min(apple.left_up_x + 2 * r_apple + 2 * step, board.long) and \
            max(0, apple.left_up_y - 2 * step) <= int(ball.centre_y) <= \
            min(apple.left_up_y + 2 * r_apple + 2 * step, board.long):
        return True
    return False


def hit_the_wall(board, ball, dist):
    if int(ball.centre_x) in [dist, board.long - dist] or \
            int(ball.centre_y) in [dist, board.long - dist]:
        return True
    for i in ball.points_on_a_circle:
        if board.get_coord(i) in board.walls:
            return True
    return False


def redact_coords(ball, r_circle=20):
    delta_x_y = int(r_circle * sin(45))
    x = int(ball.centre_x)
    y = int(ball.centre_y)
    ball.points_on_a_circle = [(x, y - r_circle),
                               (x + delta_x_y, y - delta_x_y),
                               (x + r_circle, y),
                               (x + delta_x_y, y + delta_x_y),
                               (x, ball.centre_y + delta_x_y),
                               (x - delta_x_y, y + delta_x_y),
                               (x - r_circle, y),
                               (x - delta_x_y, y - delta_x_y)]
