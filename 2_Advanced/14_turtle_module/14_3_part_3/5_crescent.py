import turtle as t
from itertools import cycle


SKY_COLOR = 'blue'
CRESCENT_COLOR = 'orange'

DRAWING_SPEED = 50


def circle_color_line(start_x, start_y, radius, amount, colors, x_offset=0, y_offset=0):
    x_cor, y_cor = start_x, start_y
    t.hideturtle()
    for _, color in zip(range(amount), cycle(colors)):
        t.fillcolor(color), t.pencolor(color)
        t.penup()
        t.goto(x_cor, y_cor)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        
        x_cor += x_offset
        y_cor += y_offset


def main():
    start_x, start_y = 0, -150
    radius = 200
    t.bgcolor(SKY_COLOR)
    t.hideturtle(), t.speed(DRAWING_SPEED)
    circle_color_line(start_x, start_y, radius, 2, [CRESCENT_COLOR, SKY_COLOR], x_offset=radius*0.3)

    input()

main()