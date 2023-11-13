import turtle as t
from math import sin, pi, sqrt

EXTERNAL_BORDER_COLOR = 'black'
INTERNAL_BORDER_COLOR = 'white'
STOP_COLOR = 'red'
TEXT_COLOR = 'white'
COLORS = [EXTERNAL_BORDER_COLOR, INTERNAL_BORDER_COLOR, STOP_COLOR]

STOP_SIDE_LEN = 150
STOP_SIZE_DIF = 30


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
        radius = int(side_len / (2 * sin(180 / 8 * pi / 180)))
        mid_height = sqrt(pow(radius, 2) - pow(side_len / 2, 2))

        t.up(), t.goto(start_x - side_len // 2, start_y + mid_height), t.down()
        t.pencolor(COLORS[color])
        
        t.fillcolor(COLORS[color])
        t.begin_fill()
        shape(side_len, 8)
        t.end_fill() 

        side_len -= STOP_SIZE_DIF
      

    side_len += STOP_SIZE_DIF

    t.up()
    t.goto(start_x - mid_height, start_y - side_len // 2)
    t.pencolor('white')
    t.write('STOP', align='center', font=('Arial', 16, 'normal'))

    input()


main()

