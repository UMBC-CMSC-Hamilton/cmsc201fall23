"""
nested for loops
2d lists
maybe while but probably wednesday
"""

size = int(input('What size do you want? '))

for i in range(size):
    for j in range(size):
        print(f'({i}, {j})', end=' ')
    print()

for i in range(size):
    for j in range(size):
        if i >= j:
            print('*', end='')
    print()

print('\n')

for i in range(size):
    for j in range(size):
        if i + j <= size - 1:
            print('*', end='')
    print()

"""
Want:

           *
          **
         ***
        ****
       *****
      ******
     *******
    ********
   *********
  **********
 ***********
************
"""

for i in range(size):
    for j in range(size):
        if i > j:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(size):
    for j in range(size):
        if i + j < size - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

if False:
    for i in range(size):
        print(f'i is {i}')
        for j in range(size):
            print(f'j is {j}')
        input('>> ')

"""
    Last week we "remember" that lists can be composed of data
        data can be ints, floats, bools, strings
        data can also be lists
"""

my_list = [
    [1, 2, 3],  # index 0
    [4, 5, 6],  # index 1
    [9, 8, 7],  # index 2
    [10, 11, 13]  # index 3
]
print("L = ", len(my_list))
my_index = int(input("What index do you want? "))
if 0 <= my_index < len(my_list):
    print(my_list[my_index])
else:
    print('Bad human!')

"""
    The super important thing to know is that the inner list
        can have a different length to the outer list


    What if I want to access a particular value?
    
"""
print(my_list[1][1], my_list[2][0])
my_list[2][2] = 14
print(my_list)

for row in my_list:
    print(row)

wierd_list = [
    [3, 9, 12, 15],
    [7, 77, 343, 28, 49],
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],
    ['a', 'b', 'c']
]

wierd_list.append([4, 5, 6])

for row in range(len(wierd_list)):
    for j in range(len(wierd_list[row])):
        print(wierd_list[row][j], end='\t')
    print()

number_list = [1, 2, 3, 4, 5, 10, 12, 15, 20]
position = int(input('Where to insert (the actual position)? '))
what_to_insert = int(input('Give me a number: '))

number_list.append(0)
for i in range(len(number_list) - 2, position - 1, -1):
    number_list[i + 1] = number_list[i]

number_list[position] = what_to_insert

print(number_list)
number_list.insert(3, 15)
print(number_list)

"""
    TicTacToe
    
    Pick X or O
    
    keep track of the turn (use turn % 2 to figure out which turn it is)
    
    we need a board which is a 2d list (3x3)
    
    get user input and validate (check to make sure that the user
        has entered a board position, board must be empty there)
    
    victory check <-- we're going to work on this part
"""

my_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

for i in range(len(my_board)):
    first_element = my_board[i][0]
    if first_element == ' ':
        row_victory = False
    else:
        row_victory = True
    for j in range(len(my_board[i])):
        if my_board[i][j] != first_element:
            row_victory = False
    if row_victory:
        print(first_element, 'has won')
        

for col in range(len(my_board)):
    first_element = my_board[0][col]
    if first_element == ' ':
        col_victory = False
    else:
        col_victory = True
    for row in range(len(my_board[i])):
        if my_board[row][col] != first_element:
            col_victory = False
    if col_victory:
        print(first_element, 'has won')
        
if anti_diag_element != ' ':
    diag_victory = True
else:
    diag_victory = False
diag_victory = True

for i in range(len(my_board)):
    if my_board[i][i] != diag_element:
        diag_victory = False
        
if diag_victory:
    print('Diagonal victory for ', diag_element)
    
anti_diag_element = my_board[0][0]
if anti_diag_element != ' ':
    anti_diag_victory = True
else:
    anti_diag_victory = False
for i in range(len(my_board)):
    if my_board[i][len(my_board) - 1 - i] != anti_diag_element:
        anti_diag_victory = False
        
if anti_diag_victory:
    print('Anti-Diagonal victory for ', anti_diag_element)
