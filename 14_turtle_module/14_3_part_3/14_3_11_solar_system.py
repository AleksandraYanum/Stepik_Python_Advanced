import turtle as t


SOLAR_SYSTEM_OBJECTS = {'sun': {'relative_radius': 1, 'color': 'yellow', 'text': 'Солнце'},
                        'mercury': {'relative_radius': 0.3, 'color': 'peru', 'text': 'Меркурий'},
                        'venus': {'relative_radius': 0.4, 'color': 'peru', 'text': 'Венера'},
                        'earth': {'relative_radius': 0.3, 'color': 'spring green', 'text': 'Земля'},
                        'mars': {'relative_radius': 0.2, 'color': 'dark orange', 'text': 'Марс'},
                        'jupiter': {'relative_radius': 0.6, 'color': 'peru', 'text': 'Юпитер'},
                        'saturn': {'relative_radius': 0.6, 'color': 'peru', 'is_ring': True, 'text': 'Сатурн'},
                        'uranus': {'relative_radius': 0.5, 'color': 'sky blue', 'text': 'Уран'},
                        'neptune': {'relative_radius': 0.5, 'color': 'blue', 'text': 'Нептун'},
                        'pluto': {'relative_radius': 0.1, 'color': 'peru', 'text': 'Плутон'}
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
        planet_radius = sun_radius * planet_info['relative_radius']
        planet_color = planet_info['color']
        planet_name = planet_info['text']

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