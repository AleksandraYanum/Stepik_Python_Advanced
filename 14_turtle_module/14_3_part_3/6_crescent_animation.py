import turtle as t


CRESCENT_COLOR = 'orange'
SKY_COLOR = 'blue'
SPEED_DELTA = 5


def moon(start_x, start_y, radius):
    t.penup()
    t.goto(start_x, start_y)
    t.fillcolor(CRESCENT_COLOR)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
 

def moon_shadow(start_x, start_y, radius, i): 
    x = start_x + radius * 2
    t.goto(x - i, start_y) 
    t.fillcolor(SKY_COLOR)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def main():
    t.hideturtle(), t.penup(), t.tracer(0)
    t.bgcolor(SKY_COLOR)

    start_x, start_y = 0, -50
    crescent_radius = 120

    while True:
        for i in range(0, crescent_radius * 4, SPEED_DELTA):
            moon(start_x, start_y, crescent_radius)
            moon_shadow(start_x, start_y, crescent_radius, i)
            t.update()
        
    
main()


