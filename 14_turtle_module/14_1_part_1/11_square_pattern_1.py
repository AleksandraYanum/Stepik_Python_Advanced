import turtle as t


def square_pattern(smallest_side, square_amount, step):
  side = smallest_side
  for _ in range(square_amount):
    square(side)
    side += step

  
def square(side):
  for _ in range(4):
    t.left(90)
    t.forward(side)
    

def main():
  smallest_side, square_amount, step = 20, 31, 10
  square_pattern(smallest_side,square_amount, step)


main()