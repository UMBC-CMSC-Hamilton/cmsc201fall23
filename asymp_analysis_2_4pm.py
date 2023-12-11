"""
    Our final is:
        Friday Dec 15th at 6-8pm
            Not a regular time, it's called a "common final"
            Rooms TBA - not going to be here
        I will probably release a practice test today or tomorrow.
"""

"""
    Asymptotic Analysis
        (Computational Complexity/ Complexity Theory)
    
    We want to ask how many steps our algorithms take as we increase the
        data size (n).
        
    If you remember the number of steps to do a selection sort is approximately
        n^2/2 where n is the size of the list.
    Basically the same for insertion and buble sort all take about n^2/2 steps.

my_var = other_var * 3 + something ** 2

    You may say, 1 step, or 4 steps or 6 steps
    
    Big-O notation: "it ignores constants"
    
        f(n) is O(g(n)) when there are constants C and N so that
            f(n) <= C g(n) for n >= N.
        C means we ignore constants
        N means "eventually"
    
    5n^2 - 2n + 1 is O(n^2)
    I get to pick the constant C, I pick 5.
    5n^2 - 2n + 1 <= 5n^2 ??
    
    pick N = 2, then you don't consider any values less than 2.
    
    n^2 is O(n^4) ? yes
    n^2 <= 1 * n^4
    minimum N for our purposes is always N = 0
    
    f(n) is O(g(n)) as long as
        lim_{n to infinity} f(n)/g(n) < infinity
        
    5n^2 - 3n + 7 is O(n^2)
    
    lim_{n -> inf} [5n^2 - 3n + 7] / n^2 = lim (10n - 3) / 2n = lim 10/2 = 5
    
    n^3 + 4n "is" O(n^2)
    
    lim_{n -> infinity} (n^3 + 4n)/n^2 = lim (3n^2 + 4)/2n = lim 6n / 2
    
    n^3 + 4n <= C n^2 should not be possible [and it's not]
    
    
    n^2 is O(2^n)
        lim_{n to infinity} [n^2]/[2^n] = lim 2n /[ 2^n ln(2) ]
        
            = lim 2 / [2^n (ln(2))^2)] = 0 < infinity
            
    Think about it this way:
        is n^2 < 2^n N > 1
        
"""


def a_and_b(n, current):
    """
        This is an O(2^n) function, so not great we have to be careful
    """
    if n == 0:
        print(current)
        return
    
    a_and_b(n - 1, current + 'a')
    a_and_b(n - 1, current + 'b')


def for_function_one(n):
    """
        This is an O(n) function which means that as the input increases
        by a factor of 10 the runtime will increase by a factor of 10
    """
    for i in range(n):
        print(i + 2)
        print(3 * i + 5)


def for_function_two(n):
    """
        O(n^2) time because of the nested loops
    """
    for i in range(n):
        for j in range(n):
            print(i + j)


def for_function_three(n):
    """
        When you have loops that are not nested you add their running time
        n + n which is 2n is O(n)
    """
    for i in range(n):
        print('blah')
    
    for j in range(n):
        print('other blah')


def for_function_four(n):
    """
        This is an O(n) function because sqrt(n) * sqrt(n) = n
    """
    for i in range(int(n ** (1 / 2))):
        for j in range(int(n ** (1 / 2))):
            print(i + j)


def for_function_five(n):
    """
        This will run n^3 / 2 steps which means it is O(n^3)
    """
    for i in range(n):
        for j in range(n):
            for k in range(n / 2):
                print(i - j + k)


def while_function_one(n):
    """
        The number of steps is n/3
        is O(n)  testable
    """
    
    current = 0
    while current < n:
        print(current, n)
        current += 3


def while_cube_root(n):
    current = 0
    total = 0
    while total < n:
        current += 1
        total += current ** 2
        

def while_function_two(n):
    """
        O(sqrt(n)) or O(sqrt(1 + 8n))
        will not happen too complex
        not on quiz, or final.
    """
    current = 0
    total = 0
    while total < n:
        current += 1
        total += current
        print(total, current)
    
    """
        1 + 2 + 3 + 4 + 5 ... + k = k(k + 1)/2
        n = k(k + 1)/2
        solve for k
        2n = k^2 + k
        k^2 + k - 2n = 0
        -1 + sqrt(1 - 4(1)(-2n))
        ------------------------ = -1/2 + sqrt(1 + 8n)/2 = k
                     2
    
    """


def binary_search(the_list, start, end, to_find):
    if start >= end:
        return False
    
    midpoint = (start + end) // 2
    if the_list[midpoint] == to_find:
        return True
    elif to_find < the_list[midpoint]:
        return binary_search(the_list, start, midpoint, to_find)
    else:
        return binary_search(the_list, midpoint + 1, end, to_find)


"""

n / 2^steps = 1
n = approx = 2^#steps

lg(n) = #steps
O(lg(n)) function

O(sin(n)) probably won't happen

"""


def while_log_business(n):
    """
        O(lg(n)) may happen
    """
    while n > 0:
        n //= 2
        print(n)


def get_max_of_list(the_list):
    current = the_list[0]
    for i in range(len(the_list)):
        if current < the_list[i]:
            current = the_list[i]

def for_example_six(n):
    """
        O(n^7) function
    """
    for i in range(n ** 2):
        for j in range(n ** 5):
            print(i * j)
