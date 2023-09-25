import turtle as t


def turtle_circle(ray_size, ray_amount=12):
  t.penup()
  t.shape('turtle')
  t.shapesize(1)
  t.pensize(5)
  t.stamp()

  turn_angle = 360 / ray_amount
  line_len = 20
  empty_line_len = 30
  bakward_len_dif = line_len + empty_line_len
  for i in range(ray_amount):
      t.forward(ray_size)
      t.pendown()
      t.forward(line_len)
      t.penup()
      t.forward (empty_line_len)

      t.stamp()
      t.backward(ray_size + bakward_len_dif)
      t.right(turn_angle)


def main():
  ray_amount = 12
  ray_size = 120
  turtle_circle(ray_size, ray_amount)



main()