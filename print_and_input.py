"""
    TA office hours are in ITE 201E
    My office is ITE 211 MW 2:30 - 4:00
    
    For file transfer:

    https://www.bitvise.com/
    https://cyberduck.io/
    
        download ssh client not server
"""

"""
    What is python?
    
        Programming language - a set of instructions that get translated
            into machine code 'at some point'
        Interpreted Language - Python, Ruby, Java, Javascript
            there is an interpreter that reads our code called python.exe
            or python
        Compiled Language - assembly language, C/C++, Rust, etc
            get translated directly into machine code
"""

print("this is an argument")
print(5)
print(3.14159265358979)  # computer secretly stores this in scientific notation
print(True, False)
# not going to be tested, but you should know that True = 1, False = 0
print(True * True, False * False, True + False, True + 6)
"""
    Basic / Primitive Data Types:
        String (str) - sequence of characters
        Integers (int) - are positive negative or zero but whole
        Floating points (float) "has a decimal point"
        Booleans (bool) - True or False
"""
print(True, "happy", 2.718, 'also this', 4, 5, 6)

"""
    With input, you can get text from a user.
        input function ONLY returns strings
"""

tv_show = input('Give me a TV show: ')
# assignments go this way <---
# this is wrong: input() = random_nonsense
print('The tv show you gave is', tv_show)

radius = 4.2
is_happy = False
friends = -7
"""
    Variables can be used in algebraic expressions
        order of operations is "standard"
        PE[DM][SA] or BODMAS
"""

new_friends = 5 * (friends + 18)

meme = 6 / 2 * (2 + 1)
anti_meme = 6 / (2 * (2 + 1))
print(meme)

x = 5 ** 2  # double ** is exponent
y = 5 ** (1 / 2)
z = 5 ^ 2  # do not use the bitwise exclusive or
print(x, y, z)
sqrt_5 = 5 ** 1 / 2
print(sqrt_5)

"""
    Variable - location in RAM (memory) where you can store data
        use variables to give these locations names so that we
        can access them
        
    Python-Legal Variable Names
        must start with letters or underscores, capital or lower case
            cannot start with a symbol or number
        the rest of the variable must be letters, numbers, underscores
            no symbols (!@#$%^&*()~`)
"""
THIS_IS_A_VARIABLE = 5
thisIsMyString = "my string"
_single_underscore = True
__double_underscore = False
___triple_underscore = "why"
print(0b1100011)

"""
    PEP8 programming standard
    
        variables should be snake-case
        they should be lowercase separated by underscores
        single letter variables like "x" or "y" should be avoided
            unless it's obvious what they mean
            add a comment describing them
"""
snake_case = 'Yes'
another_variable_is_here = 'very yes'
the_radius = 5
r = 17.2  # r represents the radius of the object

"""
    All input is taken as strings
"""

print(5 + int("7"))
seven = '7'
print(5 + int(seven))

hopefully_an_int = int(input('Tell me an integer: '))
print('You entered:', hopefully_an_int)

"""
We will enter a lot of data into your inputs
    We will always enter the correct data TYPE into the input
"""

my_float = float(input('Enter a float: '))

