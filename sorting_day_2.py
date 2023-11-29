"""

    https://visualgo.net/en/sorting
    
    We talked about bubble sort.

        exchanges adjacent elements
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



def merge_sort(the_list):
    if not the_list:
        return the_list

    halfway = len(the_list) // 2
    first_half = the_list[0: halfway]
    second_half = the_list[halfway:]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    return put_together(first_half, second_half)


print(put_together([3, 4, 8, 9], [1, 2, 5, 10, 20, 50]))


