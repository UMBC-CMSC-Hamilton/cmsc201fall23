import random
import time

"""
    https://visualgo.net/en/sorting
    Bubble Sort again
    Selection Sort
    Insertion Sort
    
    Merge Sort
"""

"""
    version of the question you'll see on the final.

    [2, 5, 4, 1, 7, 2, 9]
    [2, 4, 1, 5, 2, 7, 9] - first cycle of bubble sort
    [2, 1, 4, 2, 5, 7, 9] - second cycle
    [1, 2, 2, 4, 5, 7, 9] - third cycle
    [1, 2, 2, 4, 5, 7, 9] - fourth cycle (final check)

    bubble sort compares adjacents
"""


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
    
    return the_list


"""
Selection Sort - Find Min Sort

scans through the list, finds the minimum and swaps it
    into the correct position

[4, 9, 7, 4, 5, 2, 1] i = 0
[1, 9, 7, 4, 5, 2, 4] i = 1
[1, 2, 7, 4, 5, 9, 4] i = 2
[1, 2, 4, 7, 5, 9, 4] i = 3
[1, 2, 4, 4, 5, 9, 7] i = 4
[1, 2, 4, 4, 5, 9, 7] i = 5
[1, 2, 4, 4, 5, 7, 9] (done)
"""


def selection_sort(the_list):
    for i in range(len(the_list) - 1):
        min_index = i
        for j in range(i + 1, len(the_list)):
            if the_list[j] < the_list[min_index]:
                min_index = j
        
        if min_index != i:
            temp = the_list[min_index]
            the_list[min_index] = the_list[i]
            the_list[i] = temp
    
    return the_list


"""
    Insertion Sort - pull back sort

    [3, 1, 9, 2, 7, 3, 5, 6] i = 0
    [1, 3, 9, 2, 7, 3, 5, 6] i = 1
    [1, 3, 9, 2, 7, 3, 5, 6] i = 2 [no swaps]
    [1, 2, 3, 9, 7, 3, 5, 6] i = 3
    [1, 2, 3, 7, 9, 3, 5, 6] i = 4
    [1, 2, 3, 3, 7, 9, 5, 6] i = 5
    [1, 2, 3, 3, 5, 7, 9, 6] i = 6
    [1, 2, 3, 3, 5, 6, 7, 9] i = 7


    [1, 2, 3, 4, 5, 6, 7, 8] - great list for insertion sort
    
    [8, 7, 6, 5, 4, 3, 2, 1] - worst case for insertion sort
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
    Merge Sort
    
    [4, 6, 2, 9, 5, 1, 7, 3]
    [4, 6, 2, 9] [5, 1, 7, 3]
    [4, 6] [2, 9] [5, 1] [7, 3]
    [4] [6]     [2] [9]     [5] [1]     [7] [3]
    [4, 6] [2, 9] || [1, 5] [3, 7]
    [2, 4, 6, 9]     [1, 3, 5, 7]
    [1, 2, 3, 4, 5, 6, 7, 9]
    
    
    [1, 7, 3, 4, 2, 9, 1, 5, 4, 8, 7, 2, 1]
    [1, 7, 3, 4, 2, 9] [1, 5, 4, 8, 7, 2, 1]
    [1, 7, 3] [4, 2, 9] [1, 5, 4, 8] [7, 2, 1]
    
"""

def put_together(first_list, second_list):
    first_index = 0
    second_index = 0
    result = []
    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
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


def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    # print('breaking apart', the_list)
    halfway = len(the_list) // 2
    first_half = the_list[0: halfway]
    second_half = the_list[halfway:]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    # print('about to put together: ', first_half, second_half)
    
    return put_together(first_half, second_half)
    

"""
    2^4 = 16 ... is that relevant? hmm...
    size 16
    2 x size 8
    4 x size 4
    8 x size 2
    16 x size 1
    
    2^7 == 128
    128 list
    2x 64
    4x 32
    8x 16
    16x 8
    32x 4
    64x 2
    128x 1
    
    n/2^steps = 1
    
    57 basically if you just round up to the next power of two
        the same number of steps will happen
    1x 28 - 1x 29
    2x 14 - 1x14 1x15
    6x 7 - 1x7 - 1x8
    
    
    n/2^steps = 1
    n = 2^steps
    log_2(n) = #steps
    
    Each step costs approximately n operations put together function
        looks through each element once.
        
    Merge Sort runs in n * lg(n) time
    lg(n) = log_2(n)
    ln(x) = log_e(x)
    log(x) = log_10(x)
    
    Last time, bubble, insertion and selection sort take about n^2 operations
    
    Merge sort takes n lg(n) operations
    
    Who wins?
        What does it mean to win?
            doing fewer operations is what we probably mean by winning
            number of operations ~ amount of time
            
    T(selection) ~ n^2
    T(merge) ~ n ln(n)
    Who wins?
    
    lim{n -> infinity} n lg(n) / n^2 = lim lg(n) / n
    L-Hopital's rule:
    lim 1/n / 1 = lim_{n to infinity} 1/n = 0
"""


"""
    pivot = first element of the list
    create a less list and greater list
    less list = all the elements less than the pivot
    greater list = all the elements greater than or equal to the pivot
    
    don't add the pivot to the greater list (or any list really)
"""
def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    
    pivot = the_list[0]
    greater_list = []
    less_list = []
    equal_list = []
    for i in range(len(the_list)):
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        elif the_list[i] == pivot:
            equal_list.append(the_list[i])
        else:
            greater_list.append(the_list[i])
    
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)
    return less_list + equal_list + greater_list

"""

[5, 4, 9, 6, 7, 3, 1, 2] pivot = 5
QS[4, 3, 1, 2] + 5 + QS[9, 6, 7]

QS[4, 3, 1, 2] pivot = 4
QS[3, 1, 2] + 4 + [] = [1, 2, 3, 4]
QS[3, 1, 2] pivot = 3
[1, 2] + 3 + [] ==> [1, 2, 3]
QS[1, 2] pivot = 1
[] + 1 + [2] ==> [1, 2]

QS[9, 6, 7] pivot = 9
[6, 7] + 9 + [] ==> [6, 7, 9]
QS[6, 7]
[] + 6 + [7] ==> [6, 7]

==> [1, 2, 3, 4, 5, 6, 7, 9]

[4, 7, 9, 1, 2, 6, 8] show me a step of quicksort
[1, 2] + 4 + [7, 9, 6, 8]


[1, 2, 3, 4, 5, 6, 7, 8, 9]
[] + 1 + [2, 3, 4, 5, 6, 7, 8, 9]
QS[2, 3, 4, 5, 6, 7, 8, 9] = [] + 2 + [3, 4, 5, 6, 7, 8, 9]
QS[3, 4, 5, 6, 7, 8, 9] = [] + 3 + [4, 5, 6, 7, 8, 9]
...

"""




def time_test(size, the_sort):
    new_list = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.process_time()
    the_sort(new_list)
    end_time = time.process_time()
    print(f'The sort {the_sort.__name__} took ', end_time - start_time, 'seconds')



for size in [1000, 10000, 50000, 100000, 250000, 1000000]:
    print('Testing on size', size)
    time_test(size, quick_sort)
    time_test(size, merge_sort)
    
