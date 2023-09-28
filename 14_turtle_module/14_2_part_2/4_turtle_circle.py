import turtle as t


def turtle_circle(ray_size, ray_amount=12):
  t.penup()
  t.shape('turtle')
  t.shapesize(2)
  t.stamp()
  t.hideturtle()

  turn_angle = 360 / ray_amount
  for i in range(ray_amount):
      t.forward(ray_size)
      t.stamp()
      t.backward(ray_size)
      t.right(turn_angle)


def main():
  ray_amount = 10
  ray_size = 120
  turtle_circle(ray_size, ray_amount)



main()