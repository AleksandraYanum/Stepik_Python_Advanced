# TODO: make david star drawing with perfect positions

import turtle as t
from math import cos, pi


def david_star(triangle_side, angle_amount=6):
  turn_angle = 360 / angle_amount
  radius = int(triangle_side / 2 / cos(turn_angle / 2 * pi / 180))

  shape(triangle_side, int(angle_amount / 2))

  t.hideturtle()
  t.penup()
  t.left(turn_angle / 2)
  t.forward(radius)  
  t.left(turn_angle * 2)
  t.forward(radius)  
  t.right(turn_angle * 2 + turn_angle / 2)
  t.pendown()
  t.showturtle()

  shape(triangle_side, int(angle_amount / 2), 0)


def shape(side, angle_amount, is_up=1):
  turn_angle = 360 / angle_amount
  rotate = t.left if is_up else t.right
  for _ in range(angle_amount):
    t.forward(side)
    rotate(turn_angle)

      
def main():
  triangle_side = 200
  david_star(triangle_side)
  

main()