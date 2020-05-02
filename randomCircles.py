import turtle
import random

window = turtle.Screen()
window.title("Tim the turtle making circles!")

# Creating our turtle Tim!
tim = turtle.Turtle()

# Setting the shape of tim
tim.shape('turtle')

# Set pen width
tim.width(5)

# To be used for our random circle generator
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black', 'pink', 'cyan', 'magenta', 'grey']

# Setting x to 1 for infinite loop
x = 1

# Creating different color circles with different widths randomly in the plane
while x == 1:
    randColor = random.randrange(0, len(colors))
    tim.color(colors[randColor])
    rand1 = random.randrange(-600, 600)
    rand2 = random.randrange(-600, 600)
    tim.penup()
    tim.setpos((rand1, rand2))
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0, 80))
    tim.end_fill()

# Prevents the window from closing
turtle.done()