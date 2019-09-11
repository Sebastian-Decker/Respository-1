def print_name(full_name):
    print(f'Hello, {full_name}')

#name = input('Enter your name: ')

#print_name(name)

def print_names(name1, name2):
    print(f'Hello, {name1} and {name2}')

#print_names("Sebastian", "Tina")

#def abc(*args):
 #   print('hello')
  #  print(args[0])
#    for name in args:
#        print(name)

#abc()
#abc('a')
#abc('a','b','c','d','e')

#def addition(*args):
#   print(sum(args))

#addition(1,2,3,4,5,6)

my_list = [1, 2, 3, 4, 'a', 'b', 'c']


def addition(n1, n2):
    print(n1)
    print(n2)
    print(n1+n2)

"""
don't do this
    def subtraction(3, 2):
        ...

        def divide(n1, n2):
            ...and

    """

#a^2 + b^2 = c^2

def pythagorean_theorem(a, b):
    c = (a**2 + b**2)**(1/2)
    return c

    

pythagorean_theorem(2,2)
result = pythagorean_theorem(2,2)

print(pythagorean_theorem(2,2))
print(result)