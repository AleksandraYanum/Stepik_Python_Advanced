import turtle as t


CRESCENT_COLOR = 'orange'
SKY_COLOR = 'blue'
SPEED_DELTA = 5


def moon(start_x, start_y, radius, color):
    t.penup()
    t.goto(start_x, start_y)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def main():
    t.hideturtle(), t.penup(), t.tracer(0)
    t.bgcolor(SKY_COLOR)

    start_x, start_y = 0, -50
    crescent_radius = 120
    crescent_diameter = crescent_radius * 2

    while True:
        for i in range(0, crescent_radius * 4, SPEED_DELTA):
            x = start_x + crescent_diameter - i

            moon(start_x, start_y, crescent_radius, CRESCENT_COLOR)
            moon(x, start_y, crescent_radius, SKY_COLOR)

            t.update()
        
    
main()


