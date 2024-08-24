"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle    
import random                       # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast. 


forwards = [ 53, 44, 167, 56, 6, 3, 4, 5]
lefts = [ 9, 4, 7, 4, 7, 3, 6, 9]
colors = [ 'red', 'green', 'blue']

for  i in range(8):

    forward = forwards[random.randint(0, 8)]
    left = lefts[random.randint(0, 8)]
    color = colors[random.randint(0, 8)]


    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  

