import turtle


def triangle(side):
  for _ in range(3):
    turtle.left(120)
    turtle.forward(side)


def main():
  side = int(input('Triangle side is '))
  triangle(side)


main()  