# Polygon, Pinwheel, and Asterisk
import turtle

def draw_polygon(some_turtle, sides, size):
    #Draws a polygon with the given number of sides and size
    for i in range(sides):
        some_turtle.forward(size)
        some_turtle.right(360/sides)


def draw_pinwheel(some_turtle, sides, size):
    """Draws a pinwheel with the given number of sides and size"""
    for i in range(sides):
        draw_polygon(some_turtle, 3, size)
        some_turtle.right(360/sides)

def draw_asterisk(some_turtle, size):
    """Draws an asterisk with the given size"""
    for i in range(5):
        some_turtle.forward(size)
        some_turtle.right(144)

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
    size = int(input("Enter the size of each side: "))
    draw_pinwheel(turtle, sides, size)
    turtle.done()
elif mode_selector == "3":
    size = int(input("Enter the size of each side: "))
    draw_asterisk(turtle, size)
    turtle.done()
else:
    print("Invalid input")

    


