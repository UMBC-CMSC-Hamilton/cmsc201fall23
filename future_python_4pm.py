"""
Dec 15th 6-8 pm for you in ITE 102 (here)

Future Python
    What didn't we learn this semester?
        List and Dictionary Comprehensions
        Exception Handling
        Classes
        Variable arguments and keyword arguments

    A list comprehension is a kind of short hand that you can use
        combines the creation of a list with a for loop
"""

new_list = ['x' for i in range(10)]
print(new_list)

list_of_numbers = [i + 1 for i in range(20)]
print(list_of_numbers)

five_by_five = [[i + j for j in range(5)] for i in range(5)]
print(five_by_five)

length = 5
width = 3
checkerboard = [['x' if (i + j) % 2 else 'o' for j in range(width)] for i in range(length)]

for row in checkerboard:
    print(''.join(row))

# a ? b : c; ternary operator if a then b else c
my_var = 100 if length > 10 else 5  # ternary operator
# b if a else c
print(my_var)

student = True
if student:
    fee = 10
else:
    fee = 12

fee = 10 if student else 12

import string
import random

my_letters = {x: ord(x) for x in string.ascii_letters}
print(my_letters)

random_numbers = {x: random.randint(0, 100) for x in range(25)}
print(random_numbers)

divided = False
while not divided:
    try:
        x = int(input('Tell me a number: '))
        y = int(input('Tell me a number: '))
        print(x / y)
        divided = True
    except ValueError as e:
        print(e)
        print('There was a problem')
    except ZeroDivisionError:
        print('You tried to divide by zero, naughty person. ')

#  in c++ and java try - catch
try:
    open('this file definitely doesnt exist.txt')
except FileNotFoundError:
    print('That wasnt a file but i am not going to crash')

try:
    # the program cannot crash, don't let it happen
    print(5 / 0)
except Exception as e:
    print('hi something went wrong')
    print(type(e))


def hide_the_error():
    raise KeyError("I am throwing you an error, please catch me.")


try:
    # other langauges = throw
    hide_the_error()
except KeyError as key_error:
    print("Yep that was a KeyError")
    print(key_error)

"""
    classes in python
        NoneType, int, bool, string, float, list, dict
        What if you want your own data type?
            data type to have it's own functions and internal variables
"""


class Starship:
    def __init__(self, name, length, speed):
        self.name = name
        self.length = length
        self.speed = speed
    
    def fire(self):
        print(f"{self.name} goes pew pew")


ship = Starship("Enterprise-D", 650, 'warp 9.7')
another_ship = Starship("Millennium Falcon", 20, "0.6 past c")

print(ship, another_ship)
print(ship.name, ship.speed)
print(another_ship.name, another_ship.speed)

ship.fire()  # ==> fire(ship)
another_ship.fire()  # ==> fire(another_ship)


class Student:
    # grades = [] shared variable, avoid it if you don't know what you're doing
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []
    
    def add_grade(self, new_grade):
        if new_grade >= 0:
            self.__grades.append(new_grade)
        else:
            print('Negative grades not allowed. ')
    
    def get_grades(self):
        return list(self.__grades)
    
    def __repr__(self):
        """
            must return a string which represents the class data
        """
        return f'Student: {self.name}\t ID: {self.student_id}'


s1 = Student('Eric', 12345)
s2 = Student('Brian', 632214)

s1.add_grade(97)
s2.add_grade(93)
s1.add_grade(56)
s2.add_grade(72)
print(s2.get_grades())

"""
    variable arguments
    you can have a function with a variable number of parameters
"""


# C++ might think pointer, but it's not really
# it's called the list-pack operator
def geometric_average(*numbers):
    print(numbers)
    total = 1
    for x in numbers:
        total *= x
    return total ** (1 / len(numbers))


print(geometric_average(2, 3, 4, 6, 7))
print(geometric_average(1, 1, 5, 4, 9, 2, 123781, 34, 23, 23, 2))

print('x')
print('x', 3)
print('a', '3', 'b')


def keywords(x, **kwargs):
    print(kwargs)


keywords(happy=7, robot=22, defcon=5, salamander=True, ship='Enterprise', x=2)


def get_nth_prime(n):
    prime_list = []
    while len(prime_list) < n:
        pass
    return prime_list[-1]


# [get_nth_prime(n) for n in range(100)]

the_list = [x for x in range(100) if all(x % i for i in range(2, x))]
print(the_list)
