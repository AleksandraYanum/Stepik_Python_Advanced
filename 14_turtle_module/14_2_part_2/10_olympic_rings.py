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



# def olympic_rings(radius, start_x, start_y):
#     t.pensize(7)
#     t.speed(10)

#     colors = ['chartreuse', 'red', 'black', 'DeepSkyBlue', 'yellow']
    
#     for color, position in zip(colors, positions):
#         t.penup()
#         t.goto(position)
#         t.pencolor(color)
#         t.pendown()
#         t.circle(radius)


def main():
    radius = 50
    start_x, start_y = 0, 0
    # olympic_rings(radius, start_x, start_y)
    circle_line(radius, 4, start_x, start_y)


main()