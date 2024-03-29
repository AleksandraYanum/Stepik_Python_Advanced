import turtle as t
from math import ceil, sqrt
from random import randint, choice


GEAR_INNER_RADIUS_PERCENTAGE = 0.7

MIN_SNOWFLAKE_RADIUS = 20
MAX_SNOWFLAKE_RADIUS = 200

MIN_RAY_AMOUNT = 4
MAX_RAY_AMOUNT = 16

MIN_SNOWFLAKE_AMOUNT = 10 
MAX_SNOWFLAKE_AMOUNT = 20

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650
RIGHT_X_BORDER = SCREEN_WIDTH // 2
LEFT_X_BORDER = - RIGHT_X_BORDER
UPPER_Y_BORDER = SCREEN_HEIGHT // 2
LOWER_Y_BORDER = - UPPER_Y_BORDER

SCREEN_COLOR = 'LightSkyBlue1'
MIN_PEN_SIZE = 1
MAX_PEN_SIZE = 4

DRAWING_SPEED = 100

POSSIBLE_COLORS = ['DarkMagenta', 'blue', 'purple', 'ForestGreen', 'firebrick1', 'yellow', 'black']


#*******************************************************************************************************************

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

    return random_radius


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

# five_circle_core_lambda = lambda start_x, start_y, biggest_radius: \
# circle_core(start_x, start_y, biggest_radius, circle_amount=5, circle_radius_delta=10)

    
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


def generate_max_within_screen_radius(start_x, start_y):
    max_valid_radius_list = [RIGHT_X_BORDER - start_x, start_x - LEFT_X_BORDER, UPPER_Y_BORDER - start_y, start_y - LOWER_Y_BORDER]
    max_valid_radius = min(max_valid_radius_list)

    return max_valid_radius


def generate_max_not_overlapping_radius(curr_x, curr_y, drawn_snowflake_info_list):
    max_possible_radius_list = []

    for snowflake_info in drawn_snowflake_info_list:
        prev_x, prev_y, prev_radius = snowflake_info
        curr_distance = sqrt(pow((curr_x - prev_x), 2) + pow((curr_y - prev_y), 2))
        possible_radius = int(curr_distance - prev_radius)
        max_possible_radius_list.append(possible_radius)

    max_valid_radius = MAX_SNOWFLAKE_RADIUS if not max_possible_radius_list else min(max_possible_radius_list)

    return max_valid_radius


def generate_max_valid_radius(start_x, start_y, drawn_snowflake_info_list):
    max_within_screen_radius = generate_max_within_screen_radius(start_x, start_y)
    max_not_overlapping_radius = generate_max_not_overlapping_radius(start_x, start_y, drawn_snowflake_info_list)

    max_valid_radius = min(max_within_screen_radius, max_not_overlapping_radius)
   
    return max_valid_radius

# Generates random x, y coors and radius
def generate_random_snowflake_coords():
    random_x = randint(LEFT_X_BORDER, RIGHT_X_BORDER)
    random_y = randint(LOWER_Y_BORDER, UPPER_Y_BORDER)

    return random_x, random_y


def main():
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT), t.Screen().bgcolor(SCREEN_COLOR)

    random_snowflake_amount = randint(MIN_SNOWFLAKE_AMOUNT, MAX_SNOWFLAKE_AMOUNT)
    drawn_snowflake_amount = 0
 
    # Every info set is a tuple with x, y coords and radius
    drawn_snowflake_info_list = []
  
    while drawn_snowflake_amount < random_snowflake_amount:
        max_valid_radius = 0

        while max_valid_radius < MIN_SNOWFLAKE_RADIUS:

            random_start_x, random_start_y = generate_random_snowflake_coords()
            max_valid_radius = generate_max_valid_radius(random_start_x, random_start_y, drawn_snowflake_info_list)

        random_radius = draw_random_snowflake(random_start_x, random_start_y, max_radius=max_valid_radius)
                      
        drawn_snowflake_info_list.append((random_start_x, random_start_y, random_radius))
        drawn_snowflake_amount += 1

            
    input()  

 
main()

    # snowflake(start_x, start_y, ray_amount, radius, branch_ray_two_leaves, lambda start_x, start_y, biggest_radius: \
    # circle_core(start_x, start_y, biggest_radius, circle_amount=5, circle_radius_delta=10))
    # snowflake(start_x, start_y, ray_amount, radius, circle_ray, circle_core)