import turtle as t


def lines(line_len, line_color='MediumAquamarine', dot_color='Blue', top_dot_color='Orange'):
  t.penup()
  t.goto(0, 100)
  for x_cor in range(-200, 201, 40):
    t.pendown()
    t.color(line_color)
    t.goto(x_cor, -line_len)
    t.color(dot_color)
    t.dot()
    t.penup()
    t.goto(0, 100)
    
  t.color(top_dot_color)
  t.dot()
  t.hideturtle()
  
  
def main():
  line_len = 150
  lines(line_len)
  
  
main()