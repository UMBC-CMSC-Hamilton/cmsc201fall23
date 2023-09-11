"""
    What is python?
        python is an interpreted programming language
        
        compiled language
            assembly, C/C++, Rust
        interpreted language
            javascript, python, ruby, java
            scripting language
            more layers between us and the hardware
"""

"""
    print, input are two built in functions in python
"""

print("Here is a string to be printed")
print(5, 17, 22, type(17))
print(3.1415926535897932)  # this is a float
print(5.0, type(5.0))
print(True, False)  # booleans after George Boole
print(True * True, False * False, True + False)

"""
primitive data types:
    strings - text, characters
        no such thing as individual characters, only strings
            of length 1
    floats - things with decimal points
    integers - integers
    booleans - encoding True and False
"""
print(len("robot"))
print('robot', "chicken", "this is allowed")
# " this is not allowed' you can't mix the symbols.

"""
What is a variable?
    Location in RAM where you can store values
    and it's also a name that points to that location
"""
my_variable = 5
print(my_variable)
my_variable = 'sandwich'
print(my_variable)

"""
a variable assignment is its declaration in python

new_var_name = 17
        <------------
17 = new_var_name not allowed

LHS = RHS
LHS = variable name
RHS = expression which evaluates to a value and is put into the variable
"""
random_calc = 2 * (5 - 8) / 3
print(random_calc)

"""
Python obeys the regular order of operations
    PE[MD][AS] or BODMAS
    we say that multiplication and division are "equal precedence"
    neither of them will take priority over the other
"""
meme = (6 / 2) * (2 + 1)
print(meme)

"""
exponentiation in python we use **
"""

print(5 ** 2, 7 ** 3, 3 ** (1 / 2))
print(5 ^ 2)  # bitwise xor [not needed in 201]
"""
two divisions in python

floating point division -> / output a float
integer division -> // outputs an integer
"""
print(5 / 2, 5 // 2)
print(6 / 3, 6 // 3)
print(-7//3)

"""
    input = it takes a prompt (a string) displays that to the user
        gets a string from user and puts it in whatever variable
        that we assign
"""

# the_movie = input('tell me a movie: ')
# print('The movie you selected is', the_movie)
# fav_class = input('Tell me your favorite class: ')

number_one = int(input('Tell me a integer: '))
number_two = int(input('Tell me another integer: '))
print(number_one + number_two)

float_one = float(input('Tell me your favorite floating point number: '))
float_two = float(input('Tell me your second favorite floating point number: '))

result = float_one * float_two

print(str(result))  # never trust a float

if result - 2.56 < 0.0000001:
    print('life is good')
    
"""
    legal variable names vs python coding standards (PEP8)
    
    starts with any letter (upper or lower case) or an underscore
    rest of the characters are letters, numbers, and underscores
    no special characters !@#$%^&*() <>?~
    
"""
ROBOTS_ARE_FUN = 5
camelCaseIsForJava = 'javascript time'
______tons_of_underscores = 3
_____tons_of_underscores = 4

"""
PEP8 standard written by Guido van Rossum
    snake case
"""
this_is_a_good_variable = 5
_underscores = 'underscores'
this_variable12 = 12
print(0b111)
