import turtle


def square(side):
  for _ in range(4):
    turtle.forward(side)
    turtle.left(90)


def main():    
  side = 120
  for _ in range(8):
    turtle.left(45)
    square(side)
    

main()