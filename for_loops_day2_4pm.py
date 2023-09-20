"""
ITE 201 E (old room) moving to ITE 372 (more space hopefully)
    M->F 9-5
    
ITE 211 (my office) MW 2:30 - 4:00
"""

"""
You can create lists using the square bracket notation
"""
my_numbers = [4, 21, 77, 3941, 2]

new_list = []
# new_list = list() <-- parentheses not square brackets

if False:
    for i in range(5):
        word = input('Tell me a word: ')
        new_list.append(word)
    
    print(new_list)
    
    for i in range(5):
        my_numbers.append(int(input('Tell me a number: ')))
        print(my_numbers)
    
    even_newer_list = []
    even_newer_list.append('sandwich')
    even_newer_list.append('bacon')
    even_newer_list.append('existentialism')
    even_newer_list.append('orbit')
    print(even_newer_list)
    
    for word in even_newer_list:
        print(word)

"""
    list.remove(x)
        removes the first instance of x in the list
        x must be in the list otherwise you get a ValueError
"""
movies = ['Matrix', 'Fifth Element', 'Demolition Man', 'Matrix', 'Johnny Mnemonic', 'Finding Nemo', 'Matrix', 'Matrix']
print(movies)
movies.remove('Matrix')
print(movies)

# why didn't you just do this instead?
if False:
    for i in range(len(movies) - 1):
        if movies[i] == 'Matrix':
            movies.remove('Matrix')
            print(movies)

count = 0
for movie in movies:
    if movie == 'Matrix':
        count += 1

for i in range(count):
    movies.remove('Matrix')
    print(movies)

letter_list = ['z', 'r', 't', 'l', 'q', 'b', 'z', 'a']
if 'h' in letter_list:
    letter_list.remove('h')

"""
    range object
    
    range(stop)
    range(start, stop)
    range(start = 0, stop, step = 1)
    
        start = number [integer] where it starts
        stop = number that we go up to but not including it.
        step = how much we jump every time
"""

for i in range(4, 366, 7):
    print(i, end=' ')

print()

bad_list = ['Eric', 7, 'Sam', 4, 'Robot', 12]

names = ['Eric', 'Sam', 'Robot']
values = [7, 4, 12]

for i in range(1, len(bad_list), 2):
    print(bad_list[i])

"""
    imagine in a hiring interview they want you to reverse a list
    print it in reverse order
"""
my_happy_list = [81, 125, 64, 1729, 343, 625, 256, 1024]
print('\n\n')
for i in range(len(my_happy_list) - 1, -1, -1):
    print(my_happy_list[i])
    
for i in range(len(my_happy_list)):
    print(my_happy_list[len(my_happy_list) - 1 - i])


"""
    A word that is the same as its reverse backwards->forwards
    
    racecar
    hannah
    amanaplanacanalpanama
    tacocat
"""

palindrome = input('Tell me a palindrome or I will destroy you: ')

reversed_string = ''
for i in range(len(palindrome)):
    reversed_string += palindrome[len(palindrome) - 1 - i]

print(palindrome, reversed_string)

if palindrome == reversed_string:
    print('You are correct')
else:
    print('Prepare for destruction.')
    
"""
    for-i loops
        index valued loops (index variable is an index in a list/string)
    for-each loops
        the index variable is actually an element out of the string/list
"""
for num in [1, 5, 8, 3, 9]:
    print(num ** 2)
    
the_puppies = ['Pupper', 'Winnie', 'Cat', 'Jim', 'Max', 'Rex', 'Soju']

for puppy in the_puppies:
    if len(puppy) == 3:
        print(puppy)

# for each loop
for x in [2, 7, 1, 9, 3]:
    print(x)
    

for puppy in reversed(the_puppies):
    print(puppy)

    
"""
    index
    indices or indexes
    indice [not a thing]
"""

