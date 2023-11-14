import turtle as t
from itertools import cycle

CHESS_BOARD_SIZE = 300
SIZE_SQUARE_AMOUNT = 8
SQUARE_SIZE = CHESS_BOARD_SIZE // SIZE_SQUARE_AMOUNT

CHESS_COLORS = ['black', 'white']


def shape(side, angle_count=4):
    turn_angle = 360 / angle_count
    for _ in range(angle_count):
        t.forward(side)
        t.right(turn_angle)


def main():
    chess_board_half_size = CHESS_BOARD_SIZE // 2
    start_x, start_y = -chess_board_half_size, chess_board_half_size

    t.speed(100), t.hideturtle()

    x, y = start_x, start_y
    colors = CHESS_COLORS

    for _ in range(SIZE_SQUARE_AMOUNT):
        for color, _ in zip(cycle(colors), range(SIZE_SQUARE_AMOUNT)):
            t.penup(), t.goto(x, y), t.pendown()
            t.fillcolor(color)
            t.begin_fill()
            shape(SQUARE_SIZE)
            t.end_fill()
            x += SQUARE_SIZE
        x = start_x
        y -= SQUARE_SIZE
        colors = colors[::-1]

    input()


main()
