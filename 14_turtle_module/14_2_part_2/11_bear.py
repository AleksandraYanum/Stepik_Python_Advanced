import turtle as t


def draw_simple_bear(size):
    t.pencolor('SaddleBrown')
    t.hideturtle()
    t.speed(10)

    # Head
    t.penup()
    t.setpos(0, -size * 1.8)
    t.pendown()
    t.fillcolor('BurlyWood')
    t.begin_fill()
    t.circle(size * 2)
    t.end_fill()

    # Face
    t.fillcolor('NavajoWhite')
    t.begin_fill()
    t.circle(size * 1.2)
    t.end_fill()

    # Mouth
    t.fillcolor('Maroon')
    t.penup()
    t.setpos(0, -size / 10)
    t.pendown()
    t.begin_fill()
    t.circle(size / 5)
    t.end_fill()
    t.setpos(0, -size)

    # Eyes
    for eye_pos in [(-size, size / 3), (size, size / 3)]:
        t.color('Black', 'Black')
        t.penup()
        t.setpos(eye_pos)
        t.pendown()
        t.begin_fill()
        t.circle(size // 5)
        t.end_fill()

    # Ears
    for ear_pos in [(-size * 1.7, size * 1.5), (size * 1.7, size * 1.5)]:
        t.fillcolor('LightPink')
        t.penup()
        t.setpos(ear_pos)
        t.pendown()
        t.begin_fill()
        t.circle(size // 2)
        t.end_fill()

    t.penup()
    t.setpos(0, -size * 3)


def main():
    draw_simple_bear(50)


main()
