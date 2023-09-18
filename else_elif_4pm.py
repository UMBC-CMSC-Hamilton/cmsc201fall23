if False:
    a = True
    b = False
    c = True
    
    if (a or b) and not c:
        print('this works')
    else:
        print('nope')
    
    
    a = False
    b = False
    c = True
    
    if not(a and b) and c:
        print('yes')
        
    a = False
    b = True
    if not a or b:
        print('word')
        
    """
        Logical operators have a precedence:
            not <- highest precedence / happens first
            and <- next precedence /happens next
            or <- last precedence / happens last
        important thing to know is that not happens first and then (and and or)
    """
    a = False
    b = True
    if not (a or b):
        print('word2')  # doesn't print
        
    
    a = True
    b = False
    c = False
    if (a or c) and (not b or c):
        print('lucky')
    
    """
    
    """
    a = True
    b = True
    if not a or not b:
        print('not a or not b')
    
    if not (a and b):
        print('not (a and b)')
    """
    x(y + z) = xy + xz
    
    DeMorgan's Law:
        not (a and b) == not a or not b
        not (a or b) == not a and not b
    
    Sometimes you can simplify your code a bit if you're able to use this.
    
        Prove it using Venn Diagrams
    """
    
    """
    Operator Precedence:
    
        Algebra **, *, /, //, %, +, -
        Comparison Operators
            ==, <, >, !=, <=, >=, in
        Logical Operators
            not
            and
            or
    """
    """
        if you have an integer or a float:
            28 is "true" 0 - false or 0.0 is false but anything else is true
    """
    x = int(input('x: '))
    if x == 17 or x == 28:
        print('You have chosen wisely')
    else:
        print('You have chosen poorly')
    
    """
    elif and else
    
    what if you have an if statement that fails?
    that's completely ok, but what if you have other options?
    
    el[se ]if -> elif
    
    if [some condition]:
        do something in here
    elif [some other condition]:
        other code here
    elif [some even different condition]:
        different code
    elif [another thing]:
        more code
        
    Rules:
        1) You can have as many elif statements attached to an if statement as you want
        2) Only one will ever execute [potentially zero]
    
    else is always used at the end of a block of if-elif's
    if all of the conditions were false, then it executes the else
        catchall, it will catch you if nothing else happens
    """
    
    menu = int(input('What would you like? Pick 1-5: '))
    if menu == 1:
        print('You get sushi tonight')
    elif menu == 2:
        print('You get pizza!')
    elif menu == 3:
        print('Dumplings')
    elif menu == 4:
        print('Cookies and Cream')
    elif menu == 5:
        print('Lamb Vindaloo')
    else:
        print('You have selected porridge')
    
    
    if menu == 1:
        print('something')
    elif menu == 2:
        print('something else')
    else:
        pass
    
    print('hi we survived')
    """
    You want to chain from the most specific to the most general when the conditions
        overlap
    """
    the_int = int(input('Tell me your favorite integer: '))
    if the_int == 2001:
        print('The space odyssey')
    elif the_int > 5000:
        print('That is a mega big int')
    elif the_int > 100:
        print('That is a pretty big int')
    elif the_int > 0:
        print('Your int was positive, that\'s cool')
    
    the_int = int(input('Tell me your favorite integer: '))
    if the_int == 2001:
        print('The space odyssey')
    if the_int > 5000:
        print('That is a mega big int')
    if the_int > 100:
        print('That is a pretty big int')
    if the_int > 0:
        print('Your int was positive, that\'s cool')
    
    SECRET_PASSWORD = 'password123'
    password = input('Enter your password: ')
    if password == SECRET_PASSWORD:
        print('Access Granted, You may now crash the server')
    else:
        print('Access Denied Try again:')
        password = input('Enter your password: ')
        if password == SECRET_PASSWORD:
            print('Access Granted, You may now crash the server')
        else:
            print('Access Denied Try again, one more attempt:')
            password = input('Enter your password: ')
            if password == SECRET_PASSWORD:
                print('Access Granted, You may now crash the server')
            else:
                print('Access Denied, you may not crash this server, sorry')
    
"""
    20 questions with Harry Potter
    Hermione Granger
    Harry Potter
    Dobby
    Fluffy
    Dolores Umbridge
    Ron Weasley
    Voldemort
    Draco Malfoy
"""

human = input('Are you human? ')
if human.lower() == 'yes':
    ginger = input('Are you a ginger? ')
    if ginger.lower() == 'yes':
        print('You are Ron, don\'t mess with the ice cream truck dude')
    else:
        kill_potter = input('Have you tried to kill Potter? ')
        if kill_potter.lower() == 'yes':
            print('Naughty human')
            good_bad = input('How do you feel about centaurs? (good/bad)')
            if good_bad.lower() == 'good':
                print('You are Draco')
            else:
                print('You are Dolores')
        else:
            glasses = input('Do you wear glasses? ')
            if glasses.lower() == 'yes':
                print('You are Harry Potter')
            else:
                print('You are Hermione Granger')
else:
    elf = input('Are you an elf? ')
    if elf.lower() == 'yes':
        print('You are Dobby')
    else:
        nose = input('Do you have a nose? ')
        if nose.lower() == 'yes':
            print('You are Fluffy')
        else:
            print('You are Voldemort')

