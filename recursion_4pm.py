"""
    Recursion - idea is that functions can call themselves
    
"""


def my_function(count):
    print(count)
    
    if count == 100:
        return
    
    my_function(count + 1)


my_function(0)

"""
    Factorials
    
    n! = n(n - 1)(n - 2)(n - 3).... 1
    0! = 1
    
    To think recursively you ask "what if i knew the answer to 4!?"
    5! = 5 * 4!
    n! = n * (n - 1)!
"""


def iter_fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
rec_fact(5) = 5 * rec_fact(4) = 5 * 24 = 120
rec_fact(4) = 4 * rec_fact(3) = 4 * 6 = 24
rec_fact(3) = 3 * rec_fact(2) = 3 * 2 = 6
rec_fact(2) = 2 * rec_fact(1) = 2 * 1 = 2
rec_fact(1) = 1 * rec_fact(0) = 1 * 1 = 1
rec_fact(0) = 1
"""


def rec_fact(n):
    if n == 0:
        return 1
    print(f'calling recursive factorial on {n - 1}')
    result = rec_fact(n - 1) # this is where it gets paused
    print(f'returned from recursive factorial on {n - 1}')
    return n * result


"""
    Second math example: Fibonacci
    
    Fib(n) = Fib(n - 1) + Fib(n - 2)
    Fib(1) = 1
    Fib(0) = 1
"""

def rec_fib(n):
    """
        first example of branching recursion
    """
    if n <= 1:
        return 1
    print(f'fib({n}) Calling fib({n - 1})')
    result_1 = rec_fib(n - 1)
    print(f'fib({n}) Calling fib({n - 2})')
    result_2 = rec_fib(n - 2)
    return result_1 + result_2


def iter_fib(n):
    if n <= 1:
        return 1
    
    prev = 1
    prev_prev = 1
    current = 1
    for i in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    
    return current
    


k = int(input(">> "))
while k > -1:
    print(iter_fib(k))
    k = int(input(">> "))