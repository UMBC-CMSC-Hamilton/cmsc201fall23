"""
Write a boolean expression that returns True when the dictionary
names contains "Eric" but does not contain "George"
"""
names = {}
# this is what i want:
"Eric" in names and "George" not in names

"""
Write a boolean expression that returns True when row is a legal index
    for my_2d_list and col is a legal index for my_2d_list[row].

    legal = between 0 and the length of the list
"""
my_2d_list = [[]]
row = 0
col = 0
# this is the answer here:
0 <= row < len(my_2d_list) and 0 <= col < len(my_2d_list[row])
row in range(len(my_2d_list)) and col in range(len(my_2d_list[row]))

"""
16) What are some differences between a global and local variable? (Name at least two.)
    Accessibility - You can access global varaiables anywhere in a program
        but local variables only in the function where they were created
    Lifespan - A global variable lives as long as the program does,
        local variables live until the end of the function
17) When opening a file, what are the three modes and what do they do?
    read - opens the file, sets the cursor to the beginning allows reading
        read mode will raise a file doesn't exist error
    write - opens the file, blanks it out, sets the cursor to the start,allows writing
        will create the file if it doesn't exist
    append - open the file with write permissions, sets the cursor at the end
        will create the file if it doesn't exist

18) What is a boolean flag?
    A boolean variable that tracks a state in the program.  When that state changes, the
        variable flips from T-> F or F-> T and then allows other parts of the program to
        trigger.
        
        is_prime flag if you are scanning through divisors
        game_over flag if you're playing a game
19) Describe what can be done to a variable when it is passed by reference.
    Can it be modified inside the function?

    Passing a variable by reference allows us to change that variable inside of a function.
    Yes. Not a copy, it's actually the underlying object/variable.
    In python mutables pass by reference, immutables by value.

    int do_something(int x, int & y);

20)         3
            0
            
    Reason: .get method won't return a KeyError. If the key is not in the dictionary
        it will return the second argument that you pass into it.  If you don't use the
        second argument it will return None.
"""

new_dictionary = {'apple': [1, 2, 3, 7], 'banana': [13, 4, 9, 18]}
print(new_dictionary.get("random"))
print(new_dictionary['apple'][2])
print(new_dictionary.get('apple')[2])

a_list = [[2, 4, 6], [1, 2, 8], [3, 11, 17]]
for x in range(5, 7):
	print(a_list[x % 3][(2 * x + 2) % 3])
"""
    work:
        a_list[5 % 3][(2* 5 + 2) %3]
        a_list[2][0]) = 3
        
        a_list[6 % 3][(2 * 6 + 2) %3]
        a_list[0][2] = 6
    answer:
        3
        6
"""

test_string = "abracadabra"
print("z".join(test_string.split("a")))
print(test_string.split('a'))
print('aaaa'.split('a'))

"""
7) for row in range(the_board): -> for row in range(len(the_board)):
8) count = 0 [because counting from 1 is not for us]
9) Add colon. and for col in range(len(the_board[row])):
10) if the_board[row][col] == 'X': to if the_board[row][col] == letter:
14) return True
24) either add the argument "X" or "O" whichever.
    add board instead of the_board
        print(has_filled_row(board, "X"))
"""

def get_even_count(grid):
    even_list = []
    for i in range(len(grid)):
        count = 0
        for j in range(len(grid[i])):
            if grid[i][j] % 2 == 0:
                count += 1
        even_list.append(count)
    return even_list


def average_lists(grid):
    num_elements = 0
    total = 0
    for i in range(len(grid)):
        # num_elements += len(grid[i])
        for j in range(len(grid[i])):
            total += grid[i][j]
            num_elements += 1
    if num_elements == 0:
        return 0
    
    return total / num_elements
