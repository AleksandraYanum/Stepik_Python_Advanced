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


def main():
    Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    speed(0) 

    polygon_height = 70
    polygon_center_distance = polygon_height + POLYGON_DISTANCE
    first_polygon_center_x = - (SCREEN_WIDTH // 2 - BORDER_DISTANCE)  #center
    first_polygon_center_y = SCREEN_HEIGHT // 2 - BORDER_DISTANCE   #center

    penup() 
    for polygon_in_row in range(POLYGON_AMOUNT_IN_ROW):
        shuffle(POLYGON_POSSIBLE_COLORS)
        for polygon_in_col in range(POLYGON_AMOUNT_IN_COL): 
            curr_polygon_side_amount = randint(POLYGON_MIN_POSSIBLE_SIDE_AMOUNT, POLYGON_MAX_POSSIBLE_SIDE_AMOUNT)
            curr_polygon_color = POLYGON_POSSIBLE_COLORS[polygon_in_col]

            curr_polygon_center_x = first_polygon_center_x + polygon_center_distance * polygon_in_col 
            curr_polygon_center_y = first_polygon_center_y - polygon_center_distance * polygon_in_row
            curr_polygon_turn_angle = 360 / curr_polygon_side_amount
            
            fillcolor(curr_polygon_color)

            # For polygons with an odd number of sides (3, 5, 7), the starting point is the center of the bottom border
            # For polygons with an even number of sides (4, 6) - the leftmost point lying on the upper boundary

            if curr_polygon_side_amount % 2 == 1:
                curr_сircumcircle_radius = polygon_height / (cos(pi / curr_polygon_side_amount) + 1) # радиус описанной окружности
                curr_polygon_side = 2 * curr_сircumcircle_radius * sin(pi / curr_polygon_side_amount) 
                curr_start_x, curr_start_y = curr_polygon_center_x, curr_polygon_center_y - polygon_height / 2  # drawing sratrting coordinate
                curr_drawing_turn_angle = 180 - curr_polygon_turn_angle / 2
                setheading(curr_drawing_turn_angle)
            else:
                curr_polygon_side = 2 * (polygon_height / 2) * tan(pi / curr_polygon_side_amount)
                curr_start_x, curr_start_y = curr_polygon_center_x - curr_polygon_side / 2, curr_polygon_center_y + polygon_height / 2
                setheading(0)
            
            # DRAWING 
            setposition(curr_start_x, curr_start_y)
            pendown()
            begin_fill()
            for _ in range(curr_polygon_side_amount): 
                forward(curr_polygon_side)
                right(curr_polygon_turn_angle)
            end_fill()
            penup()


    hideturtle()
    input()








main()

