"""
#favorite_number = input("what is your favorite number? ")
#if favorite_number.isdiget:
#    favorite_number = int(favorite_number)

#print(type(favorite_number))

num_1 = int(input("Input number 1: "))
num_2 = int(input("Input number 2: "))

"1 + 1 = 2"

print(str(num_1) + "+" + str(num_2) + "=" + str(num_1 + num_2))
print("%d + %d = %d" %(num_1, num_2, num_1=num_2))
print(f"{num_1} + {num_2} = {num_1+num_2}")
"""

"""
import turtle # Need to import the module turtle

screen = turtle.Screen() # Need to create a new screen/drawing board
screen.bgcolor("pink") # Sets the background color
screen.title("CIS-121") # Sets the title

drawing_turtle = turtle.Turtle() # Creates a turtle to draw with

drawing_turtle.forward(100)
drawing_turtle.left(90)

drawing_turtle.forward(100)
drawing_turtle.left(90)

drawing_turtle.forward(100)
drawing_turtle.left(90)

drawing_turtle.forward(100)

turtle.done() # This keeps the screen/canvas open until you close it
"""

"""
import turtle

window = turtle.Screen()
window.title("hexagon")
window.bgcolor("orange")
drawing_turtle = turtle.Turtle()

drawing_turtle.forward(100)
drawing_turtle.left(60)

drawing_turtle.forward(100)
drawing_turtle.left(60)

drawing_turtle.forward(100)
drawing_turtle.left(60)

drawing_turtle.forward(100)
drawing_turtle.left(60)

drawing_turtle.forward(100)
drawing_turtle.left(60)

drawing_turtle.forward(100)

turtle.done()
"""


import turtle
import time
import random

window = turtle.Screen()
drawing_turtle = turtle.Turtle()

num_sides = input("Enter the number of sides of the shape you want. ")

if num_sides.isdigit():
    num_sides = int(num_sides)

angle = 180 - 180*(num_sides-2)/num_sides

drawing_turtle.up

x = 0
y = 0
drawing_turtle.setpos(x, y)

num_shapes = 24

for _ in range(num_shapes):
    drawing_turtle.color(random.random(), random.random(), random.random())
    x += 5 # x = x + 5
    y += 5
    drawing_turtle.forward(x)
    drawing_turtle.left(y)
    for _ in range(num_sides):
        drawing_turtle.begin_fill()
        drawing_turtle.down()
        drawing_turtle.forward(40)
        drawing_turtle.left(angle)
        drawing_turtle.forward(40)
        print(drawing_turtle.pos())
        drawing_turtle.up()
        drawing_turtle.end_fill()

turtle.done()




















