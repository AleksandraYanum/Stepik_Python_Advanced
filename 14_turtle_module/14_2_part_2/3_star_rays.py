import turtle as t


def star_rays(ray_size, ray_amount=12):
  turn_angle = 360 / ray_amount
  t.hideturtle()
  for _ in range(ray_amount):
      t.forward(ray_size)
      t.stamp()
      t.backward(ray_size)
      t.right(turn_angle)


def main():
  t.shape('triangle')
  ray_amount = int(input())
  ray_size = 120
  t.dot(20)
  star_rays(ray_size, ray_amount)



main()