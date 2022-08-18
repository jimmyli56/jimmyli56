# Create a flag challenge program - created by Christopher Bell - modified from Art Simon
import turtle

# create a new turtle object called tia
tia = turtle.Turtle() 
# make tia's initial shape a turtle, look up what other shape turtles can be
tia.shape("turtle") 
# initialize tia's draw speed to be 10
tia.speed(5)

# fill the background green using begin_fill() and end_fill()
tia.color('blue')
tia.begin_fill()
tia.goto(200,100)
tia.goto(50,-100)
tia.goto(-10,-100)
tia.goto(-100,100)
tia.goto(200,100)
tia.end_fill()
tia.penup()
# make tia go back home
tia.goto(40,-15)
# change tia's color to blue
tia.color('yellow')
tia.pendown()
# make a circle - note where the circle starts - where is the center?
tia.begin_fill()
tia.circle(50)
tia.end_fill()
# what other shapes can you draw with?

# where could I move and draw another circle to make it look like a doughnut? How about a cresent moon?

# display some text
tia.color('black')
tia.penup()
# why am I picking the pen up? What would happen if I didn't?
tia.goto(0, -90)
tia.pendown()
tia.hideturtle()
turtle.done()
print("complete!")