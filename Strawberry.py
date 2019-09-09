import turtle
my_turtle = turtle.Turtle
turtle.speed(5)
turtle.bgcolor("sky blue")

"""
def is_point_in_shape(x, y, shape):
    if (x > shape_left) and (x < shape_right) and (y > shape_top) and (y > shape_bottom):
        return True
    else:
        return False

"""

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

def outline_point_seeds():
    for location in the_shape:# to draw seeds on each pt on outline
        if location < max(the_shape) and location > min(the_shape): 
            draw_seed(location)
            

# define highest x
# define highest y
# define lowest x
# define lowest y
  

def draw_berry_dos():
    straw_tri = {}
    
    draw_here = turtle.pos() # start pos
    face_this_way = turtle.heading() 

    turtle.goto(draw_here) # "start"
    straw_tri.update({"start": draw_here})
    turtle.setheading(face_this_way)
    
    turtle.color("red") 
    turtle.begin_poly() # create polygon
    turtle.begin_fill()
    turtle.circle(50, 180)
    
    point_1 = turtle.pos() # "first point"
    straw_tri.update({"first point" : point_1})
    turtle.lt(30) 
    turtle.forward(70)
    
    point_2 = turtle.pos() # "second point"
    straw_tri.update({"second point" : point_2})
    
    turtle.circle(20, 100)

    point_3 = turtle.pos() # "third point"
    straw_tri.update({"third point" : point_3})
    turtle.rt(30)
    turtle.goto(draw_here) # return to start
    
    turtle.end_fill()
    turtle.end_poly() # close polygon
    print(straw_tri)    

straw_tri = {
    'start': (0.00,0.00),
    'first point': (0.00,100.00),
    'second point': (-60.62,65.00),
    'third point': (-65.94,34.82)
        }
def tri_guide():
    turtle.color("gold")
    turtle.goto(straw_tri.get('start'))
    turtle.goto(straw_tri.get('first point'))
    print(turtle.heading())
    turtle.setheading(212.5)
    turtle.forward(90) # needs to be swapped out w/ variable
    
#update dict
    tip = turtle.pos() # add 'strawberry tip'
    straw_tri.update({"strawberry tip": tip})
    
    turtle.goto(straw_tri.get('start')) # finish "bottom triangle"
    
    turtle.setheading(45) # start "top triangle"
    turtle.forward(75) # needs height variable
    
#update dict
    
    top = turtle.pos()
    straw_tri.update({'top of berry': top})
    
    turtle.goto(straw_tri.get('first point')) # finish "top triangle"
    


draw_berry_dos()


tri_guide()



