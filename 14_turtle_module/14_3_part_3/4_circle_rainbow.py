import turtle as t


DRAWING_SPEED = 10


def ten_circle_rainbow(start_x, start_y, biggest_radius):
    circle_core(start_x, start_y, biggest_radius, circle_amount=7, circle_radius_delta=10)

  
def circle_core(start_x, start_y, radius, circle_amount=1, circle_radius_delta=0):
    x, y = start_x, start_y - radius
    t.penup()
    t.goto(x, y)
    t.pendown()

    y_cor = y
    for _ in range(circle_amount):
        t.circle(radius)
        radius -= circle_radius_delta
        t.penup()
        y_cor += circle_radius_delta
        t.goto(x, y_cor)
        t.pendown()

def main():
    t.hideturtle(), t.speed(DRAWING_SPEED)

    bigest_radius = 300
    start_x, start_y = 0, - 50

    circle_core(start_x, start_y, bigest_radius)

    input()


main()