import turtle as t
from random import randint, randrange
from itertools import cycle

#*******************************************************************************************************************

SKY_COLOR = 'midnight blue'
STAR_COLOR = 'gold'
HOUSE_COLOR = 'RoyalBlue4'
LIGHT_WINDOW_COLOR = 'gold'
NO_LIGHT_WINDOW_COLOR = 'medium blue'

MIN_STAR_SIZE = 2
MAX_STAR_SIZE = 7

WINDOW_SIZE = 30
WINDOW_DISTANCE = WINDOW_SIZE // 2
ALL_ONE_WINDOW_SPACE = WINDOW_SIZE + WINDOW_DISTANCE * 2

SCREEN_WIDTH = 15 * ALL_ONE_WINDOW_SPACE
SCREEN_HEIGHT = 10 * ALL_ONE_WINDOW_SPACE

MIN_HOUSE_WIDTH = 1 * ALL_ONE_WINDOW_SPACE
MIN_HOUSE_HEIGHT = 1 * ALL_ONE_WINDOW_SPACE
MAX_HOUSE_HEIGHT = SCREEN_HEIGHT - ALL_ONE_WINDOW_SPACE

MIN_HOUSE_AMOUNT = 5
MAX_HOUSE_AMOUNT = 15

#*******************************************************************************************************************

def main():
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    t.Screen().colormode(255)
    t.Screen().bgcolor(SKY_COLOR)
    t.hideturtle(), t.tracer(0)
    
    start_x = - SCREEN_WIDTH // 2
    start_y = - SCREEN_HEIGHT // 2

    house_amount = 5
    # randint(MIN_HOUSE_AMOUNT, MAX_HOUSE_AMOUNT)
    drawn_house_width = 0

    for i in range(house_amount - 1):
        max_curr_house_width = SCREEN_WIDTH - drawn_house_width - (house_amount - i - 1) * MIN_HOUSE_WIDTH
        curr_house_width = randrange(MIN_HOUSE_WIDTH, max_curr_house_width + 1, ALL_ONE_WINDOW_SPACE)
        curr_house_height = randrange(MIN_HOUSE_HEIGHT, MAX_HOUSE_HEIGHT, ALL_ONE_WINDOW_SPACE)

        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        rectangle(curr_house_width, curr_house_height, HOUSE_COLOR)

        drawn_house_width += curr_house_width
        start_x += curr_house_width

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    
    curr_house_width = SCREEN_WIDTH - drawn_house_width
    curr_house_height = randrange(MIN_HOUSE_HEIGHT, MAX_HOUSE_HEIGHT, ALL_ONE_WINDOW_SPACE)

    rectangle(curr_house_width, curr_house_height, color=HOUSE_COLOR)



    input()


def rectangle(width, height, color='black'):
    t.color(color)
    t.begin_fill()
    for step, _ in zip(cycle([width, height]), range(4)):
        t.forward(step)
        t.left(90)
    t.end_fill()


main()