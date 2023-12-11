"""
    Final Exam:
        Dec 15th 6-8 pm, Friday
            Rooms TBA

    Asymptotic Analysis
        (Computational Complexity)
        
        Way to analyze an algorithm to determine its runtime
            as a function of its input size.
            
        Three types of algorithms:
            1) internet ready - finish in a second or less
            2) Weather prediction - lives on the edge take a few days
                hours at least.
            3) Totally unrunnable - takes multiple lifetimes of the universe
                it'll finish after 10^20 * lifetime of the universe
"""

"""
    Let me talk about the main tool of asymptotic analysis: Big-O
    
    
    f(n) is O(g(n)) when there exists constants C, N so that
    f(n) <= C * g(n) when n >= N
    
    n^2 vs 5n^2 + 2n + 1
    
    lim_{n to infinity} [5n^2 + 2n + 1] / n^2 = 5
    
    What we want is a way to say that any "kind of N^2 function" is in the
        same family.  That's what O does for us.
        
    5n^2 + 2n + 1 <= 8 n^2
    C = 8
    N = 2
    
    How many steps does an algorithm take?
        7n^2 "steps"
        4n^2 "steps"
        
    my_var = 3 + other_var ** 2
    
    Bubble sort takes O(n^2) steps
    Selection sort takes O(n^2) steps
    Insertion sort takes O(n^2) steps
    
    Merge Sort takes O(n lg(n)) steps
    
    The function that doesn't grow as fast is actually better
        the function measures time, if time grows fast, that means the
        algorithm takes longer to run.
        
    QuickSort actually takes O(n^2) steps in the worst case.
        average case for quicksort is O(n lg(n))
        
    An algorithm that takes n^2 time or 2^n time? Which is better?
        n^2 algorithm will beat it because:
            plug in 10, 20, 30, 40 see that 2^n grows massively larger
        or:
            lim 2^n / n^2 = lim 2^n ln(2) / 2n = lim [ln(2)]^2 2^n / 2 = infinity
            2^n grows so much faster than n^2 that n^2 just dies in the limit
        
            lim 2^n / n^17 = infinity LHR
        
"""

def a_and_b(n, current):
    """"
        O(2^n) because we know that there are 2^n strings of a's and b's
            of length n.
            it's going to run print exactly 2^n times
    """
    if n == 0:
        print(current)
        return
    
    a_and_b(n - 1, current + 'a')
    a_and_b(n - 2, current + 'b')



def blah_function(x, y):
    """
        This is an O(xy) function
        if you pretend: x, y are both about n
        O(n^2)
    """

    for i in range(x):
        for j in range(y):
            print(i + j)


def new_function(n):
    """
        I'm running these loops n^3/2 times
        The good news about O is that what we do:
        O(n^3) could say O(n^3/2)
    """
    for i in range(n):
        for j in range(n):
            for k in range(n/2):
                print(i + j - k)
                
    
def square_rooty_function(n):
    """
        This runs O(n) times because sqrt(n) * sqrt(n) = n
    """
    for i in range(int(n ** (1/2))):
        for j in range(int(n ** (1 / 2))):
            print(i * j)
            
            
def two_loops(n):
    """
        O(2n) or O(n) function, the loops MUST be nested to multiply
        if the loops aren't nested you add
    """
    for i in range(n):
        print(2 * i)
    for j in range(n):
        print(3 * j)
        

def two_loops_again(n):
    """
        n^3 + n type function
        O(n^3) - always looking at the highest order term.
    """
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i + j + k)
    
    for r in range(n):
        print(r)


def function_2(n):
    for i in range(n):
        print(i + 5)

def function_1(n):
    """
        This is O(n^2)
    """
    for i in range(n):
        function_2(n)
        
"""
    You can't hide calculations.
"""


def selection_sort(the_list):
    for start in range(len(the_list) - 1):
        min_index = start
        for i in range(start + 1, len(the_list)):
            if the_list[min_index] > the_list[i]:
                min_index = i
        if min_index != start:
            temp = the_list[min_index]
            the_list[min_index] = the_list[start]
            the_list[start] = temp
    
    return the_list

"""
    n - 1 + (n - 2) + (n - 3) + ... + 1 = gauss sum from 1 to n - 1
    (n - 1)*(n) / 2 steps = n^2/2 - n/2 is O(n^2)
"""


def insertion_sort(the_list):
    for i in range(1, len(the_list)):
        current = i
        # short circuiting - on an and statement if the first prong is false
        # it doesn't check the second prong.
        # for current in range(i, 0, -1):
        while current > 0 and the_list[current - 1] > the_list[current]:
            temp = the_list[current]
            the_list[current] = the_list[current - 1]
            the_list[current - 1] = temp
            
            current -= 1
    return the_list
"""
1 + 2 + 3 + 4 + ... + (n - 1) = (n - 1)* n / 2 = O(n^2)
"""

"""
Definitely not going to expect you to deal with exponential running times:
    You will not have to calculate the running time of an exponential function
Might ask for the running times of:
    insertion, selection, merge sort
    
    stay away from quick sort - rather complex analysis
        average time of O(n lg(n)) but worst case O(n^2)

    make a function up like the ones in the examples, they're mostly good
        except a's and b's really.
        
    Know the gauss sum:
        1 + 2 + 3 + 4 + ... + n = n(n + 1)/2
    
    Know the running time of binary search O(lg(n))
"""


def binary_search(a_list, start, end, to_find):
    if start >= end:
        return False
    midpoint = (start + end) // 2

    if a_list[midpoint] == to_find:
        return True
    elif to_find < a_list[midpoint]:
        return binary_search(a_list, start, midpoint, to_find)
    else:
        return binary_search(a_list, midpoint + 1, end, to_find)
"""
    binary search will run until:
    n/ 2^steps = approx = 1
    n = 2^steps
    lg(n) = #steps
    O(lg(n))
    remember that O(lg(n)) is going to beat O(n)
    
    Best case: O(1) constant time
        technically Omega when you get to 341 but just wait for that
        
    If an algorithm takes 5 steps or 10 steps, or just 1 step
    we call it "constant time" O(1)
    could call it O(5) or O(10) but you just won't ever see this in any book
"""