import turtle as t
from itertools import cycle


def colorful_pattern(colors, line_amount):
  pensize = 1
  forward_len = 5
  
  for _, color in zip(range(line_amount), cycle(colors)):
    t.left(45)
    t.pencolor(color)
    t.pensize(pensize)
    t.forward(forward_len)
    pensize += 0.5
    forward_len += 3
    
  
def main():
  colors = ['blue', 'yellow', 'green', 'purple', 'orange',  'red']
  line_amount = 44
  colorful_pattern(colors, line_amount)
  
  
main()