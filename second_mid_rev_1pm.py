"""
Write a boolean expression that returns True when the dictionary
 names contains "Eric" but does not contain "George"
"""
# this is to prevent Pycharm from yelling at me
names = {}
# this is the answer
"Eric" in names and "George" not in names

"""
Write a boolean expression that returns True when row is a
legal index for my_2d_list and col is a legal index for my_2d_list[row].
"""

# this is to prevent Pycharm from yelling at me
my_2d_list = [[]]
row = 0
col = 0
# here's what i want
0 <= row < len(my_2d_list) and 0 <= col < len(my_2d_list[row])
row in range(len(my_2d_list)) and col in range(len(my_2d_list[row]))
# technically you could theoretically do this but don't
-1 * len(my_2d_list) <= row < len(my_2d_list) and -1 * len(my_2d_list[row]) <= col < len(my_2d_list[row])

"""
    function name
    parameters
    function definition
    call
    body
    clockwise from the top left
    
    
    16) accessibility - locals can only be accessed from within the function
            that creates them, globals anywhere
        lifespace - locals only live as long as the function, globals until
            the program ends
    17) When opening a file, what are the three modes and what do they do?
        read   - read only opens the file, give you an error if it doesn't exist
        write  - opens the file, blanks it out, creates the file if it doesn't exist
        append - opens the file with write permissions, doesn't destroy the file
            allows you to write at the end of the file
    18) What is a boolean flag?
        a flag is a variable that flips from true-> false or false->true
        when a certain event happens.  It can trigger other events.
    19) Describe what can be done to a variable when it is passed by reference.
        Can it be modified inside the function?
        
        The parameter is a renaming of the original variable, not a copy.
        Yes, it can.
    
"""

a_list = [[2, 4, 6], [1, 2, 8], [3, 11, 17]]
for x in range(5, 7):
	print(a_list[x % 3][(2 * x + 2) % 3])

# a_list[5 % 3][(2 * 5 + 2) % 3]
# a_list[2][0] = 3
# a_list[6 % 2][(2 * 6 + 2) % 3] = a_list[0][2] = 6
"""
Number 21:
3
6
"""

test_string = "abracadabra"
# this is just to show you what happens half way through
print(test_string.split('a'))
# silly way to do replace
# just this part
print("z".join(test_string.split("a")))

"""
7 for row in range(LEN(the_board)):
8 count = 0
9 for col in range(len(the_board[row])):  (two errors)
10 if the_board[row][col] == letter:
14 return True rather than False
24 print(has_filled_row(the_board)) into
    print(has_filled_row(board, 'X'))


"""


def get_even_count(grid):
    evens = []
    for i in range(len(grid)):
        count = 0
        for j in range(len(grid[i])):
            if grid[i][j] % 2 == 0:
                count += 1
        evens.append(count)
    return evens


def average_lists(grid):
    num_elements = 0
    total = 0
    for i in range(len(grid)):
        num_elements += len(grid[i])
        for j in range(len(grid[i])):
            total += grid[i][j]
    if num_elements == 0:
        return 0
    return total / num_elements


"""
    New Problem:
        Remember a-b equality
        print out any sequence with more or equal to a's than b's
        
        aaab abab
        not abbb babb
        
        abbbaaaa
        
"""
def a_b_greater(n, k, current):
    if n == 0:
        if k >= 0:
            print(current)
        return
    
    a_b_greater(n - 1, k + 1, current + 'a')
    a_b_greater(n - 1, k - 1, current + 'b')


def count_squares(a_list):
    if not a_list:
        return 0
    """
    square_root = a_list[0] ** (1/2)
    if (int(square_root)) ** 2 == a_list[0]:
    """
    if a_list[0] ** (1/2) == int(a_list[0] ** (1/2)):
        return 1 + count_squares(a_list[1:])
    else:
        return count_squares(a_list[1:])

""""
1. Convert the binary number 0001 1110 0001 to decimal.
1 + 32 + 64 + 128 + 256 = 481

2. Convert the binary number 0000 0101 0101 to decimal.
1 + 4 + 16 + 64 = 85

3. Convert the decimal number 295 to binary.
295 -> 147 -> 73 -> 36 -> 18 -> 9 -> 4 -> 2 -> 1
0001 0010 0111
256 + 32 + 4 + 2 + 1 = 295

4. Convert the binary number 0111 1100 1001 0011 0101 1111 0000 to hexadecimal.

7C935F0

5. Convert the hexadecimal number 0xFE327D to binary. (Remember to space them in four-
blocks in order to make reading easier.)

1111 1110 0011 0010 0111 1101

"""