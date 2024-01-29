from turtle import *
from random import choice, randint
from math import sin, cos, tan, pi, sqrt, radians


SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

POLYGON_HEIGHT = 70
POLYGON_AREA = 5000


POLYGON_POSSIBLE_COLORS = ['yellow', 'lightblue', 'violet', 'orange', 'red', 'blue', 'green']

BORDER_DISTANCE = 50
POLYGON_DISTANCE = 30
POLYGON_CENTER_DISTANCE = POLYGON_HEIGHT + POLYGON_DISTANCE
POLYGON_AMOUNT_IN_ROW = 5
POLYGON_AMOUNT_IN_COL = 5
POLYGON_MIN_POSSIBLE_SIDE_AMOUNT = 3
POLYGON_MAX_POSSIBLE_SIDE_AMOUNT = 7

EQUAL_HEIGHT = 1
EQUAL_AREA = 2
# Choose one of the options above
DRAW_MODE = EQUAL_HEIGHT


def get_start_drawing_coords_angle(center_x, center_y, side_amount, side):
    turn_angle = 360 / side_amount
    excircle_radius = side / (2 * sin(pi / side_amount))
    if side_amount % 2 == 1:
        height = excircle_radius * (cos(pi / side_amount) + 1)
        start_turn_angle = 180 - turn_angle / 2
        start_x, start_y = center_x, center_y - height / 2  
    else:
        height = 2 * (side / (2* tan(pi / side_amount)))
        start_turn_angle = 0
        start_x, start_y = center_x - side / 2, center_y + height / 2
    
    return start_x, start_y, start_turn_angle


# For polygons with an odd number of sides (3, 5, 7), the starting point is the center of the bottom border
# For polygons with an even number of sides (4, 6) - the leftmost point lying on the upper boundary

def get_drawing_init_values(center_x, center_y, height, side_amount):
   
    turn_angle = 360 / side_amount
    if side_amount % 2 == 1:
        excircle_radius = height / (cos(pi / side_amount) + 1) # радиус описанной окружности
        side = 2 * excircle_radius * sin(pi / side_amount) 
        start_turn_angle = 180 - turn_angle / 2
        start_x, start_y = center_x, center_y - height / 2  # drawing starting coordinate
    else:
        side = 2 * (height / 2) * tan(pi / side_amount)
        start_turn_angle = 0
        start_x, start_y = center_x - side / 2, center_y + height / 2

    return start_x, start_y, start_turn_angle, side


def draw_polygon_by_side(center_x, center_y, side, side_amount, color):
    turn_angle = 360 / side_amount
    start_x, start_y, start_turn_angle = get_start_drawing_coords_angle(center_x, center_y, side_amount, side)

    penup() 
    setheading(start_turn_angle)
    setposition(start_x, start_y)
    fillcolor(color)
    pendown()
    begin_fill()
    for _ in range(side_amount): 
        forward(side)
        right(turn_angle)
    end_fill()


def draw_polygon_by_height(center_x, center_y, height, side_amount, color):
    turn_angle = 360 / side_amount
    start_x, start_y, start_turn_angle, side = get_drawing_init_values(center_x, center_y, height, side_amount)

    init_x, init_y = pos()
    penup() 
    setheading(start_turn_angle)
    setposition(start_x, start_y)
    fillcolor(color)
    pendown()
    begin_fill()
    for _ in range(side_amount): 
        forward(side)
        right(turn_angle)
    end_fill()
    penup()
    setposition(init_x, init_y) 


def draw_random_polygon_by_height(center_x, center_y, height, min_possible_side_amount, max_possible_side_amount, color):
    side_amount = randint(min_possible_side_amount, max_possible_side_amount)
    
    draw_polygon_by_height(center_x, center_y, height, side_amount, color)


def draw_random_polygon_by_area(center_x, center_y, area, min_possible_side_amount, max_possible_side_amount, color):
    side_amount = randint(min_possible_side_amount, max_possible_side_amount)
    side = sqrt(area * 4 * tan(radians(180) / side_amount) / side_amount)

    draw_polygon_by_side(center_x, center_y, side, side_amount, color)



def main():
    Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    speed(0) 

    first_polygon_center_x = - (SCREEN_WIDTH // 2 - BORDER_DISTANCE)  #center
    first_polygon_center_y = SCREEN_HEIGHT // 2 - BORDER_DISTANCE   #center
    curr_center_x, curr_center_y = first_polygon_center_x, first_polygon_center_y
   
    for _ in range(POLYGON_AMOUNT_IN_ROW):
        for _ in range(POLYGON_AMOUNT_IN_COL): 
            draw_random_polygon_by_area(center_x=curr_center_x, 
                                center_y=curr_center_y, 
                                area=POLYGON_AREA, 
                                min_possible_side_amount=POLYGON_MIN_POSSIBLE_SIDE_AMOUNT, 
                                max_possible_side_amount=POLYGON_MAX_POSSIBLE_SIDE_AMOUNT, 
                                color=choice(POLYGON_POSSIBLE_COLORS))
            curr_center_x += POLYGON_CENTER_DISTANCE
        curr_center_x = first_polygon_center_x
        curr_center_y -= POLYGON_CENTER_DISTANCE

    hideturtle()
    input()


main()

