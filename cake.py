import turtle
my_turtle = turtle.Turtle
turtle.speed(1)
turtle.bgcolor("sky blue")

top = (62,177)
base = (-150, -50)

side_start = (-162, -5)

def flatoval(r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
def rectangle(short, long):
    turtle.fd(short)
    turtle.rt(90)
    turtle.fd(long)
    turtle.rt(90)
    turtle.fd(short)
    turtle.rt(90)
    turtle.fd(long)

def candle(wax_color):
    turtle.color(wax_color)
    turtle.down()
    turtle.width(15)
    turtle.forward(45)
    turtle.width(10)
    turtle.color("yellow")
    turtle.forward(10)
    turtle.bk(5)
    turtle.width(5)
    turtle.color("orange")
    turtle.bk(5)
    turtle.color("red")
    turtle.fd(2)
    turtle.up()


"""
shape("circle")
shapesize(5,4,1)
fillcolor("white")
"""

turtle.up()
turtle.forward(500)
turtle.backward(500)
turtle.color("white")

#base of cake

turtle.goto(base)
turtle.begin_fill()
flatoval(150)
turtle.end_fill()

#icing
turtle.left(45)
turtle.color("pink")
turtle.down()
turtle.width(20)
flatoval(150)

turtle.color("white")
turtle.up()
#Sides of cake
turtle.lt(135)

turtle.goto(side_start)


turtle.begin_fill()
rectangle(145, 235)
turtle.end_fill()




#top of cake
turtle.goto(top)
turtle.begin_fill()
flatoval(150)
turtle.end_fill()




# top icing
turtle.left(45)
turtle.color("pink")
turtle.down()
turtle.width(20)
flatoval(150)


turtle.up()
turtle.goto(-15, 80)

turtle.rt(45)
turtle.down()
# candle
candle("Tomato")
turtle.goto(-85, 90)

candle("Salmon")
turtle.goto(-135, 130)

candle("gold")
turtle.goto(-95, 170)

candle("Medium Sea Green")
turtle.goto(-25, 170)

candle("Dark Turquoise")
turtle.goto(30, 130)

candle("Medium Slate Blue")

turtle.up()
turtle.fd(100)
