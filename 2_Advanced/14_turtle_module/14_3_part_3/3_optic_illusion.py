import turtle as t
from math import cos, sin,pi
from itertools import cycle


FILLING_TRIANGLE_COLOR = 'white'
FILLING_CIRCLE_COLOR = 'black'
UP_TRIANGLE_COLOR = 'black'
DOWN_TRIANGLE_COLOR = 'white'
PENSIZE = 3
DRAWING_SPEED = 10


def david_star_with_circles(start_x, start_y, triangle_side, circle_radius):
  angle_amount = 6
  turn_angle = 360 / angle_amount
  radius = int(triangle_side / 2 / cos(turn_angle / 2 * pi / 180))
  
  # First up triangle
  t.pensize(PENSIZE)
  t.pencolor(UP_TRIANGLE_COLOR)
  t.penup()
  t.goto(start_x, start_y)
  t.pendown()
  shape(triangle_side, int(angle_amount / 2))

  t.penup()
  t.left(turn_angle / 2)
  t.forward(radius)  
  t.left(turn_angle * 2)
  t.forward(radius)  
  t.right(turn_angle * 2 + turn_angle / 2)

  # Drawing circles
  x, y = t.pos()
  triangle_by_circles(x, y, triangle_side, circle_radius)
  
  # Second down triangle
  t.goto(x, y)
  t.pendown()
  t.pencolor(DOWN_TRIANGLE_COLOR), t.fillcolor(FILLING_TRIANGLE_COLOR)
  t.begin_fill()
  shape(triangle_side, int(angle_amount / 2), 0)
  t.end_fill()


def shape(side, angle_amount, is_up=1):
  turn_angle = 360 / angle_amount
  rotate = t.left if is_up else t.right
  for _ in range(angle_amount):
    t.forward(side)
    rotate(turn_angle)


def triangle_by_circles(start_x, start_y, triangle_side, circle_radius):
  angle_amount = 3
  t.penup()
  t.goto(start_x, start_y - circle_radius)
  t.fillcolor(FILLING_CIRCLE_COLOR), t.begin_fill()
  t.circle(circle_radius)
  t.end_fill()

  t.goto(start_x + triangle_side, start_y - circle_radius)
  t.begin_fill()
  t.circle(circle_radius)
  t.end_fill()

  triangle_angle = 180 / angle_amount
  t.goto(start_x + (triangle_side * cos(triangle_angle * pi / 180)), \
        start_y - triangle_side * sin(triangle_angle * pi / 180) - circle_radius)
  t.begin_fill()
  t.circle(circle_radius)
  t.end_fill()

     
def main():
  t.hideturtle(), t.speed(DRAWING_SPEED)
  triangle_side = 300
  radius = 50
  start_x, start_y = -100, -100
  david_star_with_circles(start_x, start_y, triangle_side, radius)

  input()

main()