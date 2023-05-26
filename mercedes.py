import turtle

# Function to draw a circle with a given radius and color
def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw an arc with a given radius, angle, and color
def draw_arc(radius, angle, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius, angle)
    turtle.left(90)
    turtle.forward(radius * 2)
    turtle.left(90 + angle)
    turtle.forward(radius * 2)
    turtle.end_fill()

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('white')

# Create a turtle object
t = turtle.Turtle()
t.speed(2)
t.penup()

# Move to the starting position
t.goto(-70, -25)
t.pendown()

# Draw the Mercedes logo
draw_circle(50, 'black')
draw_circle(40, 'white')
draw_circle(30, 'black')
draw_circle(20, 'white')
draw_arc(70, 180, 'black')
draw_arc(70, 180, 'black')

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.done()
