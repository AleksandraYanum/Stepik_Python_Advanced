import turtle as t


def square_pattern(smallest_side, biggest_side, step):
  for side in range(smallest_side, biggest_side, step):
    t.left(90)
    t.forward(side)
    
    
def main():
  smallest_side, biggest_side, step = 10, 195, 5
  square_pattern(smallest_side, biggest_side, step)
  
  
main()
