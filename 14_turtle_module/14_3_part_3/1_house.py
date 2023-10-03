import turtle as t


def shape(side, angle_amount):
  turn_angle = 360 / angle_amount
  for _ in range(angle_amount):
    t.forward(side)
    t.left(turn_angle)


def house(start_x, start_y, square_side, triangle_side):
  t.penup()
  t.goto(start_x, start_y)
  t.pendown()
  
  t.fillcolor('DodgerBlue')
  t.begin_fill()
  shape(square_side, angle_amount=4)
  t.end_fill()
  
  t.penup()
  t.goto(start_x - (triangle_side - square_side) / 2, start_y + square_side)
  t.pendown()

  t.fillcolor('Peru')
  t.begin_fill()
  shape(triangle_side, angle_amount=3)
  t.end_fill()



def main():
  triangle_side = 200
  square_side = 150
  start_x, start_y = 0, - 100
  house(start_x, start_y, square_side, triangle_side)
  
  
main()