import turtle as t
import itertools as it


def rectangle(width, height):
  for step, _ in zip(it.cycle([width, height]), range(4)):
    t.forward(step)
    t.left(90)


def main():
  width = 200
  height = 100
  rectangle(width, height)

main()