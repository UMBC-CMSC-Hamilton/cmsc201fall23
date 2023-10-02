"""
    Functions and Mutability

    Midterm 1 is next week
        TF MCQ
"""

"""
    What is a function?
        a function is a block of code that we can "call"
        anywhere in the code we can jump to the function, execute it
        and then we return to the place that called it.
        
    Parameters - inputs to the function
        Arguments are the actual values that we plug in to the parameters
            of the function
    Return - give a value back to the code that called the function
    
    Two purposes:
        1) abstraction - the function lives apart from the other piece of
            code, takes input from it and gives output, but it gives us
            a way to test individual pieces of functionality
        2) to prevent our code from ending up a giant ball of spaghetti
            prevents a lot of repeated code
"""


# def is a keyword that says "there will be a function"
# the name of the function is first_function
# what is x? x is a parameter
def first_function(x):
    print(x ** 2)


"""
What is a palindrome?
    a palindrome is a word that is spelled the same forwards and backwards

    racecar
    tacocat
    amanaplanacanalpanama
    
    what does your function need to work?
    whatever your function needs that needs to be the parameter list
"""


#                   the_word is a 'renaming' of my_word
def is_palindrome(the_word):
    for i in range(len(the_word) // 2):
        if the_word[i] != the_word[len(the_word) - 1 - i]:
            return False
    
    return True


def get_max(a_list):
    current = 0
    if a_list:  # non-empty means true
        current = a_list[0]  # a_list[0]
    else:
        return None
        
    for x in a_list:
        if current < x:  # a_list[i]
            current = x
    
    return current


def increment_x(x):
    x += 1
    print(x)
    return x


def construct_list(new_list):
    command = input('>> ')
    while command != 'quit':
        new_list.append(command)
        command = input('>> ')


def my_function(x, y, z):
    print(x * y * z)


def my_sum_function(a_list):
    the_sum = 0
    for x in a_list:
        the_sum += x
    # what does this do?  this a_list = [] will create a new list
    # new list will be empty and a_list will now point to it
    a_list = []
    print(a_list)
    return the_sum

if __name__ == '__main__':
    first_function(5)
    first_function(7)
    first_function(17)
    my_word = input('Tell me a word to check: ')
    print(is_palindrome(my_word))
    another_word = input('Tell me a word to check: ')
    print(is_palindrome(another_word))
    
    # input is a function and what does it return?
    # input does some magic which gets user input, returns a string to us
    input('This is an argument: ')
    # without setting the input into a variable the result of the function
    # is lost, remember that it is the same for all functions
    
    # you must set returns into variables
    print(get_max([1, 2, 3, 6, 5, 9, 2, 3, 3, 2, 1, 3, 5, 3, 2, 1]))
    print(get_max([13, 21, -5, -17, 34, 89]))
    print(get_max([-1, -2, -3, -4, -5]))
    print(get_max([]))
    
    the_x = 5
    increment_x(the_x)
    """
        some variables can be modified inside of functions and others
            can't
        if it's a primitive data type, int, bool, string, float
            then it can't.
            if these are passed we make copies and it's called
            "pass by value"
            
        the function makes a copy of the variable and uses the copy
            doesn't use the original value
            
        we can modify lists, dictionaries, classes
            "pass by reference" = the variable is not copied
                it's actually the same variable but just renamed
    """
    print(the_x)
    # this will modify the_x
    the_x = increment_x(the_x)
    print(the_x)

    # any function that doesn't return something "secretly" returns None
    value = my_function(3, 4, 5)
    print(value)
    #
    my_list = []
    construct_list(my_list)
    print(my_list)
    
    random_list = [2, 4, 6, 8, 10]
    random_list[3] = 157
    print(random_list)
    
    happy_birthday = "happy birthday to you"
    #happy_birthday[3] = 'c'  # strings are immutable cannot be changed
    # print(happy_birthday)
    my_letters = list(happy_birthday)
    print(my_letters)
    my_letters[3] = 'c'
    print(my_letters)
    
    # in order to convert a list back into a string use the join function
    print(''.join(my_letters))
    #     empty string is called the separator, string that will be put between the letters
    #             my_letters is a list of strings

    # strings are primitive data types and they pass by value
    # therefore in python they are also immutable
    # so are integers, floats, and bools (all immutable)
    
    # lists dictionaries and classes are mutable
    
    the_1001_list = list('1001')
    print(the_1001_list)

    s = 'HAPPY BIRTHDAY'
    s = s.lower()
    print(s)
    
    # don't do this:
    """
    x = int(input('tell me a number'))
    if x == 3:
        def robot_function():
            print('robot')
            
    robot_function()
    """
    
    out_list = [1, 2, 3, 5, 8, 13, 21, 34, 89]
    the_sum = my_sum_function(out_list)
    print(the_sum, out_list)

