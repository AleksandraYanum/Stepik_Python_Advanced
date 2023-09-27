import turtle as t


def olympic_rings():

    radius = 100
    t.pensize(7)
    t.speed(10)

    colors = ['chartreuse', 'red', 'black', 'DeepSkyBlue', 'yellow']
    positions = [(100, -115),
                (202, 0),
                (-3, 0),
                (-208, 0),
                (-106, -115)]
                
    for color, position in zip(colors, positions):
        t.penup()
        t.goto(position)
        t.pencolor(color)
        t.pendown()
        t.circle(radius)


def main():
    olympic_rings()


main()