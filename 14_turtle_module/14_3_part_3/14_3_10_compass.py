import turtle as t

DRAWING_SPEED = 10

COMPASS_RAY_AMOUNT = 4
COMPASS_RADIUS = 200

COMPASS_TEXT_SIZE = 10
COMPASS_TEXT_FONT = 'Arial'
COMPASS_TEXT_ALIGNMENT = ['center', 'left', 'center', 'right']


def draw_compass(start_x, start_y, radius, *, text_size=COMPASS_TEXT_SIZE, text_font=COMPASS_TEXT_FONT, 
                 north_title='Север', east_title='Восток', south_title='Юг', west_title='Запад'):
    
    
    
    snowflake(start_x, start_y, COMPASS_RAY_AMOUNT, radius, line_ray, circle_core)
    add_compass_text(start_x, start_y, radius, text_size, text_font, north_title, east_title, south_title, west_title)


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


def add_compass_text(start_x, start_y, radius, size, font, *cardinal_direction_titles):

   text_params_dict = dict(zip(cardinal_direction_titles,
                               zip([
                                    (start_x, start_y + (radius + size)),
                                    (start_x + (radius + 1.5 * size), start_y - (size // 1.5)),
                                    (start_x, start_y - (radius + 2.5 * size)),
                                    (start_x - (radius + size), start_y - (size // 1.5))
                                    ], 
                                    COMPASS_TEXT_ALIGNMENT)))
   
   for text, (coords, alignment) in text_params_dict.items():
        x, y = coords
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(text, align=alignment, font=(font, size))


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

    draw_compass(start_x, start_y, COMPASS_RADIUS)


 
    input()

main()