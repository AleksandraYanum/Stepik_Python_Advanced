import turtle as t

EXTERNAL_BORDER_COLOR = 'black'
INTERNAL_BORDER_COLOR = 'white'
STOP_COLOR = 'red'
TEXT_COLOR = 'white'
COLORS = [EXTERNAL_BORDER_COLOR, INTERNAL_BORDER_COLOR, STOP_COLOR]

STOP_SIDE_LEN = 150
STOP_SIZE_DIF = 10


def shape(side, angle_count=6):
    turn_angle = 360 / angle_count
    for _ in range(angle_count):
        t.forward(side)
        t.right(turn_angle)


def main():

    t.speed(10), t.hideturtle(), t.up()

    side_len = STOP_SIDE_LEN
    start_x, start_y = -STOP_SIDE_LEN // 2, STOP_SIDE_LEN

    x, y = start_x, start_y
    for color in range(len(COLORS)):
        t.up(), t.goto(x, y), t.down()
        t.pencolor(COLORS[color])
        
        t.fillcolor(COLORS[color])
        t.begin_fill()
        shape(side_len, 8)
        t.end_fill() 

        side_len -= STOP_SIZE_DIF
        x += STOP_SIZE_DIF // 2
        y -= STOP_SIZE_DIF

    t.up()
    t.goto(start_x + STOP_SIDE_LEN // 2, start_y - STOP_SIDE_LEN * 1.5)
    t.pencolor('white')
    t.write('STOP', align='center', font=('Arial', STOP_SIDE_LEN // 2, 'normal'))

    input()


main()

