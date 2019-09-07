import turtle
my_turtle = turtle.Turtle
turtle.speed(5)
turtle.bgcolor("sky blue")

def is_point_in_shape(x, y, shape):
    if (x > shape_left) and (x < shape_right) and (y > shape_top) and (y > shape_bottom):
        return True
    else:
        return False

    
"""def do_shapes_overlap():
    for a, b in [(rec_1, rec_2), (rec_2, rec_1)]:
        if ()"""

start_point = 0,0
start_point = 0,0
top_of_berry = (40, 50)

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
        
def draw_berry(draw_here):
    turtle.setpos(draw_here)
    turtle.color("red")
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.lt(30)
    turtle.forward(70)
    turtle.circle(20, 100)
    turtle.rt(30)
    turtle.goto(draw_here)
    turtle.end_fill()
    turtle.end_poly()
    the_shape = turtle.get_poly()
    return(the_shape)

def draw_seed(location):
        turtle.up()
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


shape_coordinates = []

# define highest x
# define highest y
# define lowest x
# define lowest y
  

def draw_berry_dos(draw_here):
    turtle.setpos(draw_here)
    turtle.color("red")
    turtle.begin_poly() # create polygon
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.lt(30)
    turtle.forward(70)
    turtle.circle(20, 100)
    turtle.rt(30)
    turtle.goto(draw_here)
    turtle.end_fill()
    turtle.end_poly() # close polygon
    the_shape = turtle.get_poly()
    print(the_shape)
    shape_coordinates.append(the_shape)
    turtle.backward(70)
    for location in the_shape:# to draw seeds, need to return area, not outline
        if location < max(the_shape) and location > min(the_shape): 
            draw_seed(location)

draw_berry_dos(start_point)
strawberry_top(top_of_berry)



#draw_berry_dos(start_point)

