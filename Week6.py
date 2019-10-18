# Iterative Statement

# Review

"""
if expression: Expression must evaluate to a True value
    statement

if the first doesn't work, try the next 
elif (else if) expression:
    statement

if all else fails, run this guy
else:
    statement
"""

# While loop

"""
While expression: Expression must evaluate to a True value
    statement
"""


"""
This runs forever, use CTRL + C to break out of it
while True:
    print("Hello")
"""

a = 0

while a != 10:
    print(a)
    a += 1 # Same thing as a = a + 1

user_input = None
while True:
    user_input = int(input("Enter the number 10 "))
    if user_input == 10:
        break

print("thank you for inputting the number 10.")

speed_limit = int(input("Enter the speed limit"))

demerit_points = 0

while True:
    speed_of_car = int(input("What is the speed of the car"))


    if speed_of_car <= speed_limit:
        print("Ok")
        continue

    demerit_points += (speed_of_car - speed_limit) // 5
    print(demerit_points)

if demerit_points >= 12:
    print("License Suspended")
    break

