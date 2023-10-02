import turtle as t


def draw_simple_bear(start_x, start_y, head_radius):
    t.penup()
    t.goto(start_x, start_y)
    t.hideturtle()
    t.speed(20)
    t.pencolor('SaddleBrown')
    t.pendown()

    # Head
    t.fillcolor('BurlyWood')
    t.begin_fill()
    t.circle(head_radius)
    t.end_fill()

    # Face
    face_radius = head_radius / 2
    t.fillcolor('NavajoWhite')
    t.begin_fill()
    t.circle(face_radius)
    t.end_fill()

    # Nose and mouth
    nose_radius = head_radius / 10
    t.fillcolor('Maroon')
    t.penup()
    t.setpos(start_x, start_y + face_radius)
    t.pendown()
    t.begin_fill()
    t.circle(nose_radius)
    t.end_fill()
    t.setpos(start_x, start_y + nose_radius)

    # Eyes
    eye_raduis = nose_radius
    eye_x_cor_1 = start_x - face_radius
    eye_x_cor_2 = start_x + face_radius
    eye_y_cor = start_y + head_radius

    for eye_pos in [(eye_x_cor_1, eye_y_cor), (eye_x_cor_2, eye_y_cor)]:
        t.color('Black')
        t.penup()
        t.setpos(eye_pos)
        t.pendown()
        t.begin_fill()
        t.circle(eye_raduis)
        t.end_fill()

    # Ears
    ear_x_cor_1 = start_x - head_radius
    ear_x_cor_2 = start_x + head_radius
    ear_y_cor = start_y + head_radius * 1.5

    for ear_pos in [(ear_x_cor_1, ear_y_cor), (ear_x_cor_2, ear_y_cor)]:
        t.fillcolor('LightPink')
        t.penup()
        t.setpos(ear_pos)
        t.pendown()
        t.begin_fill()
        t.circle(face_radius / 2)
        t.end_fill()

    t.penup()
    input()
    t.setpos(0, -head_radius * 3)


def main():
    head_radius = 100
    start_x, start_y = 0, -150
    draw_simple_bear(start_x, start_y, head_radius)


main()
