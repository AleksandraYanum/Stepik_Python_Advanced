import turtle as t


def dot_line(dot_amount=10, dot_size=40):
  t.penup()
  t.backward(300)
  for _ in range(dot_amount):
    t.dot(dot_size)
    t.penup()
    t.forward(50)


def main():
  t.shape('turtle')
  dot_line()
  

main()