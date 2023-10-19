
def number_two_problem():
    if __name__ == '__main__':
        string_list = []
        s = input("Enter a string: ")
        while s != "stop":
            string_list.append(s.lower())
            s = input("Enter a string: ")
        # begin your code here
        
        max_count = -1
        max_string = ''
        for s in string_list:
            count = 0
            for the_chr in s:
                if the_chr.lower() == 'a':
                    count += 1
            if max_count < count:
                max_count = count
                max_string = s
                
        print(max_string, max_count)


"""
    Dictionaries in python
    
    if you think about a list then you have indices which you use
        to retrieve/insert elements
        indices are between 0 ... length(list) - 1
        
    Instead of index-> value
    
    Think about it as key -> value
        key can be any immutable variable type:
            string, int, float, bool,
                future thinking: datetime
    Syntax:
        my_dictionary = {key: value, other_key: other_value, a_key: a_value}
"""

my_numbers = {'happy': 15, 'sad': 12, 'shrimp': 3, 'toast': 21,
              'fish taco': 33, 15: 1905, 15: 2011}
# no duplicate keys
print(my_numbers)
print(my_numbers['sad'], my_numbers['toast'])
# accesssing a value results in a key error
print(my_numbers[15])
# if it isn't a key then it will result in a KeyError which is like
# an IndexError
# print(my_numbers['turtle'])

"""
    Applications of dictionaries
    
    {student_id: student_name}
"""

students = {'eric8': 'Eric', 'robert5': 'Robert',
            'sh3487348': 'Shannon', 'sh293892': 'Shannon'}

"""
    keys must be immutable BUT the values don't have to be
    values can be ... lists, or dictionaries
"""

users = {'eric8': ['abcd1234', 52.31, 'eric@oursite.com'],
         'robert7': ['password1', 123.55, 'robert@umbc.edu'],
         'joseph1': ['pw2',2378.2,'j@umbc'],
         'joseph2': ['pw3',225.1,'j2@oursite'],
         'mark': ['markymark',33.1,'markymark@markwahlberg.wahlberg']
         }

PASSWORD = 0
MONEY = 1
EMAIL = 2

print(users['mark'][EMAIL])
print(users['joseph1'][MONEY])
print(users['eric8'][PASSWORD])


doors = {
    1: 'The End',
    2: 'Anyway',
    3: 'There is a goat here'
}

# can do this but don't
weird = {
    True: 'hi',
    1: 'what on earth?',
    3: 'robot',
    'happy': 'chicken'
}

print(weird)

"""
    for each loops work with dictionaries (you will use this construction)
    but it only outputs the keys not the values
"""
for x in users:
    print(x, users[x])
    
def change_password():
    username = input('What is the username? ')
    while username not in users:
        username = input('What is the username? ')
    
    new_password = input('What is the new password? ')
    users[username][PASSWORD] = new_password
    print(users)
    
    """
        How to add a key to a dictionary:
            assign the key for the first time
    """
    users['theresa4'] = ['werewolves', 62.00, 't4@t4.net']
    print(users)
    
    del users['mark']
    print(users)

def fish_fun():
    fish_map = {
        'tuna': 3,
        'salmon': 14,
        'escolar': 33,
        'mahi-mahi': 5,
        'catfish': 42
    }
    
    del_list = []
    
    for fish in fish_map:
        print(fish, fish_map[fish])
        y_n = input('Would you like to remove that fish? ')
        if y_n.lower() in ['y', 'yes']:
            del_list.append(fish)
    
    for fish in del_list:
        del fish_map[fish]
    print(fish_map)
    
    new_fish = ['clownfish', 'trout', 'shrimp']
    for fish in new_fish:
        fish_map[fish] = 15
    print(fish_map)


new_user = {
    'eric8': {'Name': 'Eric', 'Email': 'eric8@umbc.edu'},
    'samantha3': {'Name': 'Samantha', 'Email': 's234@umbc.edu'}
}

print(new_user['samantha3']['Email'])

awful = {
    'a': 3,
    'A': 4
}
print(awful)

"""
    del keyword
"""
"""
x = 3
print(x)
# have i ever had to do this in "professional code?" = no
del x
print(x)
"""
"""
Here's another feature you don't need right now:
def function1(x):
    def function2(x,y):
        return 2 * x + y
    
    return function2(x, 5)

print(function2(3, 2))
"""

"""
    Last thing I'll say about dictionaries:
        word dictionary is a python thing
    In other languages they're usually called:
        Hash Tables, Hash Maps, or some combination of that
"""
# used internally by dictionaries, you never actually need it
print(hash('asdhfsajf'))

"""
    Completely different
    
    Let's talk about string slices
        this is a pure python thing, not in many other languages
"""
my_string = 'hello i am a long string with many letters'
print(my_string[2:6], my_string[13:25])

new_string = 'abcdefghijklmnop'
print(new_string[5:200000])
print(new_string[223232323:12938179839813798])
print(new_string[10:5])

# replace the thing at index 10 with an x
new_string = new_string[0:10] + 'x' + new_string[11:len(new_string)]
print(new_string)

# default numbers: if the first slot is empty it is zero
#                  if the second slot is empty then it is the end
print(new_string[:7])
print(new_string[12:])
print(new_string[:])

