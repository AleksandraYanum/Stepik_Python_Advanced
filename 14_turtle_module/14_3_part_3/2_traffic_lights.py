import turtle as t
from itertools import cycle


TRAFFIC_LIGHTS_COLORS = ['red', 'yellow', 'green']
TRAFFIC_LIGHTS_RECTANGLE_COLOR = 'black'

DRAWING_SPEED = 10

def traffic_lights(start_x, start_y, width, height, circle_amount=3):
   small_rectangle_height = height // circle_amount

   # Distance from the next circle
   circle_distance = small_rectangle_height // 3
   radius = small_rectangle_height // 2 - circle_distance // 2

   t.hideturtle(), t.fillcolor(TRAFFIC_LIGHTS_RECTANGLE_COLOR)
   
   t.begin_fill()
   rectangle(start_x, start_y, width, height)
   t.end_fill()

   x = start_x + width // 2
   y = start_y + small_rectangle_height * (circle_amount - 1) + circle_distance // 2

   circle_color_line(x, y, radius, circle_amount, TRAFFIC_LIGHTS_COLORS, y_offset=-(radius*2+circle_distance))


def circle_color_line(start_x, start_y, radius, amount, colors, x_offset=0, y_offset=0):
    x_cor, y_cor = start_x, start_y
    t.hideturtle()
    for _, color in zip(range(amount), cycle(colors)):
        t.fillcolor(color)
        t.penup()
        t.goto(x_cor, y_cor)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        
        x_cor += x_offset
        y_cor += y_offset


def rectangle(start_x, start_y, width, height):
  t.penup()
  t.goto(start_x, start_y)
  t.pendown()

  angle_amount = 4
  turn_angle = 360 / angle_amount
  for step, _ in zip(cycle([width, height]), range(angle_amount)):
    t.forward(step)
    t.left(turn_angle)


def main():
    t.speed(DRAWING_SPEED)

    start_x, start_y = -50, -150
    width = 200
    height = 400

    traffic_lights(start_x, start_y, width, height)

    input()


main()