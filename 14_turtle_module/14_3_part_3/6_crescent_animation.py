import turtle as t


CRESCENT_COLOR = 'orange'
SKY_COLOR = 'blue'
SPEED_DELTA = 20


def main():
    t.hideturtle(), t.penup()

    start_x, start_y = 0, -50
    crescent_diameter = 400
    t.bgcolor(SKY_COLOR)

    while True:

        t.goto(start_x, start_y)
        t.dot(crescent_diameter, CRESCENT_COLOR)         

        x = start_x + crescent_diameter    
        
        for _ in range(crescent_diameter // SPEED_DELTA):
            x -= SPEED_DELTA
            t.goto(x, start_y)
            t.dot(crescent_diameter, SKY_COLOR)

        t.goto(start_x, start_y)
        t.dot(crescent_diameter, CRESCENT_COLOR)  

        x = start_x - crescent_diameter  

        for _ in range(crescent_diameter // SPEED_DELTA):
            x += SPEED_DELTA
            t.goto(x, start_y)
            t.dot(crescent_diameter, SKY_COLOR)      



    input()


main()


