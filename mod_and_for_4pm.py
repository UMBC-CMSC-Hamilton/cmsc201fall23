"""
    Modulus Division
    
        6/5 = 1 R 1
            6 = 5(1) + 1
        19/4 = 4 R 3
            19 = 4 * 4 + 3
        23 / 9 = 2 R 5
            23 = 2(9) + 5
            
        23 = 3(9) - 4 = 4(9) - 13 = 1(9) + 14
        0 <= r < d
        n / d
        
        Integer division and modulus division:
        
            integer division gives us the quotient 23 // 9 (two division bars)
            Modulus division gives us the remainder 23 % 9
                Symbol is percent but it doesnt really have anything to do
                    with percent.
            
"""
if False:
    print(5 % 3, 23 % 9, 281 % 37)
    print(5 // 3, 7 // 2, 7 % 2)
    
    # if you mod by two you are checking "parity" = evenness or oddness
    print(9 % 2, 4 % 2, 1 % 2, 18 % 2)
    print(-3 % 5, -3 // 5, -13 // 3)
    # -3 = (-1) * 5 + 2
    # -13 = (-5) * 3  + 2
    
    """
        Like hw but not:
        
            Months of the year
            What month will it be n months from now?
            0 = September
            1 = October
            2 = November
            3 = December
            4 = January...
            12 = September
            18 = March
    """
    
    num_months = int(input('How many months from now do we want to go? '))
    num_months = num_months % 12
    
    # not 12 but 0 because 24 % 12, 36 % 12, 72 % 12 are all zero
    if num_months == 0:
        print('September')
    elif num_months == 1:
        print('October')
    elif num_months == 2:
        print('November')
    elif num_months == 3:
        print('December')
    elif num_months == 4:
        print('January')
    elif num_months == 5:
        print('February')
    elif num_months == 6:
        print('March')
    elif num_months == 7:
        print('April')
    elif num_months == 8:
        print('May')
    elif num_months == 9:
        print('June')
    elif num_months == 10:
        print('July')
    elif num_months == 11:
        print('August')
    
    # use mod for games.
    turn_count = 1  # player_1
    # game happens here
    turn_count = turn_count + 1  # 2 player_2
    # and here
    turn_count = turn_count + 1  # 3 player_1
    # also here
    turn_count = turn_count + 1  # 4 player_2
    
    """
    Let's talk about for loops.
    
        Sometimes we want to repeat a bit of code
        
    Syntax:
    for [index variable] in range(10): <-- need a colon
        next line get tabbed
    """
    for i in range(10):
        print(10 - i)
    
    # range(number) gives you 0, 1, 2, 3, .... number - 1
    # try to add all the numbers between 1 and 10
    
    max_num = int(input('How much do you want to add? '))
    total = 0
    for i in range(max_num):
        total += i + 1
        print(i + 1, total)
        # total = total + i + 1 same functionality as above
    
    print(total)
    
    """
        Factorial because I like it.
        
        n! = n (n - 1) (n - 2) (n - 3) ... 3 * 2 * 1
           = 1 * 2 * 3 * 4 * ... * n
    """
    
    n = int(input('What factorial do you want to compute? '))
    factorial = 1
    
    for i in range(n):
        factorial *= i + 1
        # factorial = factorial * (i + 1)
        print(i + 1, factorial)
        # total = total + i + 1 same functionality as above
    
    print(factorial)
    
    
    for j in range(100):
        factorial = 1
        for i in range(j):
            factorial *= i + 1
        print(j, factorial)
        

"""
    fibonacci numbers
    Rule: add the previous two numbers
    0th 1st
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and more!
"""

previous_num = 1
prev_prev_num = 0

k = int(input('What fibonacci do you want to calculate? '))
for i in range(k - 1):
    current = previous_num + prev_prev_num
    # now we're going to set up for the next loop
    prev_prev_num = previous_num
    previous_num = current
    
    print(current)
    
print(f'The {k}th Fibonacci is', current)


"""
Lists:
    A list is a collection of various data (variables)
        the list itself is a variable
    Syntax for a list:
        [1, 2, 3, 4, 5]
"""
my_words = ['cat', 'dog', 'chicken', 'failure', 'bank', 'phone']
print(my_words)

random_list = [3.14, 'dog', 'pupper', 17, True, False]
print(random_list)

for x in random_list:
    print(x + 2)
