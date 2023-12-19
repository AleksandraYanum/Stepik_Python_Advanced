import turtle as t
from math import radians, sin, cos

RELATIVE_RADIUS = 'relative_radius'
COLOR = 'color'
TEXT = 'text'
IS_RING = 'is_ring'

SOLAR_SYSTEM_OBJECTS = {'sun': {RELATIVE_RADIUS: 1, COLOR: 'yellow', TEXT: 'Солнце'},
                        'mercury': {RELATIVE_RADIUS: 0.3, COLOR: 'peru', TEXT: 'Меркурий'},
                        'venus': {RELATIVE_RADIUS: 0.4, COLOR: 'peru', TEXT: 'Венера'},
                        'earth': {RELATIVE_RADIUS: 0.3, COLOR: 'spring green', TEXT: 'Земля'},
                        'mars': {RELATIVE_RADIUS: 0.2, COLOR: 'dark orange', TEXT: 'Марс'},
                        'jupiter': {RELATIVE_RADIUS: 0.6, COLOR: 'peru', TEXT: 'Юпитер'},
                        'saturn': {RELATIVE_RADIUS: 0.6, COLOR: 'peru', IS_RING: True, TEXT: 'Сатурн'},
                        'uranus': {RELATIVE_RADIUS: 0.5, COLOR: 'sky blue', TEXT: 'Уран'},
                        'neptune': {RELATIVE_RADIUS: 0.5, COLOR: 'blue', TEXT: 'Нептун'},
                        'pluto': {RELATIVE_RADIUS: 0.1, COLOR: 'peru', TEXT: 'Плутон'}
                        }

PLANET_DISTANCE = 50
TEXT_DISTANCE = 20
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 650

def main():
    t.Screen().colormode(255)
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    t.hideturtle(), t.penup(), t.tracer(0)

    sun_radius = 100

    # left central coords
    x = -SCREEN_WIDTH // 2 + PLANET_DISTANCE
    y = 0


    for planet_info in SOLAR_SYSTEM_OBJECTS.values():
        planet_radius = sun_radius * planet_info[RELATIVE_RADIUS]
        planet_color = planet_info[COLOR]
        planet_name = planet_info[TEXT]
        is_ring = planet_info.get(IS_RING)

        start_x = x + planet_radius
        start_y = y - planet_radius

        t.goto(start_x, start_y)
        t.pendown()
        t.fillcolor(planet_color)
        t.begin_fill()
        t.circle(planet_radius)
        t.end_fill()

        if is_ring is not None:
            el_x = start_x
            el_y = start_y + planet_radius // 2
            horizontal_radius = planet_radius * 1.5
            vertical_radius = planet_radius // 2
            ellipse(el_x, el_y, horizontal_radius, vertical_radius)
        
        t.penup()
        t.goto(start_x, start_y - TEXT_DISTANCE)
        t.write(planet_name, align='center', font=('Arial', 10, 'normal'))
        x = start_x + planet_radius + PLANET_DISTANCE


    input()

def ellipse(x, y, horizontal_radius, vertical_radius, color='black', fill=''):
    t.penup()
    t.goto(x, y)
    t.color(color, fill)
    t.begin_fill()
    t.pendown()
    for deg in range(361):
        rad = radians(deg)
        curr_x = horizontal_radius * sin(rad) + x
        curr_y = -vertical_radius * cos(rad) + vertical_radius + y
        t.goto(curr_x, curr_y)
    t.end_fill()
 

main() 