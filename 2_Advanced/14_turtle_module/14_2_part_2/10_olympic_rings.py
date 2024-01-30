import turtle as t
from itertools import cycle


def circle_color_line(start_x, start_y, radius, amount, colors):
    x_cor, y_cor = start_x, start_y
    diameter = 2 * radius
    t.hideturtle()
    for _, color in zip(range(amount), cycle(colors)):
        t.penup()
        t.goto(x_cor, y_cor)
        t.pendown()
        t.pencolor(color)
        t.circle(radius)
        x_cor += diameter


def olympic_rings(start_x, start_y, radius):
    diameter = 2 * radius
    t.speed(10)
    t.pensize(7)
    colors = ['chartreuse', 'DeepSkyBlue', 'black', 'red', 'yellow']

    # green circle
    x_cor, y_cor = start_x + radius, start_y - radius
    circle_color_line(x_cor, y_cor, radius, 1, [colors[0]])

    # all top circles
    circle_amount = 3
    x_cor, y_cor = x_cor - diameter - radius, y_cor + radius
    circle_color_line(x_cor, y_cor, radius, circle_amount, colors[1:circle_amount + 1])

    # yellow circle
    x_cor, y_cor = x_cor + radius, y_cor - radius
    circle_color_line(x_cor, y_cor, radius, 1, [colors[-1]])


def main():
    # Coordinate of the point of the two lower circles contact
    start_x, start_y = 0, 0

    radius = 70
    olympic_rings(start_x, start_y, radius)


main()