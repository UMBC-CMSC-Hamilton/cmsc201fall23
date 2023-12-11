"""
    Dec 15th 6-8 pm in ITE 104
    
    Future Python
        What didn't we learn this semester?
            
             - list comprehensions (play around with them)
                - dictionary comprehensions, also good
             - exception handling
             - classes
             - variable numbers of arguments
             - keyword arguments

    What is a list comprehension?
        gives us the opportunity to create a list using a formula
            all in one expression
"""

one_hundred_zeros = []
for _ in range(100):
    one_hundred_zeros.append(0)

print(one_hundred_zeros)

list_comp_100_0s = [0 for _ in range(100)]
if list_comp_100_0s == one_hundred_zeros:
    print('yes it is')

integer_list = [i + 1 for i in range(20)]
print(integer_list)

height = 20
width = 10
checkerboard = [['x' if (i + j) % 2 else 'o' for j in range(width)] for i in range(height)]
for row in checkerboard:
    print(''.join(row))

my_dictionary = {x: x ** 2 for x in range(17)}
print(my_dictionary)

z = 4
my_var = 3 if z == 4 else 7
# x ? y : z "the ternary operator"
# if x condition is true then do y else do z

the_list = []
# a if x else b is a ternary if operator
my_var = max(the_list) if the_list else -1
print(my_var)

x = 20
y = 0
quotient = x / y if y != 0 else 0
print(quotient)

entered_properly = False

while not entered_properly:
    try:
        x = int(input('Tell me an integer'))
        y = int(input('Tell me an integer'))
        print(x / y)
        entered_properly = True
    except ValueError:
        print("one of the variables wasn't an integer")
    except ZeroDivisionError:
        print('You attempted to divide by zero')
    finally:
        # finally exists if you need to clean something up
        print('we tried')

try:
    my_file = open('random_that_doesnt_exist.txt')
except Exception:
    # if you don't know what kind of bad thing might happen
    # but... you definitely dont' want the program to crash
    # this is what to do
    print('something bad happened')

try:
    # other languages like C++ and Java use "throw" instead of raise
    raise KeyError("I raised this error to tell you something important")
except KeyError as key_error:
    print(key_error)

try:
    my_file = open('whatevertheusersays.txt', 'r')
except FileNotFoundError:
    print('That file didn\'t exist')

"""
    What is a class?
        int, bools, floats, string, lists, and dictionaries
        
        What if you want to define your own data type? use a class
"""


class Car:
    """
       there is private stuff in python now
       __makes things private, cool
    """
    
    # constructor, it runs when the class is created
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.miles = 0
        self.__my_private_int = 3
    
    # if it's a function inside of a class some people insist to call it
    #  a method
    def drive(self, miles=0):
        print(f'Your {self.make} {self.model} says Vroom!')
        self.miles += miles
    
    # overloaded operator
    def __repr__(self):
        return f'This car is a {self.make} {self.model} made in {self.year}'


x = Car("Nissan", "Maxima", 1995)
y = Car("Honda", 'Accord', 2020)

print(x.year, x.make, x.model)
x.drive()
y.drive()

print(x.miles)
x.drive(17)  # ==> converts it to drive(x, 17)
y.drive(200)  # ==> converts this to drive(y, 200)
print(x.miles, y.miles)
print(x)
print(y)
# print(y.__my_private_int)


"""
    var-args
"""


def get_average(*my_list):
    print(my_list)
    total = 0
    for x in my_list:
        total += x
    return total / len(my_list)


print(get_average(3, 5, 6, 9, 2, 1, 7))
print(get_average(3, 5, 6, 2, 2, 3))


def my_function(**keywords):
    print(keywords)


my_function(robot=7, typewriter="SelectricII", cls="almost over")

print('', end='hi')
