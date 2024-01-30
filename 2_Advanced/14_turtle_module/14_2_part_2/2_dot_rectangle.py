import turtle as t
import itertools as it


def dot_rectangle(width, height, dot_size=20):
  for step, _ in zip(it.cycle([width, height]), range(4)):
    t.forward(step)
    t.left(90)
    t.dot(dot_size)


def main():
  width = 200
  height = 100
  dot_rectangle(width, height)


main()  