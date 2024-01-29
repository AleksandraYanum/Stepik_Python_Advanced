from itertools import cycle
import turtle as t

def rhombus(side):
    for angle, _ in zip(cycle([60, 120]), range(4)):
        t.forward(side)
        t.left(angle)

def snowflake(side, rhombus_amount=10):
    turn_angle = 360 / rhombus_amount
    for _ in range(rhombus_amount):
       t.right(turn_angle)
       rhombus(side)
    
    
def main():
    side = 120
    snowflake(side)


main()