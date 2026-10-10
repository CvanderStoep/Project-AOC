import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Coordinate System")
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
# t.shape("turtle")
t.color("blue")

# Move to different coordinates
# Move to (100, 100)
t.penup()
t.goto(150, 100)
t.pendown()
t.write("(150, 100)")

# Move to (-100, 100)
t.penup()
t.goto(-100, 100)
t.pendown()
t.write("(-100, 100)")

# Move to (-100, -100)
t.penup()
t.goto(-100, -100)
t.pendown()
t.write("(-100, -100)")

# Move to (100, -100)
t.penup()
t.goto(100, -100)
t.pendown()
t.write("(100, -100)")

# Return to origin
t.penup()
t.goto(0, 0)
t.pendown()
t.write("(0, 0)")

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
