import turtle as t
from random import randint, randrange, choice
from itertools import cycle

#*******************************************************************************************************************

SKY_COLOR = 'midnight blue'
STAR_COLOR = 'gold'
# BUILDING_COLOR = 'RoyalBlue4'
BUILDING_POSSIBLE_COLORS = ['RoyalBlue4', 'SlateBlue4', 'SlateGray', 'DarkOliveGreen', 'salmon4']
LIGHT_WINDOW_COLOR = 'gold'
NO_LIGHT_WINDOW_COLOR = 'medium blue'

MIN_STAR_SIZE = 2
MAX_STAR_SIZE = 7

WINDOW_SIZE = 30
WINDOW_DISTANCE = WINDOW_SIZE // 2
ALL_ONE_WINDOW_SPACE = WINDOW_SIZE + WINDOW_DISTANCE * 2

SCREEN_WIDTH = 15 * ALL_ONE_WINDOW_SPACE
SCREEN_HEIGHT = 10 * ALL_ONE_WINDOW_SPACE

MIN_BUILDING_WIDTH = 1 * ALL_ONE_WINDOW_SPACE
MIN_BUILDING_HEIGHT = 1 * ALL_ONE_WINDOW_SPACE
MAX_BUILDING_HEIGHT = SCREEN_HEIGHT - ALL_ONE_WINDOW_SPACE

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

    building_amount = 5
    # randint(MIN_BUILDING_AMOUNT, MAX_BUILDING_AMOUNT)

    drawn_building_width = 0
    window_possible_colors = [LIGHT_WINDOW_COLOR, NO_LIGHT_WINDOW_COLOR]
    building_possible_colors = cycle(BUILDING_POSSIBLE_COLORS)

# BUILDINGS DRAWING
    for i in range(building_amount - 1):
        max_curr_building_width = SCREEN_WIDTH - drawn_building_width - (building_amount - i - 1) * MIN_BUILDING_WIDTH

        curr_building_width, curr_building_height = \
            draw_random_building(building_start_x, building_start_y, MIN_BUILDING_WIDTH, max_curr_building_width, ALL_ONE_WINDOW_SPACE,
                                 MIN_BUILDING_HEIGHT, MAX_BUILDING_HEIGHT, ALL_ONE_WINDOW_SPACE, next(building_possible_colors))

# WINDOWS DRAWING
        window_amount_in_height = curr_building_height // ALL_ONE_WINDOW_SPACE
        window_amount_in_width = curr_building_width // ALL_ONE_WINDOW_SPACE

        window_start_x = building_start_x + WINDOW_DISTANCE
        curr_window_start_y = building_start_y + WINDOW_DISTANCE

        draw_building_windows(window_start_x, curr_window_start_y, window_amount_in_height, window_amount_in_width,
                              WINDOW_SIZE, WINDOW_DISTANCE, window_possible_colors)

        drawn_building_width += curr_building_width
        building_start_x += curr_building_width

# LAST BUILDING DRAWING
    curr_building_width = SCREEN_WIDTH - drawn_building_width
    curr_building_height = randrange(MIN_BUILDING_HEIGHT, MAX_BUILDING_HEIGHT, ALL_ONE_WINDOW_SPACE)

    draw_building(building_start_x, building_start_y, curr_building_width, curr_building_height, next(building_possible_colors))

    window_amount_in_height = curr_building_height // ALL_ONE_WINDOW_SPACE
    window_amount_in_width = curr_building_width // ALL_ONE_WINDOW_SPACE
    window_start_x = building_start_x + WINDOW_DISTANCE
    curr_window_start_y = building_start_y + WINDOW_DISTANCE

    draw_building_windows(window_start_x, curr_window_start_y, window_amount_in_height, window_amount_in_width,
                              WINDOW_SIZE, WINDOW_DISTANCE, window_possible_colors)

    input()


def draw_building_windows(start_x, start_y, amount_in_height, amount_in_width, size, distance, possible_colors):

    curr_start_y = start_y
    for _ in range(amount_in_height):
            curr_start_x = start_x

            for _ in range(amount_in_width):
                t.penup()
                t.goto(curr_start_x, curr_start_y)
                t.pendown()
                color = choice(possible_colors)
                square(size, color)
                curr_start_x += size + distance * 2

            curr_start_y += size + distance * 2


def draw_random_building(start_x, start_y, min_width, max_width, step_width, min_height, max_height, step_height, color):

    random_width = randrange(min_width, max_width + 1, step_width)
    random_height = randrange(min_height, max_height, step_height)
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