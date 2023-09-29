import turtle as t


def david_star(triangle_side, compression_percent=0.6):
  angle_amount = 3
  shape(triangle_side, angle_amount)
  
  t.penup()
  t.goto(0, triangle_side * compression_percent)
  t.pendown()

  is_up = 0
  shape(triangle_side, angle_amount, is_up)


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