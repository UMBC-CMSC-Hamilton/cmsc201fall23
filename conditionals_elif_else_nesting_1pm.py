"""

"""
import math

if False:
    number = float(input('Tell me an angle in degrees: '))
    # radians so if you don't convert your answers will be confusing
    math.sin(number * math.pi / 180)
    print(math.pi)
    
    """
        Back to if statements
    
            without conditionals we basically only have one direction
                that a program can flow, really we're not doing
                "computation"
    """
    
    x = 3
    my_string = 'Happy'
    
    if x == 3 and my_string.lower() == 'happy':
        print('Yes both are true')
    
    y = 7
    z = 4
    
    if y > 10 or z < 5:
        print('hello there')
    
    x = int(input('Enter int: '))
    y = int(input('Enter int: '))
    
    if not (x == 2 and y == 5):
        print('Hello!!!')
    
    """
    DeMorgan's Law
        Distributive property for not
        x(y + z) = xy + xz
        
        not(A and B) <=> not A or not B
        not(A or B)  <=> not A and not B
    """
    
    """
        Operator Precedence
        
        Algebra -> PEMDAS + L->R sinistrodextral
        Conditional operators
            == < > <= >= != in
        Logical Operators
            not - important to know that not happens first
            and
            or
    """
    
    a = False
    b = True
    
    if not a or b:
        print('donuts')
    
    a = True
    b = False
    c = True
    if (a or b) and not c:
        print('coffee coffee coffee')
    
    a = False
    b = True
    c = True
    if (a or b) and (a or c):
        print('winner winner chicken dinner')
    
    """
        what if you don't execute the if statement?
        
        if you use an else statement at the end of your if statment
        you will execute that code when all of the other statements
            if /elif are false
    """
    
    password = input('Tell me your password: ')
    
    if password == 'password1':
        print('You have accessed the server')
    else:
        print('Access denied.')
    
    """
        modulus division %
        a % b = "a mod b" is the remainder after you divide a // b
        
        You can use modulus to check if a number is even or odd
            that number % 2 == 0 then it's even
                            == 1 then it's odd
            (0 is even)
    """
    the_number = int(input('Tell me a number divisible by 7'))
    if the_number % 7 == 0:
        print(the_number, 'is divisible by 7')
    else:
        print(the_number, 'has a remainder', the_number % 7)
    
    """
        you can also chain if statements together using "elif"
        else if
    """
    
    the_animal = input('Tell me an animal: ')
    if the_animal == 'dog':
        print('Bark bark -> pet')
    elif the_animal == 'cat':
        print('meow? -> pet maybe if not evil')
    elif the_animal == 'lion':
        print('RUN! but maybe doesn\'t matter')
    elif the_animal == 'hamster':
        print('eat it, says one sorta messed up student')
    elif the_animal == 'snake':
        print('Give hamster')
    elif the_animal == 'human':
        print('The most dangerous game')
    else:
        print('Who knows are you sure it isnt a rock?')
    
    x = int(input('Tell me int immediately!! '))
    if x > 2000:
        print('x is very large')
    elif x > 10:
        print('x is bigger than 10')
    elif x > 0:
        print('x is positive')
    else:
        print('x is probably negative or zero right?')
    
    if x > 2000:
        print('x is very large')
    if x > 10:
        print('x is bigger than 10')
    if x > 0:
        print('x is positive')
    
    """
        Nesting is a feature of a programming language where you
            are able to put if statements 'inside' of other if statements
            
            Inner if statements only execute when the outer one does
    """
    
    my_movie = input('Tell me a movie: ')
    favorite_number = int(input('Tell me a number '))
    
    if my_movie.lower() == 'home alone' or my_movie.lower() == 'home alone 2':
        print('Home Alone was good, but there are some plot holes')
        if favorite_number > 100:
            print('That is a pretty big number')
        else:
            print('That is a reasonable number')
    else:
        print('That movie was awesome')
        if favorite_number == 28:
            print('That is perfect')
    
    """
        This will "run" but not like you think
        
        because 'home alone 2' is a non-empty string, therefore
        TRUE
        
        empty strings and zero are false
        0.0 float 0 int '' <- empty string are all false
        anything else is true
    """
    if my_movie == 'home alone' or 'home alone 2':
        print('Yes but what?')

"""
    Poor star wars fans :(
"""

jedi = input('Are you a jedi? ')
if jedi.lower() == 'yes':
    farm_boy = input('Are you a farm boy from a sand planet? ')
    if farm_boy.lower() == 'yes':
        print('You are Luke')
    else:
        green = input('Are you small and green and maybe about 1000 years old? ')
        if green.lower() == 'yes':
            print('You are yoda')
        else:
            print('You are Obi Wan')
else:
    sith = input('Are you a sith? ')
    if sith.lower() == 'yes':
        cyborg = input('Are you a cyborg? ')
        if cyborg.lower() == 'yes':
            print('You are Darth Vader')
        else:
            print('You are the Emperor')
    else:
        large_and_furry = input('Are you large and furry? ')
        if large_and_furry.lower() == 'yes':
            print('You are Chewbacca')
        else:
            droid = input('Are you the droids we\'re looking for? ')
            if droid.lower() == 'yes':
                color = input('What color are you? ')
                if color == 'gold':
                    print('You are C3P0')
                elif color == 'white' or color == 'blue':
                    print('You are R2D2')
                else:
                    print('You are a Gonk Droid')
