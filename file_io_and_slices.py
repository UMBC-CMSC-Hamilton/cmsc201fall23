"""
    Slices - a substring (a sublist) that starts at a particular index
        and ends at a second index
"""

a_string = 'mystringisgood'
print(a_string[2:8])
print(a_string[10:14])

print(a_string[7:1:-1])

my_string = input('Enter a string: ')
print(my_string[::-1])
if my_string == my_string[::-1]:
    print('it is a palindrome')
else:
    print('no')
    
    
"""
    abcabc
    012345
    
    first thing and putting it on the end
    bcabca
    123450
    
    cabcab
    234501 i + 2 mod len(string)
    take from 2 to end + (concat) string from 0 to 2
    
    abcabc (i + 3) mod len(string)
"""

for r in range(len(my_string)):
    print(r)
    for i in range(len(my_string)):
        print(my_string[i], my_string[(i + r) % len(my_string)])

"""
    This is the lab [almost]
"""

for r in range(len(my_string)):
    print(my_string[r:] + my_string[0: r])
    if my_string[r:len(my_string)] + my_string[0: r] == my_string:
        print(f'The rotation by {r} works')

"""
    Quasi Palindrome
    
    tacocat
    
    tacocpt
    "1-quasi-palindrome"
    tacocpr
    2 - QP
    abcdefg
    not a 1-quasi-pal
    3-quasi-pal
    
"""

is_pal = True
for i in range(len(my_string)//2):
    if my_string[i] != my_string[len(my_string) - 1 - i]:
        is_pal = False
        """
            how would you keep track of the matches that fail?
        """


"""
    you can slice lists
"""
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:5])
print(my_list[::2])
print(my_list[1::2])

new_list = my_list[::2]
print(new_list)
new_list[2] = 7
print(new_list)
print(my_list)

"""
    Slicing makes a copy
"""
million_list = list(range(1000000))
# print(million_list)

# bad
"""
big_thing = []
for i in range(len(million_list)):
    big_thing.append(million_list[i:])
"""

"""
    File IO - read and write to files
        open files
        read from them
            read()
            readlines() - list of strings
            readline() - a single line
            [read functions all return the newline characters]
        write to them
            write
            writelines
        close them
"""

new_file = open("file_io.txt", 'r')
print(new_file)
# calls the read method, reads the entire file, returns a string
contents = new_file.read()
print(contents)
new_file.close()

# mode is automatically read if you don't include it
read_again = open('file_io.txt')
# readlines will split by the new line but does NOT remove newlines
for string in read_again.readlines():
    print(string.strip())
read_again.close()


# be careful here
read_once_again = open('file_io.txt')

s = read_once_again.readline()
while s:
    print(s)
    s = read_once_again.readline()

read_once_again.close()

"""
    Write mode opens and empties a file "blank, zeros out"
"""
def write_file():
    new_file = open('new_file.txt', 'w')
    s = input('>> ')
    while s != 'quit':
        new_file.write(s + "\n")
        s = input('>> ')
    
    new_file.close()

    
    new_file = open('new_file.txt', 'w')
    s = input('>> ')
    file_lines = []
    while s != 'quit':
        file_lines.append(s + "\n")
        s = input('>> ')
    new_file.writelines(file_lines)
    
    new_file.close()


"""
    if you need to write new things to a file, then use 'a' mode
        for append
"""
my_file = open('new_file.txt', 'a')
s = input('>> ')
file_lines = []
while s != 'quit':
    file_lines.append(s + "\n")
    s = input('>> ')
my_file.writelines(file_lines)

my_file.close()

my_file = open('new_file.txt')
print(my_file.readlines())
print('go again: ')
my_file.seek(0)
print(my_file.readlines())
