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
    
    ### ADD THE END CODE HERE TAKE THE REST OF THE LIST ###
    
    return result


def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    
    halfway = len(the_list) // 2
    first_half = the_list[0: halfway]
    second_half = the_list[halfway:]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    
    return put_together(first_half, second_half)
    

