import turtle as t


def shape(side, angle_count=6):
    turn_angle = 360 / angle_count
    for _ in range(angle_count):
        t.forward(side)
        t.right(turn_angle)


def honeycomb(side):
  for _ in range(6):
    shape(side)
    t.forward(side)
    t.left(60)


def main():
  honeycomb(50)
    
    
main()