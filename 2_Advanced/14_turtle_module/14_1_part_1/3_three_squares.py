import turtle

def several_squares(side, count=3, angle=22.5):
  for _ in range(count):
    turtle.left(angle)
    square(side)
    
    
def square(side):
    for _ in range(4):
      turtle.forward(side)
      turtle.left(90)
    
  
def main():  
  side = int(input('Square side is '))
  several_squares(side)
  
  
main()