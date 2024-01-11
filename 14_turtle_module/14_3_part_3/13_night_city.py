# BUILDINGS ARE DRAWN FROM ONE SCREEN SIDE TO OTHER AND ON THE LOWER Y SCREEN BORDER

import turtle as t
from random import randint, randrange, choice
from itertools import cycle

#*******************************************************************************************************************

SKY_COLOR = 'midnight blue'
STAR_COLOR = 'gold'
BUILDING_POSSIBLE_COLORS = ['RoyalBlue4', 'SlateBlue4', 'SlateGray', 'DarkOliveGreen', 'salmon4']
BUILDING_POSSIBLE_COLORS = cycle(BUILDING_POSSIBLE_COLORS)
LIGHT_WINDOW_COLOR = 'gold'
NO_LIGHT_WINDOW_COLOR = 'medium blue'
wINDOW_POSSIBLE_COLORS = [LIGHT_WINDOW_COLOR, NO_LIGHT_WINDOW_COLOR]

MIN_STAR_DIAMETER = 4
MAX_STAR_DIAMETER = 8
STAR_AMOUNT = 100

WINDOW_SIZE = 30
WINDOW_DISTANCE = WINDOW_SIZE // 2
WINDOW_BLOCK_HEIGHT = WINDOW_SIZE + WINDOW_DISTANCE * 2
WINDOW_BLOCK_WIDTH = WINDOW_SIZE + WINDOW_DISTANCE * 2

SCREEN_WIDTH = 15 * WINDOW_BLOCK_WIDTH
SCREEN_HEIGHT = 10 * WINDOW_BLOCK_HEIGHT

MIN_BUILDING_WIDTH = 1 * WINDOW_BLOCK_WIDTH
MIN_BUILDING_HEIGHT = 1 * WINDOW_BLOCK_HEIGHT
MAX_BUILDING_HEIGHT = SCREEN_HEIGHT - WINDOW_BLOCK_HEIGHT

MIN_BUILDING_AMOUNT = 5
MAX_BUILDING_AMOUNT = 15

#*******************************************************************************************************************

def main():
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    t.Screen().colormode(255)
    t.Screen().bgcolor(SKY_COLOR)
    t.hideturtle(), t.tracer(0)
    
    building_start_x = - SCREEN_WIDTH // 2
    building_start_y = - SCREEN_HEIGHT // 2 

    # building_amount = 5
    building_amount = randint(MIN_BUILDING_AMOUNT, MAX_BUILDING_AMOUNT)

    drawn_building_width = 0
    curr_building_start_x, curr_building_start_y = building_start_x, building_start_y

# STARS DRAWING
    draw_random_stars(STAR_AMOUNT, MIN_STAR_DIAMETER, MAX_STAR_DIAMETER, STAR_COLOR, building_start_x, -building_start_x, building_start_y, -building_start_y)

# BUILDINGS DRAWING
    for i in range(building_amount - 1):
        max_curr_building_width = SCREEN_WIDTH - drawn_building_width - (building_amount - i - 1) * MIN_BUILDING_WIDTH

        curr_building_width, curr_building_height = \
            draw_random_building(curr_building_start_x, curr_building_start_y, MIN_BUILDING_WIDTH, max_curr_building_width, WINDOW_BLOCK_WIDTH,
                                 MIN_BUILDING_HEIGHT, MAX_BUILDING_HEIGHT, WINDOW_BLOCK_HEIGHT, next(BUILDING_POSSIBLE_COLORS))
        
# WINDOWS DRAWING
        window_vertical_amount = curr_building_height // WINDOW_BLOCK_HEIGHT
        window_horizontal_amount = curr_building_width // WINDOW_BLOCK_WIDTH

        window_start_x = curr_building_start_x + WINDOW_DISTANCE
        curr_window_start_y = curr_building_start_y + WINDOW_DISTANCE

        draw_building_windows(window_start_x, curr_window_start_y, window_vertical_amount, window_horizontal_amount,
                              WINDOW_SIZE, WINDOW_BLOCK_HEIGHT, WINDOW_BLOCK_WIDTH, wINDOW_POSSIBLE_COLORS)

        drawn_building_width += curr_building_width
        curr_building_start_x += curr_building_width

# LAST BUILDING DRAWING
    curr_building_width = SCREEN_WIDTH - drawn_building_width
    curr_building_height = randrange(MIN_BUILDING_HEIGHT, MAX_BUILDING_HEIGHT, WINDOW_BLOCK_HEIGHT)

    draw_building(curr_building_start_x, curr_building_start_y, curr_building_width, curr_building_height, next(BUILDING_POSSIBLE_COLORS))
  
    window_vertical_amount = curr_building_height // WINDOW_BLOCK_HEIGHT
    window_horizontal_amount = curr_building_width // WINDOW_BLOCK_WIDTH
    window_start_x = curr_building_start_x + WINDOW_DISTANCE
    curr_window_start_y = curr_building_start_y + WINDOW_DISTANCE

    draw_building_windows(window_start_x, curr_window_start_y, window_vertical_amount, window_horizontal_amount,
                              WINDOW_SIZE, WINDOW_BLOCK_HEIGHT, WINDOW_BLOCK_WIDTH, wINDOW_POSSIBLE_COLORS)

    input()


def draw_random_stars(amount, min_diameter, max_diameter, color, left_x_border, right_x_border, lower_y_border, upper_y_border):
    for _ in range(amount):
        random_diameter = randint(min_diameter, max_diameter)
        x, y = generate_random_coords_within_screen(left_x_border, right_x_border, lower_y_border, upper_y_border)
        t.up()
        t.goto(x, y)
        t.dot(random_diameter, color)


def generate_random_coords_within_screen(left_x_border, right_x_border, lower_y_border, upper_y_border):
    x = randint(left_x_border, right_x_border)
    y = randint(lower_y_border, upper_y_border)
    return x, y


def draw_building_windows(start_x, start_y, vertical_amount, horizontal_amount, size, block_height, block_width, possible_colors):

    curr_start_y = start_y
    for _ in range(vertical_amount):
            curr_start_x = start_x

            for _ in range(horizontal_amount):
                t.penup()
                t.goto(curr_start_x, curr_start_y)
                t.pendown()
                color = choice(possible_colors)
                square(size, color)
                curr_start_x += block_width

            curr_start_y += block_height


def draw_random_building(start_x, start_y, min_width, max_width, window_block_width, min_height, max_height, window_block_height, color):

    random_width = randrange(min_width, max_width + 1, window_block_width)
    random_height = randrange(min_height, max_height + 1, window_block_height)
    draw_building(start_x, start_y, random_width, random_height, color)

    return random_width, random_height


def draw_building(start_x, start_y, width, height, color):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    rectangle(width, height, color)


def rectangle(width, height, fill_color='black'):
    t.color(fill_color)
    t.begin_fill()
    for step, _ in zip(cycle([width, height]), range(4)):
        t.forward(step)
        t.left(90)
    t.end_fill()


def square(width, fill_color='black'):
    height = width
    rectangle(width, height, fill_color)


main()