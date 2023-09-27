import turtle as t


def shape(side, angle_amount):
  turn_angle = 360 / angle_amount
  for _ in range(angle_amount):
    t.forward(side)
    t.left(turn_angle)


def house(square_side, triangle_side):
  x = -50
  y = - 200
  
  t.penup()
  t.goto(x, y)
  t.pendown()
  
  t.fillcolor('DodgerBlue')
  t.begin_fill()
  shape(square_side, angle_amount=4)
  t.end_fill()
  
  t.penup()
  t.goto(x - (triangle_side - square_side) / 2, y + square_side)
  t.pendown()

  t.fillcolor('Peru')
  t.begin_fill()
  shape(triangle_side, angle_amount=3)
  t.end_fill()



def main():
  triangle_side = 220
  square_side = 140
  house(square_side, triangle_side)
  
  
main()