from turtle import *
from math import pi, sin, cos


HEART_BORDER_COLOR = 'red'
HEART_COLOR = 'red'
T_DIF = 0.01
DRAWING_SPEED = 100


def heart():
    t = 0
    pencolor(HEART_BORDER_COLOR), fillcolor(HEART_COLOR)
    begin_fill()

    while t <= 2 * pi:
        x = 128 * sin(t) ** 3
        y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
        goto(x, y)
        t += T_DIF

    end_fill()


def main():
    speed(DRAWING_SPEED), hideturtle()
    heart()

    input()


main()