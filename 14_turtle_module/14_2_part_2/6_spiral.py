import turtle as t


def spiral(turtle_amount):
  t.penup()
  for distance in range(1, turtle_amount):
    t.stamp()
    t.forward(distance)
    t.right(20)
    
    

def main():
  t.shape('turtle')
  t.Screen().bgcolor('light green')
  turtle_amount = 61
  spiral(turtle_amount)
  
  
main()