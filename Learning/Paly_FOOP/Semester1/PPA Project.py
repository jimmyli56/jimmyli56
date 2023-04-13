# Polygon, Pinwheel, and Asterisk
import turtle

def draw_polygon(some_turtle, sides, size):
    #Draws a polygon with the given number of sides and size
    for i in range(sides):
        some_turtle.forward(size)
        some_turtle.right(360/sides)


def draw_pinwheel(some_turtle, sides):
    """Draws a pinwheel with the given number of sides"""
    for i in range(sides):
        some_turtle.forward(100)
        some_turtle.backward(70)
        some_turtle.right(360/sides)

def draw_asterisk(some_turtle, sides):
    """Draws an asterisk with the given number of sides"""
    for i in range(sides):
        some_turtle.forward(100)
        some_turtle.backward(100)
        some_turtle.right(360/sides)

def main():
    """Main function"""
    # create a screen
    window = turtle.Screen()
    window.bgcolor("white")

    # create a turtle
    turtle = turtle.Turtle()
    turtle.shape("turtle")
    turtle.color("blue")
    turtle.speed(10)

mode_selector = input("Enter 1 for polygon, 2 for pinwheel, 3 for asterisk: ")
if mode_selector == "1":
    sides = int(input("Enter the number of sides: "))
    size = int(input("Enter the size of each side: "))
    draw_polygon(turtle, sides, size)
    turtle.done()
elif mode_selector == "2":
    sides = int(input("Enter the number of sides: "))
    draw_pinwheel(turtle, sides)
    turtle.done()
elif mode_selector == "3":
    sides = int(input("Enter the number of sides: "))
    draw_asterisk(turtle,sides)
    turtle.done()
else:
    print("Invalid input")

    


