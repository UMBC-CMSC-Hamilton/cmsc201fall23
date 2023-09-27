"""
This is the doc string
"""
import other_file
if False:
    if __name__ == '__main__':
        print('hello there', __name__)
        
    # is there a main FUNCTION/method in python?
    # i will probably ban the use of def main()
    
    """
        While Loops
        
            What is a while loop?
            
                a while loop is a loop that uses a condition, and it continues
                to repeat as long as that condition is true
            
            While loop = if statement with the repeat button on
            
    """
    
    x = 5
    while x > 0:
        x = int(input('Tell me x: '))
    
    
    print('The loop is about to begin, please take your seats')
    # skipped loops, missed loops
    x = -2
    while x > 0:
        x = int(input('Tell me x: '))
    
    print('The loop has ended')
    
    if False:
        # infinite loop = if the condition is always true
        # then the loop never terminates
        x = int(input('Tell me x: '))
        while x > 0:
            if x % 1000000 == 0:
                print(x)
            x += 1
    
    """
        What is the primary application in this class of for loops?
            User input validation
    """
    
    a_number = int(input('Tell me a number between 1 and 10: '))
    while not(1 <= a_number <= 10):
        print('You are admonished! ')
        a_number = int(input('Tell me a number between 1 and 10: '))
    
    
    my_password = 'password1234'
    
    user_password = input("What is the password? ")
    count = 5
    while user_password != my_password and count > 1:
        print('That was incorrect, you are an evil deceiver')
        count -= 1
        print(f'You have {count} attempts left')
        user_password = input("What is the password? ")
    
    
    """
        any for loop can be rewritten into a while loop
    """
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for i in range(len(my_list)):
        if my_list[i] in vowels:
            print(my_list[i], 'is a vowel')
    
    index = 0
    while index < len(my_list):
        if my_list[index] in vowels:
            print(my_list[index], 'is a vowel')
        index += 1
        
"""
    not any while loop can be made into a for loop
"""


# how many times does this loop run?
num = int(input('Tell me a number: '))

fact = 1
count = 1
while fact < num:
    count += 1
    fact *= count
    print(count, fact)

print(f'The first factorial larger is {count}! = {fact}')
"""
    If you don't know how many times a particular loop will run
        then it's probably a while loop
"""

"""
    Other uses of while loops:
        (1) GUI [= graphical user interface] programs
        (2) Server applications
        (3) Games for ex chess: while not checkmate():
"""

my_string = 'abcdef'
print(list(my_string))

list_of_string_nums = ['1', '2', '3']
for i in range(len(list_of_string_nums)):
    list_of_string_nums[i] = int(list_of_string_nums[i])
    

"""
    Aside: HW hints
"""

num = int(input('Tell me the size: '))
for i in range(num):
    for j in range(num):
        print(f'({i}, {j})', end=" ")
    print()


word = input('Tell me a word: ')
# we are going to find a's with 2 letters in between
# ama[nd]a sa[nd]al
# 012 34 5 01 23 45

for i in range(len(word) - 3):
    if word[i] == word[i + 3] == 'a':
        print('Found match at position', i)




