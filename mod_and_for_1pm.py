"""
    integer and modulus division
    
    How does division work?
    
        14/5 = 2.8 (correct if you're using / floating point division)
        
        Instead what if you said:
            2 with remainder of 4
            parity = even or oddness (0 is even)
        
        if you're going to divide n // d (double division is integer division)
        n = q * d + r
        
        14/5, n = 14, d = 5 n // d
        14 = -5 * 5 + 39

        14 = 2 * 5 + 4
            Rule: 0 <= r < d
            
            For positive numbers division basically rounds down.
        
        13 // 3
        
        Remainder determines the difference:
            If you want to get the remainder you use n % d
                "we say n mod d"
                "modulus division"
"""
if False:
    print(13 // 3, 8 // 2, 23 // 7, 21 // 7, 22 // 7)
    
    print(5 % 3, 23 % 6, 31 % 11, 4 % 2, 18 % 3, 25 % 5)
    # mod weirdness
    print(-2 % 5)
    # -2 = (-1) * 5 + 3
    # -2 = 0 * 5 - 2
    # in C++ it doesn't work like this, -2 % 5 = -2
    
    # how might we use mod?
    # let's say we want to find out what month it is after n months
    n = int(input('How many months in the future do you want to go? '))
    # it can be more than 12
    # Starting in september, +1 october +2 november, ...
    current_month = n % 12
    print(current_month)
    if current_month == 1:
        print('October')
    elif current_month == 2:
        print('November')
    elif current_month == 3:
        print('December')
    elif current_month == 4:
        print('January')
    elif current_month == 5:
        print('February')
    elif current_month == 6:
        print('March')
    elif current_month == 7:
        print('April')
    elif current_month == 8:
        print('May')
    elif current_month == 9:
        print('June')
    elif current_month == 10:
        print('July')
    elif current_month == 11:
        print('August')
    elif current_month == 0:
        print('September')
    
    
    """
        Completely different:
            For loops and lists
    
            If you need to repeat a piece of code, use a loop!
    """
    # i is the "index variable" - for loop creates it and changes it as you
    # progress.
    # in just another keyword
    # range(max) = 0, 1, 2, 3, 4, 5...., max - 1 [non-inclusive]
    # Syntactic - need a colon at the end of the for line
    #           tab in one more level
    
    for i in range(10):
        print(i)
    
    # let's say you want to add all the numbers between 1 and 10
    total = 0
    # because i don't want total to be reset every time we go through the loop
    for i in range(10):  # you could also do range(11) up to 10
        # total = total + i + 1
        total += i + 1
        print(i, total)
    
    print(f'The total is {total}')
    
    """
        What is a prime number?
            a number whose integer divisors are 1 and itself [only]
            Integer divisor is that it divides the number without remainder.
            except 1 which is not
            1 2 3 4 5
            0 1 2 1 0
    """
    
    n = int(input('What number do you want to check for primality: '))
    is_prime = True
    for i in range(n):
        if i == 0 or i == 1:
            pass # no-op, NOP/ no operation does nothing, except placeholder
        elif n % i == 0:
            is_prime = False
    
    if n == 1:
        is_prime = False
    
    if is_prime:
        print(n, 'is prime!!')
    else:
        print(n, 'is not prime')
    
    
    """
        range(stop) = 1 argument, 0,1,2,... stop - 1
        
        range(start, stop) start, start + 1, start +2 , start + 3, ... stop - 1
    
        range(start, stop, step)
    """
    n = int(input('What number do you want to check for primality: '))
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            
    if n == 1:
        is_prime = False
    
    if is_prime:
        print(n, 'is prime!!')
    else:
        print(n, 'is not prime')

"""
    List in python [array, vector]
    
    a data type which contains multiple possible variables/data
"""
my_list = [3, 'happy', 17, 'string', True, 2.7]
#          0      1     2     3       4     5

print(my_list)
"""
    In order to get an element out of a list you must use index notation
"""
print(my_list[3], my_list[0], my_list[4])

"""
    You can mix data types strings, ints, floats, even bools in a list:
        Generally don't
"""
#           0  1   2   3   4   5
new_list = [7, 18, 41, 57, 51, 39]
print(new_list)
for x in new_list:
    print(x, x + 5)

for index in range(len(new_list)):
    print(index, new_list[index])
    