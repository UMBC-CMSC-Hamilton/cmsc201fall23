"""

    https://visualgo.net/en/sorting
    
    We talked about bubble sort.

        exchanges adjacent elements
"""

import time
import random


def bubble_sort(the_list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(the_list) - 1):
            if the_list[i] > the_list[i + 1]:
                temp = the_list[i]
                the_list[i] = the_list[i + 1]
                the_list[i + 1] = temp
                is_sorted = False


"""
    Selection Sort - find min sort
        find the min element, then swap it
        advance to next position, do it again.
        
        [3, 2, 8, 1, 9, 5] min = 1, i = 0
        [1, 2, 8, 3, 9, 5] min = 2, i = 1
        [1, 2, 8, 3, 9, 5] min = 3, i = 2
        [1, 2, 3, 8, 9, 5] min = 5, i = 3
        [1, 2, 3, 5, 9, 8] min = 8, i = 4
        [1, 2, 3, 5, 8, 9] min = 9, i = 5
    
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
    [4, 9, 2, 7, 8, 1]
    [1, 9, 2, 7, 8, 4]
    [1, 2, 9, 7, 8, 4]
    [1, 2, 4, 7, 8, 9]
    [1, 2, 4, 7, 8, 9]
    [1, 2, 4, 7, 8, 9]
    
    
    Selection sort will run the same steps regardless of the structure
    of the list
    
    What is the runtime of this sort?
        n^2 - sum from s = 1 to n of s
        n^2 - gauss sum from 1 to n
        n^2 - n(n + 1)/2
        n^2 - n^2/2 - n/2 = n^2/2 - n/2
    All cases are the same: best == average == worst case
        n^2/2 steps.    Theta(n^2)
        
        5 seconds to sort a list of size 1,000
        500 seconds to sort a list of size 10,000
"""

"""
[5, 4, 9, 8, 3, 1]
i = 1 [4, 5, 9, 8, 3, 1] I can pull 4 back by 1 position
i = 2 [4, 5, 9, 8, 3, 1] I can't pull 9 back since it's sorted already
i = 3 [4, 5, 8, 9, 3, 1] I can pull back 8 by one element and then it stops
i = 4 [3, 4, 5, 8, 9, 1] I have to pull 3 back by 4 positions

i = 5 [3, 4, 5, 8, 1, 9] current = 5
i = 5 [3, 4, 5, 1, 8, 9] current = 4
i = 5 [3, 4, 1, 5, 8, 9] current = 3
i = 5 [3, 1, 4, 5, 8, 9] current = 2
i = 5 [1, 3, 4, 5, 8, 9] current = 1
    current = 0
    
i = 5 [1, 3, 4, 5, 8, 9] I have to pull 1 back all the way.

"""


"""
If you have a list of size n, then you are doing n things if the list is
    sorted
"""


def insertion_sort(the_list):
    """
        pull back sort
        Also quadratic because its worst case runtime is
            sum of i from 1 to n which means n(n + 1)/2
    """
    for i in range(1, len(the_list)):
        
        current = i
        while current > 0 and the_list[current] < the_list[current - 1]:
            # swap first
            temp = the_list[current]
            the_list[current] = the_list[current - 1]
            the_list[current - 1] = temp
            # decrement current
            current -= 1

    return the_list

"""
    Begin MergeSort
    
    What happens if you divide the list in half?
    
    [4, 5, 2, 1, 7, 9, 3, 2]
    [4, 5, 2, 1]    [7, 9, 3, 2]
    [4, 5] [2, 1]   [7, 9] [3, 2]
    [4] [5]     [2] [1]       [7] [9]       [3] [2]
Rejoin them but in sorted order:
    [4, 5]      [1, 2]        [7, 9]        [2, 3]
    [1, 2, 4, 5]      [2, 3, 7, 9]
    [1, 2, 2, 3, 4, 5, 7, 9] - sorted
    
"""

def put_together(first_list, second_list):
    """
        assumes that both lists are already sorted
    """
    result = []
    first_index = 0
    second_index = 0
    while first_index < len(first_list) and second_index < len(second_list):
        # want to take the smaller thing whatever it is
        if first_list[first_index] <= second_list[second_index]:
            result.append(first_list[first_index])
            first_index += 1
        else:
            result.append(second_list[second_index])
            second_index += 1

    for i in range(first_index, len(first_list)):
        result.append(first_list[i])
    for j in range(second_index, len(second_list)):
        result.append(second_list[j])
    
    return result

