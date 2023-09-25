"""
    draw a triangle program
"""

size = int(input('What size triangle do you want? '))
for i in range(size):
    # i represent the row [line that we're currently outputing]
    for j in range(i + 1):
        # j represents the column current character
        print('*', end='')
        # turns off the enter character at the end of print
    print()  # gives us the endline after the inner loop

print('\n')

for i in range(size):
    # i represent the row [line that we're currently outputing]
    for j in range(size - i):
        # j represents the column current character
        print('*', end='')
        # turns off the enter character at the end of print
    print()  # gives us the endline after the inner loop

"""
       *
      **
     ***
    ****
   *****
  ******
 *******
********
"""

for i in range(size):
    # i represent the row [line that we're currently outputing]
    for j in range(size):
        # j represents the column current character
        if j < i:
            print(' ', end="")
        else:
            print('*', end='')
        # turns off the enter character at the end of print
    print()  # gives us the endline after the inner loop

for i in range(size):
    # i represent the row [line that we're currently outputing]
    for j in range(size):
        # j represents the column current character
        if j < size - i - 1:
            print(' ', end="")
        else:
            print('*', end='')
        # turns off the enter character at the end of print
    print()  # gives us the endline after the inner loop

"""
    2-D lists
    
    Lists can contain ints, floats, bools, strings
        Lists can also contain lists.
"""

my_double_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 11, 12]
]

print(len(my_double_list))
"""
When you use an index on a 2d list you get a sublist
"""
print(my_double_list[2])
print(my_double_list[2][1], my_double_list[3][2])

for i in range(len(my_double_list)):
    # whenever you scan through an inner list, remember
    # you need to take its length not the length of the outer list
    for j in range(len(my_double_list[i])):
        print(my_double_list[i][j], end=' ')
    print()

new_list = [
    [1, 2, 3],
    [3, 4, 5, 6, 7, 8, 9],
    ['a', 'b'],
    [2, 4, 6, 8, 10],
    [1, 1, 2, 3, 5, 8, 13, 21, 34]
]

for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        print(new_list[i][j], end=' ')
    print()
    
"""
    Tic Tac Toe
        draw the board:
            ok that's a little work
        determine whose turn it is:
            use mod trick (evens is X, odds is O), count = 0
        get the user's move:
            check that the user has entered a valid move
            if they haven't force them to
        make the move
        victory checker
            80% of the work
"""

SIZE = 3

the_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

player_turn = 0

for i in range(SIZE):
    print(the_board[i][0], '|', the_board[i][1], '|', the_board[i][2])
    if i < SIZE - 1:
        print('--+---+--')
        
for row in range(len(the_board)):
    first_value = the_board[row][0]
    if first_value != ' ':
        row_victory = True
    else:
        row_victory = False
    for col in range(len(the_board[row])):
        if the_board[row][col] != first_value:
            row_victory = False
    print(first_value, 'has won')

for col in range(len(the_board)):
    first_value = the_board[0][col]
    if first_value != ' ':
        col_victory = True
    else:
        col_victory = False
    for row in range(len(the_board)):
        if the_board[row][col] != first_value:
            col_victory = False
    if col_victory:
        print(first_value, 'has won')
        
diagonal = the_board[0][0]
if diagonal != ' ':
    diag_victory = True
else:
    diag_victory = False
for i in range(len(the_board)):
    if diagonal != the_board[i][i]:
        diag_victory = False
