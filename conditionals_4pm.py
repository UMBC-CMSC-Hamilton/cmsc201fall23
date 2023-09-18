if False:
    """
        Printing in Python
    """
    
    my_number = 128
    my_string = 'cheddar cheese'
    
    print('I like', my_string, 'and the number is', my_number)
    
    # using string concatenation putting plus between two strings
    like_string = "I like"
    print(like_string + " " + my_string)
    # cast from int to string
    print("My favorite number is " + str(my_number))
    
    # python knows that f"" f'' is a format string
    print(f"I like {my_string} and the number is {my_number}")
    
    # C style
    print("I like %s and the number is %d" % (my_string, my_number))
    
    """
        Escape Sequences
        
        \n = newline
        \t = tab character
        \r = carriage return [I love this but I don't test it]
        \\ = a single backslash
        
        don't have to know this, but interesting:
        \r\n- windows
        \n - mac linux
    """
    
    print('a\nb')
    
    print('a\tb\tc\td')
    
    print('hello', end='')
    print('\rgoodbye')
    
    # 3 backslashes
    print('\\\\\\')
    
    print('\\the word')
    
    """
        if statement - conditional
        
    Syntax:
    
    if condition:
        everything inside of the if statement must be tabbed
        this line too
        and also this line all inside of the if statement
    
    once if statement is finished it will execute this line next
    
    In python there are two different equal signs
    
        =   assignment operator -> LHS = RHS
            LHS = variable that is going to accept the value
            RHS = expression that can be evaluated
        ==  equivalence operator (comparison)
            are the two things the same or different?
    """
    
    x = int(input('Tell me an integer: '))
    
    if x == 5:
        print('x is five')
    
    print('x is', x)
    
    food = input('Tell me something to eat: ')
    if food.lower() == 'sandwich'.lower():
        print('Good choice')
        
    movie = input('Tell me a movie to watch: ')
    if movie.upper() == 'Barbie'.upper():
        print('Good choice')
    
    
    print(movie.upper(), movie.lower())
    
    """
        Comparison operators
        
        == < > <= >= !=
    """
    x = 0
    y = 0
    while x != -1:
        x = int(input('Tell me int: '))
        y = int(input('Tell me int: '))
        
        if x < y:
            print(f'{x} is less than {y}')
            if 2 * x < y:
                print('x is way less than y')
        
        if x == y:
            print(f'{x} is equal to {y}')
    
        if x != y:
            print(f'{x} is not equal to {y}')
    

"""
    Logical Operators
    
and, or, not

X and Y = true if both X and Y are true
    Y   True    False
X
True    True    False
False   False   False

X or Y = true if either X or Y are true
    Y   True    False
X
True    True    True
False   True   False

not X -> unary operator eats a single thing, spits out T/F

X       not X
True    False
False   True

Law of the Excluded Middle

"""

age = int(input('Tell me age: '))
name = input('Tell me your name: ')

if name.lower() == 'eric' and age >= 18:
    print('You may pass')
else:
    print('You shall not pass')


if name.lower() == 'eric' or age > 30:
    print('You are either Eric or old')
