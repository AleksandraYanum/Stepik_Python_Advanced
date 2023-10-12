import turtle as t
from itertools import cycle


DRAWING_SPEED = 50
RAINBOW_COLORS = ['red', 'orange', 'yellow', 'green', 'LightGreen', 'cyan', 'CornflowerBlue', 'blue', 'magenta', 'maroon1']


def ten_circle_rainbow(start_x, start_y, biggest_radius, colors):
    circle_amount = 10
    circle_radius_delta = biggest_radius // circle_amount
    circle_core(start_x, start_y, biggest_radius, colors, circle_amount, circle_radius_delta)

  
def circle_core(start_x, start_y, radius, colors, circle_amount=1, circle_radius_delta=0):
    x, y = start_x, start_y - radius
    t.penup()
    t.goto(x, y)
    t.pendown()

    y_cor = y
    for _, color in zip(range(circle_amount), cycle(colors)):
        t.fillcolor(color), t.begin_fill()
        t.circle(radius)
        t.end_fill()
        radius -= circle_radius_delta
        t.penup()
        y_cor += circle_radius_delta
        t.goto(x, y_cor)
        t.pendown()

def main():
    t.hideturtle(), t.speed(DRAWING_SPEED)

    bigest_radius = 200
    start_x, start_y = 0, - 50

    ten_circle_rainbow(start_x, start_y, bigest_radius, RAINBOW_COLORS)

    input()


main()