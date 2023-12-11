"""

Write an expression which returns True if and only if 'pupper'
is in the list of dogs, and 'minion' is an element of the cats list.
"""
dogs = cats = []
# this is what you need:
'pupper' in dogs and 'minion' in cats

"""
Write an expression that returns True if and only if a
string test_string contains only uppercase or lowercase letters.
"""
test_string = ''
# this is what you need:
test_string == test_string.upper() or test_string == test_string.lower()

"""
Write an expression that returns True if and only if birds is an
empty list and either password (a string) is "password1" or "asdf1234".
"""
birds = []
password = 'asdf1234'
not birds and (password == "password1" or password == 'asdf1234')
# len(birds) == 0 or birds == []

"""
planets = {"Mercury": 0.24, "Venus": 0.615, "Earth": 1, "Mars": 1.881}

print( planets["Venus"] )

answer:
    0.615

print( planets["Earth"] + planets["Mars"] )

1 + 1.881 = 2.881
answer:
    2.881

print( planets.get("Jupiter", 0))

answer:
    0


planets["Jupiter"] = 11.862
print(planets)

{"Mercury": 0.24, "Venus": 0.615, "Earth": 1,
            "Mars": 1.881, "Jupiter": 11.862}

print(planets["Neptune"])

answer:
    KeyError


Convert the decimal number 15
    15 odd => 7 odd => 3 odd => 1 odd
    1111
 	to binary: 		0b1111
 	to hexadecimal:	0xF


Convert the decimal number 241
 	to binary: 	0b 1111 0001
 	to hexadecimal:	0xF1

    241 odd => 120 even => 60 even => 30 even => 15 (i know this one)
        1111 0001
    <----
Convert the binary number 0011 1101
 	to decimal:     13 + 16 + 32 = 61
 	to hexadecimal:	3d
 	                3 * 16 + 13


Convert the binary number 1010 1111
	to decimal: 	 10 * 16 + 15 = 1 + 2 + 4 + 8 + 32 + 128 = 175
 	to hexadecimal:	 AF

bin     hex
0000    0       0100    4   1000    8   1100    C
0001    1       0101    5   1001    9   1101    D
0010    2       0110    6   1010    A   1110    E
0011    3       0111    7   1011    B   1111    F

Convert the hexadecimal number 40DE59FA
 	to binary: 0100 0000 1101 1110 0101 1001 1111 1010
(Make sure to leave space between each group of four!)
"""

print("Have\\a\ngreat\\\n\tSummer\\")
"""
Have\a
great\
    Summer\
"""
print('\\\\\\\\\\')

"""
    Answer: 15
    Reason: ints are immutable pass by value, not modified
    
    Other version of the question replaces
        count +=1 with count.append(1)
        and count = 15 with count = []
"""


def increment_count(count):
    count += 1


if __name__ == "__main__":
    count = 15
    increment_count(count)
    increment_count(count)
    print(count)

a_var = 'hello'
b_var = 4
if a_var or b_var == 'hello':  # a_var is true, so the or executes
    print('think about order of operations')  # this happens
else:
    print('b_var is hello right?')


def count_down(n):
    """
        count_down(5) = 5 + count_down(4) ==> prints 5
        count_down(4) = 4 + count_down(3) ==> prints 4
        count_down(3) = 3 + count_down(2) ==> prints 3
        count_down(2) = 2 + count_down(1) ==> prints 2
        count_down(1) = 1 + count_down(0) ==> prints 1
        count_down(0) = 0 ==> prints Surprise!
    """
    if n == 0:
        print('Surprise!')
        return 0
    else:
        print(n)
        return n + count_down(n - 1)


# if there's a print statement, then 15 gets printed (should have had that on the exam)
count_down(5)

the_matrix = [[4, 3, 9], [7, 2, 8], [1, 5, 10]]
print(the_matrix[1][1])  # 2
print(the_matrix[0][2])  # 9
print(the_matrix[2][1])  # 5

print('\n\n')

my_int = 32
while my_int:
   print(my_int)
   my_int //= 5

print('\n\n')
the_string = 'abcabcabc'
for i in range(len(the_string)):
   if the_string[i: i + 3] == 'abc':
       print(i)

# invalid slices produce empty strings
my_string = 'asdfasfdasfdasdf'
print(my_string[7:4], 'did i print?')


a_list = []
for i in range(2, 15, 3):
   a_list.append(i)

print(a_list)
print(list(range(2, 15, 3)))


"""

def find_matches(my_grid):
   #  my_grid is a 2-d list, this function should print any
   #     symbol which is found more than once in the grid
   elements = {}
   for i in range(my_grid): # range(len(my_grid))
       for j in range(len(my_grid)): # range(len(my_grid[i]))
           the_element = my_grid[i] # need to add my_grid[i][j]
           if the_element in elements # need the colon:
               the_element += 1  # elements[the_element] += 1
           elif: # else:
               elements[the_element] = 1 # this is right... wow
   for elem in elements:
       if elem >= 1: # elements[elem] > 1
           print elem, 'has matches' # add parentheses

if __name__ == __main__:
   find_matches([['a', 'a', 'b'], ['c', 'a', 'b'], ['d', 'x', 'g']])



Write a function called a_distance which takes a string message
 and calculates the minimum "distance" between two a's.

a_distance("abba") will return 3 since that is the
        difference in positions.
a_distance("abbbbbabbbabbbbbbabbbaba") will return 2
        because the last a's are only two apart.
a_distance("abcdbazzzza") will return 5 since the
        a's are 5 characters apart.
"""

def a_distance(message):
    prev_index = -1
    min_distance = len(message) + 1
    for i in range(len(message)):
        if message[i] == 'a':
            if prev_index == -1:
                prev_index = i
            else:
                if i - prev_index < min_distance:
                    min_distance = i - prev_index
                prev_index = i
    
    return min_distance


def a_distance_two(message):
    prev_index = -1
    min_distance = len(message) + 1
    for i in range(len(message)):
        if message[i] == 'a' and prev_index == -1:
            prev_index = i
        elif message[i] == 'a' and i - prev_index < min_distance:
            min_distance = i - prev_index
            prev_index = i
        elif message[i] == 'a':
            prev_index = i
    
    return min_distance


def a_distance_three(message):
    indices = []
    for i in range(len(message)):
        if message[i] == 'a':
            indices.append(i)
    
    min_dist = len(message) + 1
    for j in range(len(indices) - 1):
        if indices[j + 1] - indices[j] < min_dist:
            min_dist = indices[j + 1] - indices[j]
            
    return min_dist


"""
Assume that the_list is a one dimensional list.
Write a function called force_sort which will take a
list and return a new list with only the elements that
were in sorted order.  For example if we would "force sort"
[1, 2, 8, 4, 5] then we would get [1, 2, 8] since those are
 in order.  If we force sorted [1, 2, 3, 8, 4, 5, 10, 12] we
  would get [1, 2, 3, 4, 8, 10, 12] because they are also in order.
  You don't have to try to make the longest sorted list,
  just produce a sorted list starting with the first element in the
  list passed as an argument.

	force_sort([5, 4, 3, 2, 1]) returns [5]
	force_sort([1, 2, 4, 3, 6, 5, 10, 9]) returns [1, 2, 4, 6, 10]

"""

def force_sort(a_list):
    if not a_list:
        return []
    the_new_list = [a_list[0]]
    current = a_list[0]
    for i in range(1, len(a_list)):
        if a_list[i] >= current:
            the_new_list.append(a_list[i])
            current = a_list[i]
    
    return the_new_list
    