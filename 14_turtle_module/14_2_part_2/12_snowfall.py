import turtle as t


def branch(start_x, start_y, branch_len, leave_amount):
    t.left(90)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    leave_distance = branch_len // (leave_amount + 2)
    leave_len = 50
    leave_angle = 45

    t.forward(branch_len)

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
    branch_len = 200
    leave_amount = 2
    branch(start_x, start_y, branch_len, leave_amount)
    input()


main()