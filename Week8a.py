# file1 = open('file1.txt')
# read = file1.read(8) # Look this up
# readline1 = file1.readline()
# readline2 = file1.readline()
# readlines = file1.readlines()

# for line in file1.readlines():
#     print(line.upper())

# file2 = open('file2.csv', 'w')
# file2.write('Name,Grade\n')
# file2.writelines(['Mac,D\n', 'Ben,C\n', 'Alex,C\n'])

# file2.close()

# file3 = open('file2.csv', 'a')
# file3.write('Brodie,F\n')

# grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
# students = ['Mac', 'Ben', 'Alex', 'Farhad', 'Sebastian', 'Kaylee', 'Josh', 'Sam', 'Brodie', 'Skyler', 'Kate']

# import random
# with open('Grades.csv', 'w') as f:
#     f.write('Name,Grade\n')
#     for student in students:
#         rand = random.randint(0, len(grades)-1)
#         print(student, grades[rand])
#         f.writelines(f'{student},{grades[rand]}\n')

# dummy_variable = 0







def get_number():
    try:
        number = int(input('Enter a number: '))
        print(number)
    except ValueError as ex:
        print(ex)
        get_number()
    except:
        print("Invalid number")
        get_number()

get_number()