import turtle as t

#*******************************************************************************************************************

SKY_COLOR = 'midnight blue'
STAR_COLOR = 'gold'
HOUSE_COLOR = 'blue'
LIGHT_WINDOW_COLOR = 'gold'
NO_LIGHT_WINDOW_COLOR = 'medium blue'

MIN_STAR_SIZE = 2
MAX_STAR_SIZE = 7

WINDOW_SIZE = 20
WINDOW_DISTANCE = WINDOW_SIZE // 2
ALL_ONE_WINDOW_SPACE = WINDOW_SIZE * 2

SCREEN_WIDTH = 30 * ALL_ONE_WINDOW_SPACE
SCREEN_HEIGHT = 20 * ALL_ONE_WINDOW_SPACE

MIN_HOUSE_HEIGHT = 1 * ALL_ONE_WINDOW_SPACE
MAX_HOUSE_HEIGHT = SCREEN_HEIGHT - ALL_ONE_WINDOW_SPACE

MIN_HOUSE_AMOUNT = 3
MAX_HOUSE_AMOUNT = 10

#*******************************************************************************************************************

def main():
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    t.Screen().colormode(255)
    t.Screen().bgcolor(SKY_COLOR)
    t.hideturtle()
    
    input()


main()