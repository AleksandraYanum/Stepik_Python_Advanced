import itertools as it
import turtle as t

def rhombus(side):
    for angle, _ in zip(it.cycle([120, 60]), range(4)):
        t.forward(side)
        t.left(angle)
    
    
def main():
  side = 120
  rhombus(side)
  

main()