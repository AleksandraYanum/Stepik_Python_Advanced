import turtle


def square_pattern(smallest_side, square_amount, step):
  side = smallest_side
  for _ in range(square_amount):
    square(side)
    side += step

  
def square(side):
  for _ in range(4):
    turtle.left(90)
    turtle.forward(side)
    

def main():
  smallest_side, square_amount, step = 20, 31, 10
  square_pattern(smallest_side,square_amount, step)


main()