"""
    Slices are substrings or sublists using the array brackets
        except that we can use [start:end:step]

"""
import string
import random

def slice_time():
    my_string = 'hello'
    print(my_string[2:5], my_string[5:2:-1])
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list[4:7], my_list[4:200])
    # slices make copies
    my_slice = my_list[4:7]
    print(my_slice)
    my_slice[2] = 51
    print(my_slice)
    print(my_list)
    
    # this is not 201 stuff
    def big_stuff():
        big_list = [random.choice(string.ascii_letters) for _ in range(1000000)]
        big_string = ''.join(big_list)
        print(big_string)
        many_copies = []
        for i in range(len(big_string)):
            many_copies.append(big_string[i:])
        print('Done')
    
    
    print(my_list[0:len(my_list):2])
    print(my_list[1:len(my_list):2])
    
    new_list = list(my_list)
    new_list = my_list[:]
    
    the_word = input('Tell me a word: ')
    
    print(the_word[7:3:-1])
    
    if the_word == the_word[::-1]:
        print('yes')
    else:
        print('no')
    
    """
    k-Quasi-palindromes
    
    palindrome where we allow up to k mistakes
    
    tacocap -> pacocap or tacocat
    racecar -> renecar you can fix renener or racecar rececer
    anything is a k-Qp for sufficiently large k
    
    abcdefghijklm is a 100-QP
    """
    def quasipalindrome(word, k):
        """
            think about counting the number of errors
            i = 3
            L = 7
            7 - 1 - 3 = 3
            racecar
        """
        for i in range(len(word) //2):
            if word[i] != word[len(word) - 1 - i]:
                return False
        
    return True

"""
    File IO - the thing that definitely exists
    
    open
        How do you open a file?
            use the open function
    read
        read() - reads the entire file
        readline() - reads a single line until the next \n
        readlines() - reads all the lines gives you a list of lines
    write
    close
"""

my_file = open('rando_file.txt')

# read method reads an entire file returns a single string
file_contents = my_file.read()
print(file_contents)
my_file.close()

my_file = open('rando_file.txt', 'r')
print(my_file.readline())
print(my_file.readline())
my_file.close()

my_file = open('rando_file.txt', 'r')
print(my_file.readlines())
# the cursor is at the end of the file
# the next read will be empty
print(my_file.readlines())
my_file.close()

my_file = open('rando_file.txt', 'r')
i = 0
for line in my_file:
    print(f'the {i}th line is {line.strip()}')
    i += 1
my_file.close()


"""
    File writing:
        .write(a string)
        .writelines(list of strings)
    
    neither method even writelines unfortunately doesn't include newline
"""
def write_stuff():
    # write mode blanks the file out
    #
    nf = open('new_file.txt', 'w')
    s = input(">> ")
    while s != 'quit':
        nf.write(s + '\n')
        s = input('>> ')
        
    # why do we need to close files?
    # in general for read mode we don't
    # in write mode we definitely do
    nf.close()


nf = open('new_file.txt', 'a')
s = input(">> ")
while s != 'quit':
    nf.write(s + '\n')
    s = input('>> ')
nf.close()

with open('new_file.txt', 'a') as my_new_file:
    s = input(">> ")
    while s != 'quit':
        my_new_file.write(s + '\n')
        s = input('>> ')
