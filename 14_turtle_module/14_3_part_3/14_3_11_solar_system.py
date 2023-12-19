import turtle as t

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

PLANET_DISTANCE = 30
TEXT_DISTANCE = 20
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

def main():
    t.Screen().colormode(255)
    t.Screen().setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    t.hideturtle(), t.penup()

    sun_radius = 100

    # left central coords
    x = -SCREEN_WIDTH // 2 + PLANET_DISTANCE
    y = 0


    for planet_info in SOLAR_SYSTEM_OBJECTS.values():
        planet_radius = sun_radius * planet_info[RELATIVE_RADIUS]
        planet_color = planet_info[COLOR]
        planet_name = planet_info[TEXT]

        start_x = x + planet_radius
        start_y = y - planet_radius

        t.goto(start_x, start_y)
        t.pendown()
        t.fillcolor(planet_color)
        t.begin_fill()
        t.circle(planet_radius)
        t.end_fill()
        t.penup()
        t.goto(start_x, start_y - TEXT_DISTANCE)
        t.write(planet_name, align='center', font=('Arial', 10, 'normal'))
        x = start_x + planet_radius + PLANET_DISTANCE


    input()

main() 