"""

    Recursion is a different way to solve problems.
        Normally in programming you think about iteration:
            loops
        
        Think Differently:
            Can i break this into subproblems?
                Can I do one step of this and then get the result
                    merge them together?
                    
        Not so good: n! = n (n - 1)(n - 2) ... (3)(2)(1)
        0! = 1
        
        Good: 0! = 1
             n! = n * [(n - 1)!]
             fact(n) = n * fact(n - 1)
             If you don't know what 5! is but I tell you 4! = 24
             then all you do is 5 * 24 = 120 and you're done
"""


def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

"""
    recursion is like stacking up blocks
    
    rf(0) = base case you can stop stacking blocks now
    rf(1) => next block to come off the stack
    rf(2) => 2nd block
    rf(3) => 3rd block to come off the stack
    rf(4) => 4th block
    rf(5) => last block
"""
def recursive_factorial(n):
    # input(f'n is {n}')
    if n == 0:
        return 1
    print(f'Calculating rf({n - 1})')
    result = recursive_factorial(n - 1)
    print(f'About to return {n} * {result}')
    return n * result



"""
    Fibonacci numbers:
        Fib(n) = Fib(n - 1) + Fib(n - 2)
        Need a base case
        Pick Fib(1) = 1
             Fib(0) = 1
"""

def rec_fib(n):
    if n <= 1:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)

def iter_fib(n):
    """
        Fib(n) = (phi^n - phi^{-n}) / sqrt(5)
        phi = (1 + \sqrt{5})/2
    
    :param n:
    :return:
    """
    prev = 1
    prev_prev = 1
    if n <= 1:
        return 1
    current = 1
    for i in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    
    return current


"""
    palindromes but recursive this time:
    
    abcdcba
    a     a
     bcdcb
     b   b
      cdc
      c  c
        d => base case
    
    racetar
    r     r
     aceta
     a   a
      cet => Return False

    abcddcba
     bcddcb
      cddc
       dd
        empty
"""

def rec_pal(word):
    if len(word) <= 1:
        return True
    
    if word[0] == word[len(word) - 1]:
        return rec_pal(word[1: len(word) - 1])
    else:
        return False
        

k = int(input(">> "))
while k > -1:
    print(iter_fib(k))
    k = int(input(">> "))
