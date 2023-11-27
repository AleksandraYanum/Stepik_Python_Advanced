import turtle as t

DRAWING_SPEED = 10
START_X, START_Y = 0, 0

COMPASS_RAY_AMOUNT = 4
COMPASS_RAY_LEN = 200

COMPASS_TEXT_SIZE = 10
COMPASS_TEXT_FONT = 'Arial'

COMPASS_TEXT_DISTANCE = 10
TOTAL_TEXT_DISTANCE = COMPASS_RAY_LEN + COMPASS_TEXT_DISTANCE
COMPASS_TEXT_ALIGNMENT_DIC = {
                          'Север': (0, TOTAL_TEXT_DISTANCE, 'center'), 
                          'Восток': (TOTAL_TEXT_DISTANCE + COMPASS_TEXT_SIZE // 2, - COMPASS_TEXT_SIZE // 1.5, 'left'), 
                          'Юг': (0, -(TOTAL_TEXT_DISTANCE + 2 * COMPASS_TEXT_SIZE), 'center'), 
                          'Запад': (-(TOTAL_TEXT_DISTANCE + COMPASS_TEXT_SIZE // 3), - COMPASS_TEXT_SIZE // 1.5, 'right')
                          }


def snowflake(start_x, start_y, ray_amount, radius, ray_func, core_func):
    t.hideturtle(), t.speed(DRAWING_SPEED)
    turn_angle = 360 / ray_amount

    t.penup()
    t.goto(start_x, start_y), t.setheading(0)
    t.pendown()

    for _ in range(ray_amount):
        ray_func(start_x, start_y, radius)
        t.right(turn_angle)

    core_radius = radius // 4
    core_func(start_x, start_y, core_radius, ray_amount)


def add_compass_text(start_x, start_y, COMPASS_TEXT_ALIGNMENT_DIC):
     
     for text, text_params in COMPASS_TEXT_ALIGNMENT_DIC.items():
        x_shift, y_shift, alignment = text_params
        t.penup()
        t.goto(start_x + x_shift, start_y + y_shift)
        t.pendown()
        t.write(text, align=alignment, font=(COMPASS_TEXT_FONT, COMPASS_TEXT_SIZE))


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

def line_ray(start_x, start_y, ray_len):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    t.forward(ray_len)


def main():
    
    t.tracer(0)
    start_x, start_y = 0, 0

    snowflake(start_x, start_y, COMPASS_RAY_AMOUNT, COMPASS_RAY_LEN, line_ray, circle_core)
    add_compass_text(start_x, start_y, COMPASS_TEXT_ALIGNMENT_DIC)

 
    input()

main()