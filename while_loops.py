"""
    more loops
"""

"""
    when you run a python file, whatever file it is, it sets:
    __name__ == '__main__'
"""

print(__name__)

"""
    the same as any other function, doesn't get called automatically
"""


# this does
if __name__ == '__main__':
    print('hi')
    print('put everything inside here')
    

"""
    not allowed to have a function called main()
    
def main():
    print('we are in the main function')
"""

"""
    what is a while loop?
    
        a while loop is a loop that instead of iterating through
            a list or range, it keeps repeating while a condition is true
            
        a while is a an if statement on repeat
"""

# missed loop if the while never executes
x = -4
while x > 0:
    x = int(input('Tell me a number: '))


# infinite loop as long as it works the first time
x = int(input('Tell me a number: '))
while x > 0:
    x += 1
    print(x)


# update the variables in the condition before the loop checks again
x = int(input('Tell me a number: '))
while x > 0:
    print(x)
    x = int(input('Tell me a number: '))
    

"""
    User input validation
"""
my_num = int(input('Enter a number between 1 and 10: '))
while not(1 <= my_num <= 10):
    my_num = int(input('Enter a number between 1 and 10: '))


password = 'let me in'

user_password = input('Enter password: ')
chances = 5
while user_password != password and chances > 1:
    chances -= 1
    print(f'That was not correct, try again... you have {chances} chances left')
    user_password = input('Enter password: ')
    
if user_password == password:
    print('You have gained access')
else:
    print('You are being disconnected')


"""
    anything that you code as a for loop can also be coded as a while loop
"""

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(my_list)):
    print(my_list[i], end=" ")

print()

index = 0
while index < len(my_list):
    print(my_list[index], end=" ")
    index += 1

"""
    for-each loop
        x is an element not an index
"""
for x in my_list:
    print(x)


n = int(input('Tell me another number: '))
double = 1
count = 0
while double < n:
    double *= 2
    count += 1
    print(double)

# if you don't know how many times the loop is going to run
# you need a while loop

print(f"it took {count} number of times to get to {n}")


"""
    while loops that exist outside of this class
    
        GUI programs
        web services
        games most of the time
"""

a_list = []

command = input('>> ')
while command != 'quit':
    if command == 'print':
        print(a_list)
    elif command == 'append':
        add_element = input('What do you want to add to the list? ')
        a_list.append(add_element)
    elif command == 'remove':
        rem_element = input('What do you want to remove from the list? ')
        if rem_element in a_list:
            a_list.remove(rem_element)
        else:
            print(f'You tried to remove {rem_element} but that was not in the list.')
    command = input('>> ')


marquee = input('Tell me a sentence: ')
# let's find out if there are any a's which have two letters in between
# sandal
# 012345 so we want to check i vs i + 3
# robat[xa]

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

marquee = marquee.lower()
for i in range(len(marquee) - 3):
    print(marquee[i], marquee[i + 3])
    if marquee[i] == 'a' and marquee[i + 3] == 'a':
        print(f'We have a match at position {i}')

