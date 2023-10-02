import turtle as t


def circle_line(radius, amount, start_x, start_y):
    x_cor, y_cor = start_x, start_y
    diameter = 2 * radius
    t.hideturtle()
    for _ in range(amount):
        t.penup()
        t.goto(x_cor, y_cor)
        t.pendown()
        t.circle(radius)
        x_cor = x_cor + diameter



def olympic_rings(radius, start_x, start_y):
    diameter = 2 * radius
    # t.speed(10)
    # colors = ['chartreuse', 'red', 'black', 'DeepSkyBlue', 'yellow']

    # green circle
    x_cor, y_cor = start_x + radius, start_y - radius
    circle_line(radius, 1,  x_cor, y_cor)

    # all top circles
    x_cor, y_cor = x_cor - diameter - radius, y_cor + radius
    circle_line(radius, 3,  x_cor, y_cor)

    # yellow circle
    x_cor, y_cor = x_cor + radius, y_cor - radius
    circle_line(radius, 1,  x_cor, y_cor)


def main():
    radius = 70

    # Coordinate of the point of the two lower circles contact
    start_x, start_y = 0, 0
    olympic_rings(radius, start_x, start_y)
    # circle_line(radius, 4, start_x, start_y)


main()