"""
    ITE 372 <-- TA office hours
    ITE 211 <-- Eric
"""

"""
for loops and lists
"""
if False:
    # for-each loop because "word" are elements of this list
    word_list = ['happy', 'clam', 'bond', 'calzone', 'shrimp']
    for word in word_list:
        print(word)
        word = 'apple'
    
    print(word_list)
    
    # i is an element of the list so this is a for-each loop
    my_numbers = [1, 2, 3, 4, 5]
    for i in my_numbers:
        i **= 2  # i = i squared
        print(i)
        # you can modify the elements of a for-each loop and it doesn't
        # change the underlying list
    
    print(my_numbers)
    
    # for-i loop (uses indices rather than elements)
    # for-each loop (uses elements)
    
    my_numbers = [7, 2, 31, 58, 91]
    
    #  what makes this a for i loop?
    #               --> this does <--
    for index in range(len(my_numbers)):
        print(index, my_numbers[index])
        my_numbers[index] **= 2
    
    print(my_numbers)
    
    """
        Remember you're looking for a range(len(...)) because that gives
            indices, the variable name doesn't actually matter.
    
    What is n!  ?
    
        n! = n * (n - 1) * (n - 2) * (n - 3) * ... * 3 * 2 * 1
        0! = 1
        
        5! = 5 * 4 * 3 * 2 * 1 = 120
        4! = 4 * 3 * 2 * 1 = 24
        3! = 3 * 2 * 1 = 6
        2! = 2 * 1 = 2
        1! = 1
    """
    
    n = int(input('What factorial do you want? '))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        # fact = fact * i
    
    print(fact)
    
    """
    Let's say we want to calculate all the factorials between 1 and 100
    
        first example of nesting loops
        
            we have code that calculates factorial
            we want to repeat that calculation 100x
    """
    
    for n in range(1, 101):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)
    
    """
    Fibonacci Numbers:
        Rule: add the two previous numbers in the "list"
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
        0  1  2  3  4  5  6  7   8    9  10  11   12
    """
    
    one_prev = 1
    two_prev = 0
    current = 0
    
    which_fib = int(input('Which fibonacci number do you want to calculate?'))
    for i in range(which_fib - 1):
        current = one_prev + two_prev
        two_prev = one_prev
        one_prev = current
    
    print(current)

"""
    Let's talk about reversing a list (reversing its output)
"""
#           0    1    2    3    4    5    6    7    8
my_list = ['a', 'q', 'z', 'r', 't', 'l', 'p', 'z', 'x']

for i in range(len(my_list)):
    # trick, what is 8 - i?
    print(my_list[8 - i])


# range(start, stop, step)
# start where you start
# stop is where you go "up/down to but not including"
# step is the size of the jump each time

for x in range(2, 18, 3):
    print(x, end=' ')

print()


for x in range(2, 100, 7):
    print(x, end=' ')

print()

# invalid range, so it won't happen
for x in range(0, 10, -1):
    print(x, end=' ')

print()


for x in range(len(my_list) - 1, -1, -1):
    print(my_list[x], end=' ')

print()

"""
    You can add and remove elements from a list:
    to add an element you use the append method
"""

new_list = ["Money", "Robots", "Money"]
new_list.append("Money")
new_list.append("Happiness")
new_list.append("Sadness")
new_list.append("Anxiety")
new_list.append("Money")

print(new_list)
new_list.remove('Anxiety')
print(new_list)

if 'Serendipity' in new_list:
    new_list.remove('Serendipity')
print(new_list)
new_list.remove("Money")
print(new_list)

new_list.remove("Money")
print(new_list)

new_list.remove("Money")
print(new_list)

new_list.remove("Money")
print(new_list)

number_list = []
for i in range(5):
    new_num = int(input('Tell me a number: '))
    number_list.append(new_num)
    
print(number_list)

my_word = input('Tell me a word: ')
count = 0
for i in range(len(my_word)):
    if my_word[i].lower() == 'a':
        count += 1

print(f'There were {count} a\'s')

my_list = ['a', 'b', 'c']
for letter in my_list:
    print(letter)
    letter = input('tell me a letter')
print(my_list)
    
for i in range(len(my_list)):
    print(my_list[i])
    my_list[i] = input('tell me a letter')
print(my_list)