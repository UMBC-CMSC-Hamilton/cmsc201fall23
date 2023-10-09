"""
    Functions
    
"""


def counts_the_as(a_string):
    """
        This function takes a string and counts the number of a's in it1
        :return: integer which is the count
    """
    count = 0
    for x in a_string:
        if x.lower() == 'a':
            count += 1
    # remember that whatever the function needs to communicate
    # back to the original program it should return
    return count


ALPHA_SIZE = 26


def letter_counts(the_string):
    counts = []
    for i in range(ALPHA_SIZE):
        counts.append(0)
    
    for x in the_string:
        index = ord(x.lower()) - ord('a')
        if 0 <= index < ALPHA_SIZE:
            counts[index] += 1
    
    return counts


print(letter_counts('abcd'))
print(letter_counts('ababababa!.abbababababaababababababaaba'))
print(letter_counts('zyzzyzyxxkldswnonewgnlkwnoewsgnosnvoisngwsi'))

"""
Factorization:

"""


def is_prime(n):
    """
    :param n: a number to test for primality
    :return: True or False if it is prime or not
    """
    if n < 2:
        return False
    
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            # as soon as this line happens, the function terminates
            return False
    # this will return after the loop completes
    return True


num = int(input('Tell me a number: '))
while num != 0:
    print(is_prime(num))
    num = int(input('Tell me a number: '))

SPACE = ' '
TTT_X = 'x'
TTT_O = 'o'

the_symbols = [TTT_X, TTT_O]


def check_rows(the_board, symbols):
    """
    :param the_board: 3x3 grid with the symbols or spaces
    :param symbols: the X and O symbols for TTT
    :return: the symbol of the winner OR space if no winner
    """
    for row in range(len(the_board)):
        # takes the first element of any particular row
        first_symbol = the_board[row][0]
        if first_symbol in symbols:
            for col in range(len(the_board[row])):
                if the_board[row][col] != first_symbol:
                    first_symbol = SPACE
        if first_symbol in symbols:
            return first_symbol
    
    return SPACE


def check_cols(the_board, symbols):
    for col in range(len(the_board[0])):
        first_symbol = the_board[0][col]
        if first_symbol in symbols:
            for row in range(len(the_board)):
                if the_board[row][col] != first_symbol:
                    first_symbol = SPACE
        if first_symbol in symbols:
            return first_symbol
    
    return SPACE


def check_diagonals(the_board, symbols):
    diagonal = the_board[0][0]
    for i in range(len(the_board)):
        if diagonal != the_board[i][i]:
            diagonal = SPACE
    
    anti_diagonal = the_board[len(the_board) - 1][0]
    for i in range(len(the_board)):
        if anti_diagonal != the_board[i][len(the_board) - 1 - i]:
            anti_diagonal = SPACE
    
    if diagonal in symbols:
        return diagonal
    if anti_diagonal in symbols:
        return anti_diagonal
    return SPACE


def check_victory(the_board, symbols):
    row_victory = check_rows(the_board, symbols)
    col_victory = check_cols(the_board, symbols)
    diag_victory = check_diagonals(the_board, symbols)
    if row_victory != SPACE:
        return row_victory
    if col_victory != SPACE:
        return col_victory
    if diag_victory != SPACE:
        return diag_victory
    return SPACE


def get_user_position():
    position = input('Enter the position that you want to move as (abc)(123)')
    while position[0] not in ['a', 'b', 'c'] or \
            position[1] not in ['1', '2', '3']:
        position = input('Enter the position that you want to move as (abc)(123)')
    
    x = ord(position[0]) - ord('a')
    y = int(position[1]) - 1
    return [x, y]


def display_board(the_board):
    for i in range(len(the_board)):
        print(' | '.join(the_board[i]))
        if i < 2:
            print('---------')


def tic_tac_toe_game():
    turn = 0
    symbols = [TTT_X, TTT_O]
    the_board = [
        [SPACE, SPACE, SPACE],
        [SPACE, SPACE, SPACE],
        [SPACE, SPACE, SPACE]
    ]
    while check_victory(the_board, symbols) == SPACE:
        display_board(the_board)
        position = get_user_position()
        x = position[0]
        y = position[1]
        while the_board[x][y] != SPACE:
            position = get_user_position()
            x = position[0]
            y = position[1]
        the_board[x][y] = symbols[turn % 2]
        turn += 1

current_board = [
    ['x', ' ', 'o'],
    [' ', 'x', 'o'],
    ['x', ' ', 'x']
]

print(check_rows(current_board, [TTT_X, TTT_O]))
print(check_cols(current_board, [TTT_X, TTT_O]))
tic_tac_toe_game()