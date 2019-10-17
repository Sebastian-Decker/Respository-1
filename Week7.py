def print_something(something):
    print(f"This is something: {something}")

def print_something_else(soemthing_else):
    print(f"This is something else: {soemthing_else}")\

def getNumber():
    import random
    return random.randint(1, 1000)

def findMax(num_1, num_2):
    if num_1 > num_2:
        print(f'Value 1: {num_1} is greater than Value 2')
    elif num_1 == num_2:
        print("Error, both are equal")
    else:
        print(f'Value 2: {num_2} is greater than Value 1')

def draw_triangle():
    draw_side(200, 120)
    draw_side(200, 120)
    draw_side(200, 120)

def draw_square():
    draw_side(100, 90)
    draw_side(100, 90)
    draw_side(100, 90)
    draw_side(100, 90)
    
def draw_pentagon():
    draw_side(50, 72)
    draw_side(50, 72)
    draw_side(50, 72)
    draw_side(50, 72)
    draw_side(50, 72)

def draw_side(darwing_turtle, pixels, degrees):
    drawing_turtle.forward(pixels)
    drawing_turtle.left(degrees)

print_something("Hello World.")
print_something_else("Hello Underworld.")
print_something("Hello World.")
print_something_else("Hello Underworld.")
print_something("Hello World.")
print_something_else("Hello Underworld.")
print_something("Hello World.")
print_something_else("Hello Underworld.")
print_something("Hello World.")
print_something_else("Hello Underworld.")

num_1 = getNumber()
num_2 = getNumber()
findMax(num_1, num_2)
if __name__ == "__main__":
    import turtle

# shape = int(input("Enter a number between 1 and 3 to draw: "))
# window = turtle.Screen()

# drawing_turtle = turtle.Turtle()

# if shape == 1:
#     draw_triangle()
# elif shape == 2:
#     draw_square()
# elif shape == 3:
#     draw_pentagon()
# else:
#     print("Invalid number try again.")\

# turtle.done()
