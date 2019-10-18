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