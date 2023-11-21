import turtle as t
from math import ceil
from random import randint, choice

#*******************************************************************************************************************

# Developer consts

MIN_SNOWFLAKE_RADIUS = 20
MAX_SNOWFLAKE_RADIUS = 200

MIN_RAY_AMOUNT = 4
MAX_RAY_AMOUNT = 16

GEAR_INNER_RADIUS_PERCENTAGE = 0.7

POSSIBLE_COLORS = ['DarkMagenta', 'blue', 'purple', 'ForestGreen', 'firebrick1', 'yellow', 'white']

MIN_PEN_SIZE = 1
MAX_PEN_SIZE = 4

#*******************************************************************************************************************

# User consts

USER_MAX_RAY_AMOUNT = 20

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650
SCREEN_COLOR = 'black'

#*******************************************************************************************************************

def left_mouse_click(x, y):
    draw_random_snowflake(x, y, USER_MAX_RAY_AMOUNT)


def draw_random_snowflake(x, y, *, min_radius=MIN_SNOWFLAKE_RADIUS, max_radius=MAX_SNOWFLAKE_RADIUS, \
    min_ray_amount=MIN_RAY_AMOUNT, max_ray_amount=MAX_RAY_AMOUNT, colors=POSSIBLE_COLORS, \
    min_pen_size=MIN_PEN_SIZE, max_pen_size=MAX_PEN_SIZE):

    possible_core_funcs = [five_circle_core, circle_core, gear_circle_core]
    possible_ray_funcs = [branch_ray_two_leaves, branch_ray_six_leaves, line_ray]

    # Random values set up
    t.pencolor(choice(colors))
    t.pensize(randint(min_pen_size, max_pen_size))

    random_ray_func = choice(possible_ray_funcs)
    random_core_func = choice(possible_core_funcs)

    random_radius = randint(min_radius, max_radius)
    random_ray_amount = randint(min_ray_amount, max_ray_amount)

    snowflake(x, y, random_ray_amount, random_radius, random_ray_func, random_core_func)


def snowflake(start_x, start_y, ray_amount, radius, ray_func, core_func):
    turn_angle = 360 / ray_amount

    t.penup()
    t.goto(start_x, start_y), t.setheading(0)
    t.pendown()

    for _ in range(ray_amount):
        ray_func(start_x, start_y, radius)
        t.right(turn_angle)

    core_radius = radius // 4
    core_func(start_x, start_y, core_radius, ray_amount)

 
def branch_ray_two_leaves(start_x, start_y, ray_len):
    leave_amount = 2
    leave_len = ray_len / 4
    leave_angle = 45

    branch_ray_base(start_x, start_y, ray_len, leave_amount, leave_len, leave_angle)


def branch_ray_six_leaves(start_x, start_y, ray_len):
    leave_amount = 6
    leave_len = ray_len / 8
    leave_angle = 120

    branch_ray_base(start_x, start_y, ray_len, leave_amount, leave_len, leave_angle)
    

def branch_ray_base(start_x, start_y, ray_len, leave_amount, leave_len, leave_angle):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    leave_distance = ray_len // (leave_amount + 2)
    t.forward(ray_len)

    # Drawing branch leaves
    # TODO: use goto
    for _ in range(leave_amount):
        t.penup()
        t.backward(leave_distance)
        t.left(leave_angle)
        t.pendown()
        t.forward(leave_len)
        t.penup()
        t.backward(leave_len)
        t.right(leave_angle * 2)
        t.pendown()
        t.forward(leave_len)
        t.penup()
        t.backward(leave_len)
        t.left(leave_angle)


def line_ray(start_x, start_y, ray_len):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    t.forward(ray_len)


def circle_ray(start_x, start_y, ray_len):
    radius = ray_len / 2

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    t.circle(radius)


def five_circle_core(start_x, start_y, biggest_radius, ray_amount):
    circle_core(start_x, start_y, biggest_radius, circle_amount=5, circle_radius_delta=10)

    
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


def gear_circle_core(start_x, start_y, radius, ray_amount):
    gear_circle_base(start_x, start_y, radius, ray_amount, mid_radius=None)


def gear_circle_base(start_x, start_y, radius, ray_amount, mid_radius=None):
    mid_radius = mid_radius if mid_radius is not None else radius * GEAR_INNER_RADIUS_PERCENTAGE 
    turn_angle = 360 // ray_amount // 2
    point_list = []

    t.hideturtle()
    t.penup()
    t.goto(start_x, start_y), t.setheading(0)

    lower_left_x = start_x + mid_radius
    lower_left_y = start_y

    for _ in range(ray_amount):
        t.right(turn_angle), t.forward(radius)
        top_x, top_y = [ceil(i) for i in t.pos()]

        t.backward(radius), t.right(turn_angle)
        t.forward(mid_radius)

        lower_right_x, lower_right_y = [ceil(i) for i in t.pos()]
        t.backward(mid_radius)

        point_list.extend([(lower_left_x, lower_left_y), (top_x, top_y), (lower_right_x, lower_right_y)])
        
        lower_left_x, lower_left_y = lower_right_x, lower_right_y

    point_list[-1] = point_list[0]

    t.penup()
    t.goto(point_list[0])
    t.pendown()

    for x, y in point_list[1:]:
        t.goto(x, y)


def main():
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT), t.Screen().bgcolor(SCREEN_COLOR)
    t.hideturtle(), t.tracer(0)
    t.Screen().onclick(left_mouse_click)
    t.Screen().listen()

    input()  

 
main()
