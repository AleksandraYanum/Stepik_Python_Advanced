import turtle as t
from itertools import cycle


def circle_color_line(radius, amount, start_x, start_y, colors):
    x_cor, y_cor = start_x, start_y
    diameter = 2 * radius
    t.hideturtle()
    for _, color in zip(range(amount), cycle(colors)):
        t.penup()
        t.goto(x_cor, y_cor)
        t.pendown()
        t.pencolor(color)
        t.circle(radius)
        x_cor = x_cor + diameter


def olympic_rings(radius, start_x, start_y):
    diameter = 2 * radius
    t.speed(10)
    t.pensize(7)
    colors = ['chartreuse', 'DeepSkyBlue', 'black', 'red', 'yellow']
    color_start_idx = 0
    color_end_idx = 0

    # green circle
    circle_amount = 1
    color_end_idx += circle_amount
    x_cor, y_cor = start_x + radius, start_y - radius
    circle_color_line(radius, circle_amount,  x_cor, y_cor, colors[color_start_idx:color_end_idx])

    # all top circles
    circle_amount = 3
    color_start_idx = color_end_idx
    color_end_idx += circle_amount
    x_cor, y_cor = x_cor - diameter - radius, y_cor + radius
    circle_color_line(radius, 3,  x_cor, y_cor, colors[color_start_idx:color_end_idx])

    # yellow circle
    color_start_idx = color_end_idx
    color_end_idx += circle_amount
    x_cor, y_cor = x_cor + radius, y_cor - radius
    circle_color_line(radius, 1,  x_cor, y_cor, colors[color_start_idx:color_end_idx])


def main():
    radius = 70

    # Coordinate of the point of the two lower circles contact
    start_x, start_y = 0, 0
    olympic_rings(radius, start_x, start_y)
    # circle_line(radius, 4, start_x, start_y)


main()