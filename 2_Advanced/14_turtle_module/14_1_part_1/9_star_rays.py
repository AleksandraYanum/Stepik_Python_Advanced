import turtle as t


def star_rays(ray_size, ray_amount=12):
  turn_angle = 360 / ray_amount
  for i in range(ray_amount):
      t.forward(ray_size)
      t.backward(ray_size)
      t.right(turn_angle)


def main():
  ray_size = 100
  star_rays(ray_size)


main()