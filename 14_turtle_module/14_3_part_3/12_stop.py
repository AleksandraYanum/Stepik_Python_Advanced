import turtle as t
from math import sin, pi, sqrt

EXTERNAL_BORDER_COLOR = 'black'
INTERNAL_BORDER_COLOR = 'white'
STOP_COLOR = 'red'
TEXT_COLOR = 'white'
COLORS = [EXTERNAL_BORDER_COLOR, INTERNAL_BORDER_COLOR, STOP_COLOR]

STOP_TEXT = 'STOP'

STOP_SIDE_LEN = 200
STOP_SIZE_DIF = 10
STOP_SIGH_ANGLE_AMOUNT = 8


def shape(side, angle_count=6):
    turn_angle = 360 / angle_count
    for _ in range(angle_count):
        t.forward(side)
        t.right(turn_angle)


def main():

    t.speed(10), t.hideturtle(), t.up()
    start_x, start_y = 0, 0

    side_len = STOP_SIDE_LEN
    for color in range(len(COLORS)):
        radius = int(side_len / (2 * sin(180 / STOP_SIGH_ANGLE_AMOUNT * pi / 180)))
        mid_height = sqrt(pow(radius, 2) - pow(side_len / 2, 2))

        t.up(), t.goto(start_x - side_len // 2, start_y + mid_height), t.down()
        t.pencolor(COLORS[color])
        
        t.fillcolor(COLORS[color])
        t.begin_fill()
        shape(side_len, STOP_SIGH_ANGLE_AMOUNT)
        t.end_fill() 

        side_len -= STOP_SIZE_DIF
      

    side_len += STOP_SIZE_DIF

    t.up()

    t.goto(start_x - mid_height + STOP_SIZE_DIF // 2, start_y - side_len // 2)
    t.pencolor(TEXT_COLOR)
    t.write(STOP_TEXT, move=True, font=('Arial', radius // 2, 'normal'))

    input()


main()

