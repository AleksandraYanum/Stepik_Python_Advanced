import turtle as t
from itertools import cycle

CHESS_BOARD_SIZE = 200
SIZE_SQUARE_AMOUNT = 5
SQUARE_SIZE = CHESS_BOARD_SIZE / SIZE_SQUARE_AMOUNT
# ALL_SQUARE_AMOUN = pow(SIZE_SQUARE_AMOUNT, 2)

CHESS_COLORS = ['black', 'white']


def shape(side, angle_count=4):
    turn_angle = 360 / angle_count
    for _ in range(angle_count):
        t.forward(side)
        t.right(turn_angle)


def main():
    chess_board_half_size = CHESS_BOARD_SIZE / 2
    start_x, start_y = -chess_board_half_size, chess_board_half_size
    SQUARE_SIZE = CHESS_BOARD_SIZE / SIZE_SQUARE_AMOUNT


    t.speed(10), t.hideturtle()
    x, y = start_x, start_y

    for _ in range(SIZE_SQUARE_AMOUNT):
        for _ in range(SIZE_SQUARE_AMOUNT):
            t.penup(), t.goto(x, y), t.pendown()
            shape(SQUARE_SIZE)
            x += SQUARE_SIZE
        x = start_x
        y -= SQUARE_SIZE


    input()






main()
