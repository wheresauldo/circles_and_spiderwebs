import turtle
my_turtle = turtle.Turtle
turtle.speed(0)
turtle.bgcolor("Deep Sky Blue")

# goto start
# color
# fill/pen down
# draw shape/shape part
# leave without accidental marks

#STRAWBERRY
start_point = 0,0

turtle.goto(start_point)

#berry

turtle.begin_fill()
turtle.color("red")
turtle.circle(50, 180)
turtle.lt(30)
turtle.forward(70)
turtle.circle(20, 100)
turtle.rt(30)
turtle.goto(start_point)
turtle.end_fill()

# leaf spikes
"""
turtle.color("green")
turtle.circle(100, 36)
turtle.lt(180)
turtle.circle(100, 36)
"""
