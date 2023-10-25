"""
    No Class Monday
    
    Let's talk about recursion again.

    Let's do an example where we count the number of a's in a string
"""


def iter_count_as(the_string):
    count = 0
    for x in the_string:
        if x.lower() == 'a':
            count += 1
    return count


"""
    We can check to see if the first character is an "a"
        we add 1
        we look at the rest of the string counting the a's
"""


def count_as(the_string):
    print(the_string)
    if not the_string:
        return 0
    # if the first letter is an a
    if the_string[0].lower() == 'a':
        # increment the count by 1 and cut off the first letter
        return 1 + count_as(the_string[1:])
    else:
        # returns the count of the rest without adding 1
        return count_as(the_string[1:])


"""
    is an empty string a palindrome?
        Yes for our purposes
    is a single letter or character a palindrome?
        Yes. "x" => "x"
    Base case, part of the function that doesn't make any recursive calls
        we want to avoid infinite recursion, eventually we have to stop.
        
    What is a palindrome?
        Something where the first and last letters match
            and the inner part of the string is a palindrome
        a[palindrome]a
"""


def palindrome(word):
    # we know that if the string is empty or length 1, we're calling it a palindrome
    print(word)
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:  # word[len(word) - 1]
        return palindrome(word[1:-1])
    else:
        return False


"""
    we are going to output all combinations of a's and b's of a certain length
    
    n = 1
    a       b
    n = 2
    aa  ab  ba  bb
    n = 3
    aaa  aab  aba  abb
    baa  bab  bba  bbb
    n = 4
    aaaa  aaab  aaba  aabb
    abaa  abab  abba  abbb
    baaa  baab  baba  babb
    bbaa  bbab  bbba  bbbb
"""


def as_and_bs(n, current):
    if n == 0:
        print(current)
        return
    
    as_and_bs(n - 1, current + 'a')
    as_and_bs(n - 1, current + 'b')


def five_as(n, a_count, current):
    if n == 0:
        if a_count == 5:
            print(current)
        return
    
    if a_count < 5:
        # decrease the number of letters we need by 1
        # increase the a_count
        five_as(n - 1, a_count + 1, current + 'a')
    # a_count doesnt change
    five_as(n - 1, a_count, current + 'b')


crazy_list = [
    [], [[[]], [[[[]]]]], [[],[[]], [[[]]]], [[[[[[[]]]]]]]
]

depth_1 = []
depth_2 = [[], [], []]
depth_3 = [[[], [], []], [], [[]], []]
"""
    A depth n list is a list containing at least one depth n - 1 lists
    depth([]) = 1
    
    list_depth([]) => 1
    
    list_depth([[]]) = 1 + list_depth([]) = 1 + 1 = 2
    list_depth([[], [], []]) = 1 + max(list depths)
                 1  1    1
    list_depth([ [[], [], []], [], [] ]) = 1 + max(depths) = 1 + 2 = 3
                       2        1   1
"""
def list_depth(the_list):
    if not the_list:
        return 1
    
    max_depth = 0
    for x in the_list:
        current = list_depth(x)
        if current > max_depth:
            max_depth = current
    
    return 1 + max_depth

"""
s = int(input('>> '))
while s != 'quit':
    five_as(s, 0, '')
    s = int(input('>> '))
"""

print(list_depth([[[], [], []], [], [[]]]))
print(list_depth([[[[[[[[[[[[[[]]]]]]]]]]]]],[[], [], []], [], [[]]]))

"""
About the project:
    cup lists are forgiving
    but the mancala lists are not they must be exactly the right length of string
"""
BLOCK_WIDTH = 6
string = "Bob"
string = string.rjust(BLOCK_WIDTH)
print(string)