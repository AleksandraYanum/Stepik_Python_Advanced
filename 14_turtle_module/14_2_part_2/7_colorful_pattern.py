import turtle as t


def colorful_pattern(colors, line_amount):
  color_amount = len(colors)

  pensize = 1
  forward_len = 5
  
  for i in range(line_amount):
    t.left(45)
    t.pencolor(colors[i % color_amount])
    t.pensize(pensize)
    t.forward(forward_len)
    pensize += 0.5
    forward_len += 3
    
  

def main():
  colors = ['blue', 'yellow', 'green', 'purple', 'orange',  'red']
  line_amount = 44
  colorful_pattern(colors, line_amount)
  
  
main()