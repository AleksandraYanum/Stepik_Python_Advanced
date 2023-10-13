import turtle as t


CRESCENT_COLOR = 'orange'
SKY_COLOR = 'blue'
SPEED_DELTA = 5


def main():

    start_x, start_y = 0, -50
    crescent_diameter = 400
    t.penup(), t.hideturtle()
    t.goto(start_x, start_y)
    t.dot(crescent_diameter, CRESCENT_COLOR)
    

    t.bgcolor(SKY_COLOR)

    x = start_x + crescent_diameter
    t.goto(x, start_y)

    for i in range(crescent_diameter // SPEED_DELTA):
        x -= SPEED_DELTA
        t.goto(x, start_y)
        t.dot(crescent_diameter, SKY_COLOR)

    input()


main()
