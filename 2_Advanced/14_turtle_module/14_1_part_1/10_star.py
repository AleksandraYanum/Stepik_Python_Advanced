import turtle as t

def star(side):
    for _ in range(5):
        t.forward(side)
        t.right(144)


def main():
  side = 120
  star(side)
  

main()