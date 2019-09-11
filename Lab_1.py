#part 1
print("Sebastian Decker")

#part 2
print("put the degrees in celsius you would like to convert")
C = int(input())

F = C * 1.8 + 32

#print(F)
print(f'{C} * 1.8 + 32 = {F}')

"""#part 3
import turtle
window = turtle.Screen()
window.title("pentagon")
drawing_turtle = turtle.Turtle()
window.bgcolor("blue")
drawing_turtle.color("orange")

drawing_turtle.forward(100)
drawing_turtle.left(72)

drawing_turtle.forward(100)
drawing_turtle.left(72)

drawing_turtle.forward(100)
drawing_turtle.left(72)

drawing_turtle.forward(100)
drawing_turtle.left(72)

drawing_turtle.forward(100)
drawing_turtle.left(72)

turtle.done()
"""
#part 4
import turtle

myPen = turtle.Turtle()
myPen.ht()
myPen.speed(5)
myPen.pencolor('orange')

"""
Ask for 3 starting points of the triangle, named point_1, point_2, point_3
"""
def get_xy_corordinate():
     x, y = input('Enter the x and the y coordinates').split(',')
     return int(x), int(y)

point_1 = get_xy_corordinate
point_2 = get_xy_corordinate
point_3 = get_xy_corordinate

points = [point_1, point_2, point_3] #size of triangle

def getMid(p1,p2):
    midpoint = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
    #midpoint = tuple(map(lambda x, y: (x + y) /2, p1, p2))
    return midpoint

def triangle(points,depth):

    myPen.up()
    myPen.goto(points[0][0],points[0][1])
    myPen.down()
    myPen.goto(points[1][0],points[1][1])
    myPen.goto(points[2][0],points[2][1])
    myPen.goto(points[0][0],points[0][1])

    if depth>0:
        triangle([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   depth-1)
        triangle([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   depth-1)
        triangle([points[2],
                         getMid(points[2], points[1]),
                         getMid(points[0], points[2])],
                   depth-1)


# ASK FOR THE DEPTH OF TRIANGLE
depth = int(input('Enter the num of interactions'))
triangle(points, depth)

turtle.done()
