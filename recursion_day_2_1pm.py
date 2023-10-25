"""
    I'm going to be out on Monday See you Wednesday
        Bin/Hex lecture
        
    Let's get back to recursion
    
        recursion is when a function calls itself
        
        let's talk about palindromes
            think about: how can i make this problem into a smaller problem?
            
        Is an empty string a palindrome?
            yes
        Are single letter strings palindromes? "a"
            also yes
            
        Why do we need a base case?
            if we don't have one we will recurse "infintely"
            until we get a RecursionError
"""


def palindrome(word):
    # base case because no recursive calls
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:  # len(word) - 1
        print('Calling palindrome on', word[1:-1])
        return palindrome(word[1:-1])
    else:
        return False


"""
(something (something else (more (()))) whatever )
()()()(()())

(()()(())(((()))))
 ()()(())(((())))
 Check (), (), (()), (((())))
       True     ()     ((()))
                        (())
                         ()
                         True
) hi
(hi (bye)
f(x

( )) (
( ))) ((
((((((
"""


def check_parens_rec(the_string):
    if not the_string:
        return True
    
    print(the_string)
    
    start_index = -1
    count = 0
    for i in range(len(the_string)):
        if start_index == -1 and the_string[i] == "(":
            start_index = i
            count = 1
        elif start_index >= 0 and the_string[i] == "(":
            count += 1
        elif start_index >= 0 and the_string[i] == ")":
            count -= 1
            if count == 0:
                if not check_parens_rec(the_string[start_index + 1: i]):
                    return False
                start_index = -1
        elif start_index == -1 and the_string[i] == ")":
            return False
    
    return count == 0


def check_parens(the_string):
    count = 0
    for x in the_string:
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1
        # if the count is ever negative what we have is ( )) (
        if count < 0:
            return False
    # check that there were all the matches, final opens get closed
    return count == 0


def count_a_rec(a_string):
    """
        Count up the number of a's in a string
    """
    # an empty string has no a's
    if not a_string:
        return 0
    print(a_string)
    if a_string[0].lower() == 'a':
        return 1 + count_a_rec(a_string[1:])
    else:
        return count_a_rec(a_string[1:])


"""

I like these:
n = 1
a
b
n = 2 all the strings with a's and b's that you can make
aa
ab
ba
bb
n = 3
aaa
aab
aba
abb
baa
bab
bba
bbb
n = 4
aaaa
aaab
aaba
aabb
abaa
abab
abba
abbb
baaa
baab
baba
babb
bbaa
bbab
bbba
bbbb
You tell me n and i give you all the possibilities


"""


def a_and_b(n, current_string):
    print(n, current_string)
    if n == 0:
        print(current_string)
        return
    
    a_and_b(n - 1,  current_string + 'a')
    a_and_b(n - 1,  current_string + 'b')


def a_and_b_and_c(n, current_string):
    if n == 0:
        print(current_string)
        return
    
    a_and_b_and_c(n - 1, current_string + 'a')
    a_and_b_and_c(n - 1, current_string + 'b')
    a_and_b_and_c(n - 1, current_string + 'c')


n = int(input(">> "))
while n != 'quit':
    (a_and_b_and_c(n, ''))
    n = int(input(">> "))
