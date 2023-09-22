import turtle


def shape(side, angle_count=6):
    for _ in range(angle_count):
        turtle.forward(side)
        turtle.right(360 / angle_count)


shape(100, 6)