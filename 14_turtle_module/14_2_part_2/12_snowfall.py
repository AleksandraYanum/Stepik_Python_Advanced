import turtle as t
from math import ceil


GEAR_INNER_RADIUS_PERCENTAGE = 0.7


def snowflake(start_x, start_y, ray_amount, radius, ray_func, core_func):
    t.hideturtle(), t.speed(20)
    turn_angle = 360 / ray_amount

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    for _ in range(ray_amount):
        ray_func(start_x, start_y, radius)
        t.right(turn_angle)

    core_radius = radius // 4
    core_func(start_x, start_y, core_radius, ray_amount)

 
def branch_ray_two_leaves(start_x, start_y, ray_len):
    leave_amount = 2
    leave_len = ray_len / 4
    leave_angle = 45

    branch_ray_base(start_x, start_y, ray_len, leave_amount, leave_len, leave_angle)


def branch_ray_six_leaves(start_x, start_y, ray_len):
    leave_amount = 6
    leave_len = ray_len / 8
    leave_angle = 120

    branch_ray_base(start_x, start_y, ray_len, leave_amount, leave_len, leave_angle)
    

def branch_ray_base(start_x, start_y, ray_len, leave_amount, leave_len, leave_angle):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    leave_distance = ray_len // (leave_amount + 2)
    t.forward(ray_len)

    # Drawing branch leaves
    # TODO: use goto
    for _ in range(leave_amount):
        t.penup()
        t.backward(leave_distance)
        t.left(leave_angle)
        t.pendown()
        t.forward(leave_len)
        t.penup()
        t.backward(leave_len)
        t.right(leave_angle * 2)
        t.pendown()
        t.forward(leave_len)
        t.penup()
        t.backward(leave_len)
        t.left(leave_angle)


def line_ray(start_x, start_y, ray_len):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    t.forward(ray_len)


def circle_ray(start_x, start_y, ray_len):
    radius = ray_len / 2

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    t.circle(radius)


def five_circle_core(start_x, start_y, biggest_radius, ray_amount):
    circle_core(start_x, start_y, biggest_radius, circle_amount=5, circle_radius_delta=10)

# five_circle_core_lambda = lambda start_x, start_y, biggest_radius: \
# circle_core(start_x, start_y, biggest_radius, circle_amount=5, circle_radius_delta=10)

    
def circle_core(start_x, start_y, radius, circle_amount=1, circle_radius_delta=0):
    x, y = start_x, start_y - radius
    t.penup()
    t.goto(x, y)
    t.pendown()

    y_cor = y
    for _ in range(circle_amount):
        t.circle(radius)
        radius -= circle_radius_delta
        t.penup()
        y_cor += circle_radius_delta
        t.goto(x, y_cor)
        t.pendown()


def gear_circle(start_x, start_y, radius, ray_amount):
    gear_circle_base(start_x, start_y, radius, ray_amount, mid_radius=None)


def gear_circle_base(start_x, start_y, radius, ray_amount, mid_radius=None):

    mid_radius = mid_radius if mid_radius is not None else radius * GEAR_INNER_RADIUS_PERCENTAGE 
    turn_angle = 360 // ray_amount // 2
    point_list = []

    t.speed(20), t.hideturtle()
    t.penup()
    t.goto(start_x, start_y)

    lower_left_x = start_x + mid_radius
    lower_left_y = start_y

    for _ in range(ray_amount):
        t.right(turn_angle), t.forward(radius)
        top_x, top_y = [ceil(i) for i in t.pos()]

        t.backward(radius), t.right(turn_angle)
        t.forward(mid_radius)

        lower_right_x, lower_right_y = [ceil(i) for i in t.pos()]
        t.backward(mid_radius)

        point_list.extend([(lower_left_x, lower_left_y), (top_x, top_y), (lower_right_x, lower_right_y)])
        
        lower_left_x, lower_left_y = lower_right_x, lower_right_y

    point_list[-1] = point_list[0]

    t.penup()
    t.goto(point_list[0])
    t.pendown()

    for x, y in point_list[1:]:
        t.goto(x, y)
    input()


def main():
    start_x, start_y = 0, 0
    ray_amount = 8
    radius = 200

    snowflake(start_x, start_y, ray_amount, radius, branch_ray_two_leaves, five_circle_core)
    # snowflake(start_x, start_y, ray_amount, radius, branch_ray_two_leaves, lambda start_x, start_y, biggest_radius: \
    # circle_core(start_x, start_y, biggest_radius, circle_amount=5, circle_radius_delta=10))


    # snowflake(start_x, start_y, ray_amount, radius, circle_ray, circle_core)
    input()

 
main()