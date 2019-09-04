import turtle
my_turtle = turtle.Turtle
turtle.speed(0)
turtle.bgcolor("Deep Sky Blue")
# leaf spike
def leaf_spike():
    turtle.circle(50, 50)
    turtle.lt(120)
    turtle.circle(50, 50)

# strawberry top - all leaves

def strawberry_top(berry_top):
    turtle.setpos(top_of_berry)
    turtle.color("green")
    for i in range(6):
        turtle.begin_fill()
        turtle.circle(50, 50)
        turtle.lt(120)
        turtle.circle(50, 50)
        turtle.rt(70)
        turtle.end_fill()

# strawberry seed

def draw_seed(location):
        turtle.goto(location)
        turtle.rt(90)
        turtle.color("gold")
        turtle.begin_fill()
        turtle.circle(2, 180)
        turtle.lt(30)
        turtle.forward(3)
        turtle.circle(1, 100)
        turtle.rt(30)
        turtle.goto(location)
        turtle.end_fill()
        turtle.back(25)
        return turtle.pos()

# while get new pos == area of strawberry

 
    
# set position
# color
# fill/pen down
# draw shape/shape part
# leave without accidental marks

#STRAWBERRY
start_point = 0,0
top_of_berry = (40, 50)
first_seed = 2, 4

#berry
def draw_berry(draw_here):
    turtle.setpos(start_point)
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.lt(30)
    turtle.forward(70)
    turtle.circle(20, 100)
    turtle.rt(30)
    turtle.goto(start_point)
    turtle.end_fill()






    
draw_berry(start_point)
strawberry_top(top_of_berry)
turtle.up()
draw_seed(first_seed)

#draw_seed(second_seed)


"""
turtle.up()
turtle.fd(100)
"""
