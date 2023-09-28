import turtle as t


def david_star(triangle_side):
  angle_amount = 3
  shape(triangle_side, angle_amount)
  
  t.penup()
  t.goto(0, triangle_side * 0.6)
  t.pendown()

  is_up = 0
  shape(triangle_side, angle_amount, is_up)


def shape(side, angle_amount, is_up=1):
  turn_angle = 360 / angle_amount
  for _ in range(angle_amount):
    t.forward(side)
    if is_up:
      t.left(turn_angle)
    else:
      t.right(turn_angle)
      

def main():
  triangle_side = 200
  david_star(triangle_side)
  

main()