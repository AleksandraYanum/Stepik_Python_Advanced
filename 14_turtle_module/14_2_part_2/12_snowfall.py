import turtle as t


def snowflake(start_x, start_y, ray_amount, radius, ray_func):
    t.hideturtle()
    turn_angle = 360 / ray_amount

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    for _ in range(ray_amount):
        ray_func(start_x, start_y, radius)
        t.right(turn_angle)


def branch_ray(start_x, start_y, branch_len):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    leave_amount = 2
    leave_len = 50
    leave_angle = 45
    leave_distance = branch_len // (leave_amount + 2)

    t.forward(branch_len)

    # Drawing branch leaves
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


def main():
    start_x, start_y = 0, 0
    ray_amount = 8
    radius = 200

    snowflake(start_x, start_y, ray_amount, radius, branch_ray)
    input()

 
main()