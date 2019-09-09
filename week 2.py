#print("hello world")

#a = 3 ** 3
#print(a)

#print(2/1)
#print(2//1)

#print(5//2)
#print(5%2)

#print("what is you first name")
#first_name = input()
#last_name = input()

#print("Hello, " + first_name.upper())
#print(f"hello, {first_name} {last_name} !")

"""

-b +/- sqrt(b^2 - 4ac)
---------------------- 
         2a
"""

a = int(input())
b = int(input())
c = int(input())

result = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)

print(result)