"""
    [size 16]
    [size 8] [size 8] ==> cost is 8 + 8
    [size 4] [size 4] [size 4] [size 4] ==> cost here is 4 + 4 + 4 + 4
    [size 2] [size 2][size 2][size 2][size 2][size 2][size 2][size 2] ==>
            2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 = 16
    [1] [1] [1] [1] [1] [1] [1] [1] [1] [1] [1] [1] [1] [1] [1] [1]
    1 + 1 + 1 ... + 1 = 16 = n
    
    57
    [size 28] [size 29]
    [size 14] [size 14][size 14] [size 15]
    [size 7] [size 7] [size 7] [size 7] [size 7] [size 7] [size 7] [size 8]
    [3] [4] [3] [4] [3] [4] [3] [4] [3] [4] [3] [4] [3] [4] [4] [4]
    [2][1] [2][2] [2][1] [2][2] [2][1] [2][2] [2][1] [2][2] [2][1] [2][2] [2][1] [2][2] [2][1] ...
    [1] .... x 57  = n
    
    ((n /2)/(2 / 1))/2 ... /2 ~= 1
    n/4 /2 /2 /2 .../2
    n/8... n/16  n/32 ...
    
    n/2^k = 1
    n = 2^k
    log_2(n) = k = #steps that it requires to get down to lists of size 1
    round_up(log_2(n))
    
    Total cost to run merge sort is:
    n * lg(n) = #steps ~ time
    
    lg(n) = log_2(n)
    ln(x) = log_e(x)
    log(x) = log_10(x)
    
    The costs of our previous sorts were about #steps ~ time = n^2
    
    we want our algorithm to run fewer steps if possible
    
    so now the question is which is less?
    n lg(n) vs n^2 ???
    
    lim_{n to infinity} n lg(n) / n^2 = lim lg(n) / n = lim 1/n = 0
"""

def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    # it breaks a list in half
    halfway = len(the_list) // 2
    first_half = the_list[0: halfway]
    second_half = the_list[halfway:]
    # sorts both halves
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    # returns the merge/put_together of the sorted halves
    return put_together(first_half, second_half)



"""
    QuickSort
    
        relies on something called a pivot first element in the list
        create two lists
        less list = all the elements less than pivot
        greater list = all elements greater than or equal to the pivot
        
        don't put the pivot in either list <-- important
        
        
        [3, 5, 9, 2, 7, 1, 4] pivot = 3
        QS[2, 1] + 3 + QS[5, 9, 7, 4]
        [2, 1] pivot = 2
        [1] + 2 + [] = [1, 2]
        [5, 9, 7, 4] pivot = 5
        QS[4] + 5 + QS[9, 7]
        
        QS[9, 7] pivot = 9
        [] + 7 + [9] = [7, 9]
        [4, 5, 7, 9]
        
        [1, 2, 3, 4, 5, 7, 9]
        ======================== Example 2========================
        QS[1, 2, 3, 4, 5] pivot = 1
        [] + 1 + QS[2, 3, 4, 5]
        QS[2, 3, 4, 5] pivot = 2
        [] + 2 + QS[3, 4, 5]
        QS[3, 4, 5] pivot = 3
        [] + 3 + [4, 5]
        QS[4, 5] pivot = 4
        [] + 4 + [5] = [4, 5]
        [1, 2, 3, 4, 5]
        
        problem: the list size only decreases by one each time
        instead of the number of steps being logarithmic, it is like n.
    
"""
def quicksort(the_list):
    if len(the_list) <= 1:
        return the_list
    pivot = the_list[0]
    less_list = []
    equal_list = []
    greater_list = []
    # skipping element 0 because i'm not the the pivot in either list
    for i in range(len(the_list)):
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        elif the_list[i] == pivot:
            equal_list.append(the_list[i])
        else:
            greater_list.append(the_list[i])
    less_list = quicksort(less_list)
    greater_list = quicksort(greater_list)
    return less_list + equal_list + greater_list
    


L = []
# actually uses a modified merge sort + insertion sort
L.sort()

def time_test(size, the_sort):
    new_list = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.process_time()
    the_sort(new_list)
    end_time = time.process_time()
    print(f'The sort took {end_time - start_time} seconds')


import sys


sys.setrecursionlimit(100000)

for size in [1000, 10000, 100000, 1000000]:
    print('Running test on size', size)
    time_test(size, merge_sort)
    time_test(size, quicksort)

start_time = time.process_time()
sorted_list = [i for i in range(1000)]
quicksort(sorted_list)
print('Done', time.process_time() - start_time)