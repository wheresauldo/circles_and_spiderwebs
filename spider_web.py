# Spider Web

import turtle
my_turtle = turtle.Turtle
turtle.speed(0)

turtle.bgcolor("black")
turtle.color("white")
home = (0, 10)
not_home = (-10, 20)

"""

def draw_base(leg_num, length):
    angle = (360/leg_num)
    turtle.up()
    turtle.goto(home)
    turtle.right(angle)
    turtle.down()
    turtle.forward(length)
    turtle.penup()
    
# Draw supports    
for leg_num in range(8):
    draw_base(8, 500)
    
turtle.up()
#turtle.goto(8, 16)
turtle.goto(home)
turtle.right(90)
turtle.pendown()
"""

# draw bars
"""for i in range(200):
    turtle.right(90)
    turtle.circle((5+(i*2)), 45)"""


# Draw Spiral
"""for i in range(198):
  turtle.circle(10+i, 45)"""


# Draw Concentric Circles

"""
for i in range(30):
  turtle.circle(10*i)
  turtle.up()
  turtle.sety((10*i)*(-1))
  turtle.down()

"""
"""
for i in range(30):
  turtle.circle((10*i), 45)
  turtle.up()
  turtle.sety((10*i)*(-1))
  turtle.down()
  """
# Draw tangent circles
"""
for i in range(10):
    turtle.circle(10*i) """



"""
for i in range(7):
    turtle.right(90)
    turtle.circle(20, 40)
    
turtle.up()
turtle.forward(15)
turtle.down()
for i in range(10):
    turtle.right(90)
    turtle.circle(30, 50)
"""

"""
turtle.right(90)
turtle.circle(20, 40)
"""

#Code for building radical thread
# default num_rad= 6 default len_rad = 150

def radical_thread(num_rad,len_rad):
    for i in range(num_rad):
      turtle.forward(len_rad)
      turtle.backward(len_rad)
      turtle.right(360/num_rad)
 
#Code for building spiral thread

# assumes 6 radicals, 60dg angle, side = 150
def spiral(side):
    for i in range(15):
      turtle.penup()
      turtle.goto(0,0)
      turtle.pendown()
      turtle.setheading(0)
      turtle.forward(side)
      turtle.right(120) # make variable
      for j in range(6):
        turtle.forward(side)
        turtle.right(60)
        side = side - 10

radical_thread(6,150)
for i in range(15):
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(side)
    turtle.right(120) # make variable
    for j in range(6):
        turtle.forward(side)
        turtle.right(60)
        side = side - 10
#spiral(150)


turtle.up()
turtle.forward(100)
