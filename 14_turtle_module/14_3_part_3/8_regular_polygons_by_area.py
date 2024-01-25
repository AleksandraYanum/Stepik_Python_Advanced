from turtle import *
from random import shuffle, randint
from math import sin, cos, tan, pi


SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

POLYGON_HEIGHT = 70

# The amount of colors is not less than the amount of polygons in a row
POLYGON_POSSIBLE_COLORS = ['yellow', 'lightblue', 'violet', 'orange', 'red', 'blue', 'green']

BORDER_DISTANCE = 50
POLYGON_DISTANCE = 30
POLYGON_CENTER_DISTANCE = POLYGON_HEIGHT + POLYGON_DISTANCE
POLYGON_AMOUNT_IN_ROW = 5
POLYGON_AMOUNT_IN_COL = 5
POLYGON_MIN_POSSIBLE_SIDE_AMOUNT = 3
POLYGON_MAX_POSSIBLE_SIDE_AMOUNT = 7


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


def calculate_polygon_dimensions_by_height(center_x, center_y, side_amount, height):

    # For polygons with an odd number of sides (3, 5, 7), the starting point is the center of the bottom border
    # For polygons with an even number of sides (4, 6) - the leftmost point lying on the upper boundary
    
    turn_angle = 360 / side_amount
    if side_amount % 2 == 1:
        excircle_radius = height / (cos(pi / side_amount) + 1) # радиус описанной окружности
        side = 2 * excircle_radius * sin(pi / side_amount) 
        start_turn_angle = 180 - turn_angle / 2
        start_x, start_y = center_x, center_y - height / 2  # drawing sratrting coordinate
    else:
        side = 2 * (height / 2) * tan(pi / side_amount)
        start_turn_angle = 0
        start_x, start_y = center_x - side / 2, center_y + height / 2

    return start_x, start_y, side, start_turn_angle

  
def draw_random_polygon(center_x, center_y, height, min_possible_side_amount, max_possible_side_amount, color):
    side_amount = randint(min_possible_side_amount, max_possible_side_amount)
    start_x, start_y, side, start_turn_angle = calculate_polygon_dimensions_by_height(center_x, center_y, side_amount, height)
    draw_polygon(start_x=start_x, 
                 start_y=start_y, 
                 start_turn_angle=start_turn_angle, 
                 side_amount=side_amount, 
                 side=side, 
                 color=color)

    return side


def main():
    Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    speed(0) 

    first_polygon_center_x = - (SCREEN_WIDTH // 2 - BORDER_DISTANCE)  #center
    first_polygon_center_y = SCREEN_HEIGHT // 2 - BORDER_DISTANCE   #center
    curr_center_x, curr_center_y = first_polygon_center_x, first_polygon_center_y
   
    for _  in range(POLYGON_AMOUNT_IN_ROW):
        shuffle(POLYGON_POSSIBLE_COLORS)
        for polygon_in_row in range(POLYGON_AMOUNT_IN_COL): 
            draw_random_polygon(center_x=curr_center_x, 
                                center_y=curr_center_y, 
                                height=POLYGON_HEIGHT, 
                                min_possible_side_amount=POLYGON_MIN_POSSIBLE_SIDE_AMOUNT, 
                                max_possible_side_amount=POLYGON_MAX_POSSIBLE_SIDE_AMOUNT, 
                                color=POLYGON_POSSIBLE_COLORS[polygon_in_row])
            curr_center_x += POLYGON_CENTER_DISTANCE
        curr_center_x = first_polygon_center_x
        curr_center_y -= POLYGON_CENTER_DISTANCE

    hideturtle()
    input()


main()