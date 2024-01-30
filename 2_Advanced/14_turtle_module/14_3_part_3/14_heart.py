from turtle import *
from math import pi, sin, cos


HEART_BORDER_COLOR = 'red'
HEART_COLOR = 'red'
T_DIF = 0.01
DRAWING_SPEED = 100
HEART_SCALE = 3

def heart(scale=1):
    t = 0
    pencolor(HEART_BORDER_COLOR), fillcolor(HEART_COLOR)
    begin_fill()

    while t <= 2 * pi:
        x = scale * (128 * sin(t) ** 3)
        y = scale * (8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5))
        goto(x, y)
        t += T_DIF

    end_fill()


def main():
    speed(DRAWING_SPEED), hideturtle()
    heart(HEART_SCALE)

    input()


main()