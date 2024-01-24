from turtle import *
from random import shuffle, randint
from math import sin, cos, tan, pi


SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

POLYGON_POSSIBLE_COLORS = ['yellow', 'lightblue', 'violet', 'orange', 'red', 'blue', 'green']
BORDER_DISTANCE = 50
POLYGON_DISTANCE = 30
POLYGON_AMOUNT_IN_ROW = 5
POLYGON_AMOUNT_IN_COL = 5
POLYGON_MIN_POSSIBLE_SIDE_AMOUNT = 3
POLYGON_MAX_POSSIBLE_SIDE_AMOUNT = 7
POLYGON_HEIGHT = 70


def draw_polygon(start_x, start_y, start_turn_angle, side_amount, side, color):
    turn_angle = 360 / side_amount
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


def get_polygon_info_by_side_amount(center_x, center_y, side_amount, height):
    # For polygons with an odd number of sides (3, 5, 7), the starting point is the center of the bottom border
    # For polygons with an even number of sides (4, 6) - the leftmost point lying on the upper boundary
    
    turn_angle = 360 / side_amount

    if side_amount % 2 == 1:
        сircumcircle_radius = height / (cos(pi / side_amount) + 1) # радиус описанной окружности
        side = 2 * сircumcircle_radius * sin(pi / side_amount) 
        start_turn_angle = 180 - turn_angle / 2
        start_x, start_y = center_x, center_y - height / 2  # drawing sratrting coordinate
    else:
        side = 2 * (height / 2) * tan(pi / side_amount)
        start_turn_angle = 0
        start_x, start_y = center_x - side / 2, center_y + height / 2

    return start_x, start_y, side, start_turn_angle


def main():
    Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    speed(0) 

    polygon_center_distance = POLYGON_HEIGHT + POLYGON_DISTANCE
    first_polygon_center_x = - (SCREEN_WIDTH // 2 - BORDER_DISTANCE)  #center
    first_polygon_center_y = SCREEN_HEIGHT // 2 - BORDER_DISTANCE   #center

    for polygon_in_row in range(POLYGON_AMOUNT_IN_ROW):
        shuffle(POLYGON_POSSIBLE_COLORS)
        for polygon_in_col in range(POLYGON_AMOUNT_IN_COL): 
            curr_polygon_side_amount = randint(POLYGON_MIN_POSSIBLE_SIDE_AMOUNT, POLYGON_MAX_POSSIBLE_SIDE_AMOUNT)
            curr_polygon_color = POLYGON_POSSIBLE_COLORS[polygon_in_col]
            curr_polygon_center_x = first_polygon_center_x + polygon_center_distance * polygon_in_col 
            curr_polygon_center_y = first_polygon_center_y - polygon_center_distance * polygon_in_row
            
            curr_start_x,  curr_start_y, curr_polygon_side, curr_start_turn_angle = \
            get_polygon_info_by_side_amount(center_x=curr_polygon_center_x, 
                                            center_y=curr_polygon_center_y, 
                                            side_amount=curr_polygon_side_amount, 
                                            height=POLYGON_HEIGHT)
            draw_polygon(start_x=curr_start_x, 
                         start_y=curr_start_y, 
                         start_turn_angle=curr_start_turn_angle, 
                         side_amount=curr_polygon_side_amount, 
                         side=curr_polygon_side, 
                         color=curr_polygon_color)

    hideturtle()
    input()


main()

