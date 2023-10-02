"""
    functions, mutability
    
    Midterm:
        Next week - Wednesday
        MCQ, short answer questions, what does the code do?
            write a bit of code, 15 lines max [on paper]
        Practice test released sometime in the next few days
        On monday i'll cover the answers, explanations etc
        
        No labs next week
"""

"""
    strip, split and join [3 string functions]
    
    strip removes whitespace from the beginning and end of a string
        
        white space are spaces " " or \n \t \r
"""


def strip_split_join():
    proceed = input('Do you want to proceed? ')
    proceed = proceed.strip()
    if proceed == 'yes' or proceed == 'go':
        print('You have elected to launch.')
    else:
        print('nope')
    
    color = input('What is your favorite color? ').strip()
    if color == 'red':
        print('Red is the color of war')
    elif color == 'blue':
        print('blue is like the ocean')
    elif color == 'green':
        print('trees')
    elif color == 'yellow':
        print('sun')
    elif color == 'pink':
        print('barbies')
    else:
        print('that is not a color')
    
    my_string = "\t\t\n\n\n\n   once upon a time there was a little lamb\n\n\n\t"
    print(my_string)
    print('hi')
    print(my_string.strip())
    
    """
        split = splits a string on whitespace
    """
    sentence = input('Tell me a story: ')
    print(sentence)
    print(sentence.split())
    
    animals = "cat, dog, chicken, turkey, salmon, cow, sheep, goat,robot"
    split_animals = animals.split(",")
    print(split_animals)
    for i in range(len(split_animals)):
        split_animals[i] = split_animals[i].strip()
    
    condiments = ['ketchup', 'mustard', 'onions', 'horseraddish', 'mayonaise', 'bacon', 'mushrooms']
    """
        Whereas split converts a string into a list
        
        join converts a list back into a string
            it needs a separator
            separator.join(a_list_of_strings)
            it may seem a little backwards
    """
    cond_string = ', '.join(condiments)
    print(cond_string)
    
    print("::robots are cool::".join(condiments))


"""
    What is a function?
        it's a block of code
        we can call it by a particular name
        jump to the function, execute the block of code
        leave the function and go back to wherever we called from.
        
"""


# def is a keyword that stands for define
# the name of the function is my_first_function
# x is a parameter (variable that is defined inside of the function
# so that we get data into the function)
def my_first_function(x):
    print(x ** 2)


my_first_function(5)
my_first_function(121)
my_first_function(7701)
num = int(input('Tell me a number: '))
my_first_function(num)
# using variables that only exist inside of functions won't work
# print(x)


def is_palindrome(a_word):
    for i in range(len(a_word)):
        if a_word[i] != a_word[len(a_word) - 1 - i]:
            return False
    return True


word = input('Tell me a word to check: ')
while word != 'stop':
    print(is_palindrome(word))
    word = input('Tell me a word to check: ')

"""
    Two main purposes for functions:
    1) abstraction - allows you to deal with specific bits of functionality
        by themselves, not combine code into a gigantic spaghetti style
        block with all functionality merged
    2) avoid repetition - shortens our code dramatically
        allows us to make sure that a particular thing works
        don't end up with both working and non-working copies of the
        same bit.
"""

def vol_of_sphere(radius):
    return (4/3) * 3.141526535 * radius ** 3


print(vol_of_sphere(3))
print(vol_of_sphere(5.2))
print(vol_of_sphere(131.76))

def get_max(a_list):
    if not a_list:
        return None

    current = a_list[0]
    for x in a_list:
        if x > current:
            current = x
    return current


my_list = []
element = int(input('Tell me a number: '))
while element != 42:
    my_list.append(element)
    element = int(input('Tell me a number: '))

print(get_max(my_list))


def replace(a_string, letter, replace_with):
    list_string = list(a_string)
    print(list_string)
    for i in range(len(a_string)):
        if a_string[i] == letter:
            list_string[i] = replace_with
    
    return ''.join(list_string)

print(replace('hello', 'l', 'z'))


def increment_me(x):
    x += 1
    print(x)
    
variable = 7
increment_me(variable)
print(variable)

def append_to_list(the_list, n):
    the_list.append(n)
    print(the_list)
    
the_fancy_list = [1, 2, 3, 4, 5]

append_to_list(the_fancy_list, 17)
print(the_fancy_list)