my_counter = 31
my_name = 'Eric'

# use commas to separate different elements that you print
print('My name is', my_name)
print('The counter is currently', my_counter)

# use string concatenation
print('My name is ' + my_name)
# remember that you may have to cast whatever you are concatenating
# into a string
print("The counter is currently " + str(my_counter) + " " + str(42))

# f-strings (format-strings)
print(f'My name is {my_name}')
# print(f'My name is {robots}')
print(f'The counter is currently {my_counter}')

# C-style printing [allowed, but why?]
print("My name is %s" % my_name)

"""
    Conditionals:
    
        Conditionals take an expression, determine if that expression
        is True or False, if it's true it executes.
        
        If false [at least for an if statement] it does nothing.
        
    Syntax:
        structure of language.
        
if [condition]:
    # must put a tab,
    # all of the code that is in the if statement is tabbed
# code not tabbed follows the if statement

if the condition is true, it executes the tabbed code
if the condition is false, it skips the tabbed code

Tabs vs spaces in python
    python replaces a tab with 4 spaces
    
what is = ?
    Always an assignment operator
    LHS = RHS evaluates the RHS and sticks the value into the variable
    which is the LHS
    x = 3
    whatever = True
    x = (3 + 9) ** (1/2)
what is == ?
    if you need to test whether two "expressions" are the equal
       then you use the comparison operator ==
"""
the_int = int(input('Tell me an integer: '))

if the_int == 42:
    print('Blah blah meaning of life')
    
robot_1 = 'RoBoT'
robot_2 = 'robot'
# what we mean by case sensitive is that an upper case letter
# and a lower case letter are not the same, different ascii values

if robot_1 == robot_2:
    print('Yes it is, turns out')
    
canoe = 'Canoe'
canoe_2 = 'canoe'

if canoe == canoe_2:
    print('canoes!')

if canoe.lower() == canoe_2.lower():
    print('yes they are, canoes')
    
if canoe.upper() == canoe_2.upper():
    print('yes they are, canoes')


another = 'rocks'
another_rocks = 'rocks '
if another == 'rocks '.strip():
    print('rocky')

a_story = 'once upon a time'.strip()
print(a_story)

space_string = '       '.strip()
print(space_string, end="::\n")
"""
    Escape sequences:
        anything that starts with a \
    What is whitespace?
    [space]
    \n = newline
    \t = tab
    \r = carriage return
    
    in linux/macOS a newline is just \n
    in windows, a newline is actually \r\n
    
    A single backslash = \\
    
    If you have a unicode sequence
"""

print('\na\tb\tc\nd')
print('\\\\\\')
# right arrow unicode example
print("\u2192")

a = int(input('Tell me an int: '))
b = int(input('Tell me an int: '))

"""
    here are the comparison operators:
        == < > <= >= !=
        equals, less, greater, less than or equal to,
        greater than or equal to, not equal
    
"""

if a < b:
    print(f'{a} is less than {b}')
    print(a, 'is less than', b)

if a != b:
    print(f'{a} is not equal to {b}')

string_1 = input('Tell me string: ')
string_2 = input('tell me other string: ')
if string_1 < string_2:
    print('yes')
    
if 'aabc' < 'aade':
    print('weird but yes')

"""
Logical Operators:

    and, or, not
    
    X and Y: (are true)
    X   True    False
Y
True    True    False
False   False   False

    X or Y: (are true)
    X   True    False
Y
True    True    True
False   True   False


Unary Operator = 1-ary eats a single thing
not X
X       not X
True    False
False   True

"""