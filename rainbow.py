import turtle
my_turtle = turtle.Turtle
turtle.speed(0)
turtle.bgcolor("Deep Sky Blue")


home = (0,0)
width = 20
red_start = (100, 0)
orange_start = (82, 0)
yellow_start = (64, 0)
green_start = (46, 0)
blue_start = (28, 0)
purple_start = (10, 0)

all_colors = ["red", "Dark Orange", "yellow", "Lime Green", "blue", "purple"]

#print(all_colors[0])



# first color start position  == 1/2 radius
# start_position = ((previous_start - width)+ 2)
# next_color radius == ((previous_color - width)+ 2)


draw_rainbow(200, 180, 20)
    
#Rainbow
# red
"""turtle.width(width)

turtle.up()
turtle.goto(red_start)



turtle.left(90)
turtle.color("red")
turtle.down()
turtle.circle(200, 180)
"""

"""
turtle.up()
turtle.goto(orange_start)
turtle.down()

turtle.right(180)
turtle.color("Dark Orange")
turtle.circle(182, 180)

turtle.up()
turtle.goto(yellow_start)
turtle.down()

turtle.right(180)
turtle.color("yellow")
turtle.circle(164, 180)

turtle.up()
turtle.goto(green_start)
turtle.down()

turtle.right(180)
turtle.color("Lime Green")
turtle.circle(146, 180)

turtle.up()
turtle.goto(blue_start)
turtle.down()

turtle.right(180)
turtle.color("blue")
turtle.circle(128, 180)

turtle.up()
turtle.goto(purple_start)
turtle.down()

turtle.right(180)
turtle.color("Dark Violet")
turtle.circle(110, 180)

#Clouds

turtle.up()
turtle.goto(red_start)
turtle.right(90)
turtle.forward(60)

def draw_cloud(big_cir, big_ang, small_cir, small_ang):
    turtle.color("white")
    turtle.down()
    turtle.begin_fill()
    for i in range(7):
        turtle.circle(big_cir, big_ang)
        turtle.right(90)
        turtle.circle(small_cir, small_ang)
        turtle.right(90)
    turtle.end_fill()

def big_cloud(big_cir, big_ang, small_cir, small_ang, distance):
for i in range(4):
draw_cloud(big_cir, big_ang, small_cir, small_ang)
turtle.bk(50)

draw_cloud(40, 120, 20, 110)
turtle.bk(50)
draw_cloud(40, 120, 20, 110)
turtle.bk(50)

turtle.up()
turtle.goto(red_start)
turtle.right(120)
turtle.backward(250)

draw_cloud(40, 120, 20, 110)
turtle.bk(50)
draw_cloud(40, 120, 20, 110)
turtle.bk(50)
draw_cloud(40, 120, 20, 110)
turtle.bk(50)

"""
