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

def strawberry_top():
    turtle.setpos(straw_tri.get("top of berry"))
    turtle.color("green")
    for i in range(6):
        turtle.begin_fill()
        turtle.circle(50, 50)
        turtle.lt(120)
        turtle.circle(50, 50)
        turtle.rt(70)
        turtle.end_fill()

my_strawberry = []

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
    my_strawberry = turtle.get_poly()
    print(my_strawberry)

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
    for location in my_strawberry:# to draw seeds on each pt on outline
        if location < max(my_strawberry) and location > min(my_strawberry):
            draw_seed(location)


# define highest x
# define highest y
# define lowest x
# define lowest y


def draw_berry_dos(top_size, bottom_size):
    straw_tri = {}

    draw_here = turtle.pos() # start pos
    face_this_way = turtle.heading()

    turtle.goto(draw_here) # "start"
    straw_tri.update({"start": draw_here})
    turtle.setheading(face_this_way)

    turtle.color("red")
    turtle.begin_poly() # create polygon
    turtle.begin_fill()
    turtle.circle(top_size, 180)

    point_1 = turtle.pos() # "first point"
    straw_tri.update({"first point" : point_1})
    turtle.lt(30)
    turtle.forward(70)

    point_2 = turtle.pos() # "second point"
    straw_tri.update({"second point" : point_2})

    turtle.circle(bottom_size, 100)


    point_3 = turtle.pos() # "third point"
    straw_tri.update({"third point" : point_3})
    turtle.rt(30)
    turtle.goto(draw_here) # return to start

    turtle.end_fill()
    turtle.end_poly() # close polygon
    my_strawberry = turtle.get_poly()
    return(straw_tri)
shapes_dict = {}
straw_tri = {
    'start': (0.0, 0.0),
    'second point': (-60.62, 65.0),
    'top of berry': (53.03,53.03),
    'strawberry tip': (-75.91,51.64),
    'third point': (-65.94, 34.82),
    'first point': (0.0, 100.0)
    }
tri_guide_dict = {}

def tri_guide():
    turtle.color("gold")
    turtle.begin_poly() # return a, b, c
    turtle.goto(straw_tri.get('start'))

    a1 = turtle.pos()# a
    tri_guide_dict.update({"A1": a1})

    turtle.goto(straw_tri.get('first point'))

    b1 = turtle.pos() # b
    tri_guide_dict.update({"B1": b1})

    turtle.setheading(212.5)
    turtle.forward(90) # needs to be swapped out w/ variable

#update dict
    tip = turtle.pos() # add 'strawberry tip'
    straw_tri.update({"strawberry tip": tip})

    c1 = turtle.pos() # c
    tri_guide_dict.update({"C1": c1})

    turtle.goto(straw_tri.get('start')) # finish "bottom triangle" - return to a
    turtle.end_poly()
    guide_one = turtle.get_poly()

    turtle.begin_poly() # start - a2

    a2 = turtle.pos()# a
    tri_guide_dict.update({"A2": a2})

    turtle.setheading(45) # start "top triangle"
    turtle.forward(75) # needs height variable

#update dict

    top = turtle.pos() # top -  b2
    straw_tri.update({'top of berry': top})

    b2 = turtle.pos() # b
    tri_guide_dict.update({"B2": b2})

    turtle.goto(straw_tri.get('first point')) # c2 - finish "top triangle"

    c2 = turtle.pos() # c
    tri_guide_dict.update({"C2": c2})

    turtle.end_poly()
    guide_two = turtle.get_poly()
    return(tri_guide_dict)


tri_guide_dict = {
    "top triangle":{ # add guide
        'A1': (0.00,0.00),
        'B1': (0.00,100.00),
        'C1': (-75.91,51.64)
        },
    "bottom triangle" : { # add guide
        'A2': (0.00,0.00),
        'B2': (53.03,53.03),
        'C2': (0.00,100.00),
    }

    }

def find_area(a_key, b_key, c_key):
    # ax(by-cy) + bx(cy-ay) + cx(ay-by)
    #
    tri_guide_dict.get( {which_triangle: a_key: (x, y)})
    print(a_key)
    print(b_key)
    print(c_key)



draw_berry_dos(50, 20)
tri_guide()

tri_guide_dict.get("top triangle")

#outline_point_seeds()
#strawberry_top()
raw_input('Press RETURN to exit')
