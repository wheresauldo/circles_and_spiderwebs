import turtle
my_turtle = turtle.Turtle
turtle.speed(0)
turtle.bgcolor("light pink")
home = (0,0)
taco_length = 100
taco_width = 33

def square():
    turtle.down()
    
    for i in range(4):
        turtle.fd(20)
        turtle.left(90)
    turtle.up()
    
turtle.color("gold")
turtle.goto(home)
turtle.lt(90)

#back shell
turtle.begin_fill()
turtle.circle(taco_length, 180)
turtle.end_fill()

#fillings

#carne
turtle.color("sienna")

turtle.lt(45)


for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.lt(45)
    turtle.fd(20)
    

turtle.lt(180)

for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.lt(45)
    turtle.fd(20)

turtle.lt(45)

for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.lt(45)
    turtle.fd(20)

turtle.forward(20)

for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.lt(45)
    turtle.fd(15)

#lettuce

turtle.lt(90)
turtle.fd(30)
turtle.color("green")

for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.rt(30)
    turtle.fd(20)

turtle.lt(90)
turtle.fd(10)

for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.rt(45)
    turtle.fd(15)

# tomatoes

turtle.rt(170)
turtle.fd(30)
turtle.color("red")
turtle.bk(30)

for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.lt(20)
    turtle.fd(30)

turtle.rt(160)

for i in range(3):
    
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.rt(20)
    turtle.fd(30)


# front shell

# reposition

turtle.lt(105)
turtle.color("gold")
turtle.goto((taco_length/5), -(taco_width-10))
turtle.begin_fill()
turtle.circle(taco_length, 180)
turtle.end_fill()

#outline front shell
turtle.goto((taco_length/5), -(taco_width-10))
turtle.color("sandy brown")
turtle.down()
turtle.right(180)
turtle.circle(taco_length, 180)



turtle.up()
turtle.forward(100)
