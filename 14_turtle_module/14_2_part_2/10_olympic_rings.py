import turtle as t
from itertools import cycle


def circle_line(radius, amount, start_x, start_y, colors):
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
    colors = ['chartreuse', 'DeepSkyBlue', 'black', 'red', 'yellow']


    # green circle
    circle_amount = 1
    x_cor, y_cor = start_x + radius, start_y - radius
    circle_line(radius, circle_amount,  x_cor, y_cor, colors[0:1])

    # all top circles
    circle_amount = 3
    x_cor, y_cor = x_cor - diameter - radius, y_cor + radius
    circle_line(radius, 3,  x_cor, y_cor, colors[1:4])

    # yellow circle
    x_cor, y_cor = x_cor + radius, y_cor - radius
    circle_line(radius, 1,  x_cor, y_cor, colors[4:5])


def main():
    radius = 70

    # Coordinate of the point of the two lower circles contact
    start_x, start_y = 0, 0
    olympic_rings(radius, start_x, start_y)
    # circle_line(radius, 4, start_x, start_y)


main()