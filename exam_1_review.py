"""
# 4 on the practice test:
"""

numbers = [1, 2, 7, 4, 2, 14]
for number in numbers:
    number += 2
print(numbers)

for i in range(len(numbers)):
    numbers[i] += 2

print(numbers)

for x in range(17, 3, 5):
    print(x)

a_list = [2, 3, 1, 7, 3, 5, 1, 2, 6, 3, 9, 3]
while 3 in a_list:
    a_list.remove(3)
print(a_list)

print(27 in range(36))

print(range(36))
print(list(range(36)))

the_list = [1, 2, 4, 5, 6]
for x in range(len(the_list)):
    the_list[x] *= 2
    print(the_list[x], end=" ")
print(the_list)


"""

An expression that evaluates to True if and only if the variable
 has_coat is True and either the variable prob_rain
is greater than 50% (0.5) or prob_snow is greater than 25%.

Do not need the if statement just need the expression inside
"""
has_coat = True
prob_rain = 0.4
prob_snow = 0.2
# this is the answer you don't need the if or to define the variables
has_coat and (prob_rain > 0.5 or prob_snow > 0.25)

"""
An expression that evaluates to True if and only if all three
of the conditions here are met: the num_cats is greater than zero,
the num_dogs is less than 20, and the cat_name string is not empty.
"""
num_cats = 3
num_dogs = 1
cat_name = 'Minion'

num_cats > 0 and num_dogs < 20 and cat_name  # cat_name != ''



def infinite_loops():
    # while loops can be infinite
    x = 3
    while x > 0:
        x += 1
        
    while True:
        pass
    
    while "string" == 'string':
        print('hi')

"""
Because of operator precedence, x < y and 4 tests x < y and then tests
4, which is true.  The X < doesn't distribute over the and.

Unlike x < y and x < 4 which tests if x < both y and 4.
"""

"""

+, == , and, not, *, %

First
*, %
+
==
not
and
Last

not X and Y == (not X) and Y
not (X and Y) [not what it does]
"""

list_of_nums = [4, 6, 2, 9, 3, 5, 25]

for x in list_of_nums:
    for y in list_of_nums:
        if x == y:
            print(x, 'is', y)
        elif x % y == 0:
            print(y, 'divides', x, 'evenly')

"""
Write a program that asks the user to enter integers in ascending order.  When they enter a number that is
less than the previous number, stop and print the list.
"""
nl = []
n = int(input('Num: '))
nl.append(n)
n = int(input('Num: '))

while n > nl[len(nl) - 1]:
    nl.append(n)
    n = int(input('Num: '))

print(nl)

"""
 Input an integer n, and determine if it's perfect.
  If it is, print that n is perfect, otherwise print that it isn't.
"""

n = int(input('Tell me a number to check for perfection: '))
s = 0  # the sum of the proper divisors

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print('perfect')
else:
    print('no')