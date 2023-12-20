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

WINDOW_SIZE = 20
WINDOW_DISTANCE = WINDOW_SIZE // 2
ALL_ONE_WINDOW_SPACE = WINDOW_SIZE * 2

SCREEN_WIDTH = 30 * ALL_ONE_WINDOW_SPACE
SCREEN_HEIGHT = 20 * ALL_ONE_WINDOW_SPACE

MIN_HOUSE_WIDTH = 1 * ALL_ONE_WINDOW_SPACE
MIN_HOUSE_HEIGHT = 1 * ALL_ONE_WINDOW_SPACE
MAX_HOUSE_HEIGHT = SCREEN_HEIGHT - ALL_ONE_WINDOW_SPACE

MIN_HOUSE_AMOUNT = 3
MAX_HOUSE_AMOUNT = 15

#*******************************************************************************************************************

def main():
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    t.Screen().colormode(255)
    t.Screen().bgcolor(SKY_COLOR)
    t.hideturtle(), t.tracer(0)
    
    start_x = - SCREEN_WIDTH // 2
    start_y = - SCREEN_HEIGHT // 2

    house_amount = randint(MIN_HOUSE_AMOUNT, MAX_HOUSE_AMOUNT)
    house_height = 600
    drawn_house_width = 0


    for i in range(1, house_amount):
        max_house_width = SCREEN_WIDTH - (house_amount - i)

        t.penup()
        t.goto(start_x, start_y)
        t.pendown()

        house_width = randrange(MIN_HOUSE_WIDTH, max_house_width, ALL_ONE_WINDOW_SPACE)
        rectangle(house_width, house_height, fill_color=HOUSE_COLOR)

        drawn_house_width += house_width
        start_x = start_x + house_width

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    
    last_house_width = SCREEN_WIDTH - drawn_house_width
    rectangle(last_house_width, house_height, fill_color=HOUSE_COLOR)


    input()


def rectangle(width, height, *, border_color='black', fill_color=''):
    t.color(border_color, fill_color)
    t.begin_fill()
    for step, _ in zip(cycle([width, height]), range(4)):
        t.forward(step)
        t.left(90)
    t.end_fill()


main()