import turtle as t


def lines(start_x, start_y, line_amount, height, dot_distance, 
          line_color='MediumAquamarine', dot_color='Blue', top_dot_color='Orange'):
  
  t.hideturtle(), t.speed(20)
  t.penup()
  t.goto(start_x, start_y)
  end_y = start_y - height
  dots_len = (line_amount - 1) * dot_distance
  x_cor = int(start_x - dots_len / 2)
  t.color(line_color)
  
  for _ in range(line_amount):
    t.pendown()
    t.color(line_color)
    t.goto(x_cor, end_y)
    t.color(dot_color)
    t.dot()
    t.penup()
    t.goto(start_x, start_y)
    x_cor += dot_distance


  t.color(top_dot_color)
  t.dot()


def main():
  height = 300
  line_amount = 10
  dot_distance = 50
  start_x, start_y = -50, 200
  lines(start_x, start_y, line_amount, height, dot_distance)
  
  
main()