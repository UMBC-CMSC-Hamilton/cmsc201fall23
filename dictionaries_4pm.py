def problem_two():
    if __name__ == '__main__':
        string_list = []
        s = input("Enter a string: ")
        while s != "stop":
            string_list.append(s.lower())
            s = input("Enter a string: ")
        # begin your code here
        # if i have a string s
        max_string = ''
        max_count = -1
        for s in string_list:
            count = 0
            for char in s:
                if char == 'a':
                    count += 1
            if count > max_count:
                max_count = count
                max_string = s
        
        print(max_string)


"""
    Dictionaries - extension of the concept of a list
        in a list you have indices and they give you values
        
        in a dictionary you have keys which give values
        keys are any immutable type
            string, bool, int, float
                there are others: datetime, None
        values can be anything, lists, dicts, floats, bool, int, string, anything really
    
"""

my_movies = {'Fifth Element': 10, 'Prisoners': 8, 'GoG': 8.5,
             'Oppenheimer': 7, 'Wild Wild West': 4, 'Despicable Me 2': 7.5
             }
print(my_movies)
my_movies['GoG'] = 7.5
print(my_movies)
print(my_movies['Oppenheimer'], my_movies['Wild Wild West'])
# this should result in a KeyError if the key is not in the dict
# print(my_movies[7])
del my_movies['Despicable Me 2']
print(my_movies)

# later key will overwrite previous key
# no duplicate keys
my_numbers = {1: 'yellow', 2: 'sandwich', 3: 'aardvark',
              4: 'firefighters', 1: 'turnip'}
print(my_numbers)

"""
    Whatever you choose to be the key in the dictionary should be unique
    
    SSN = probably ok if you're the SSA
    student IDs
    anything that is unique and doesn't change
"""
users = {'eric8': ['password1', 55.00, 'Eric'],
         'sa123': ['asdf1234', 450.00, 'Samantha'],
         'john55': ['passWord', 123.55, 'Jonathan'],
         'an3487': ['pw3', 44.33, 'Anise']}

total = 0
for username in users:
    print(username, users[username])
    total += users[username][1]

print('The total amount of money is $', total)

PASSWORD = 0
MONEY = 1
NAME = 2

print(users['john55'][MONEY])

rando_dictionary = {5: 'happy', 'raddish': 17, True: 52,
                    None: 'pickle', 1: 1701}

print(rando_dictionary)
print(rando_dictionary[5] + rando_dictionary[None])

# one of the many reasons to avoid mixing data types
# print(rando_dictionary[True] + rando_dictionary[5])

users['kevin6'] = ['a;sodhwohfna;sjdhf;ajsgdb;sa;foih', 0.00, 'Kevin']

numbers_dictionary = {
    1: 'hi',
    2: 'fifty',
    3: 'unicorn',
    18: 'salmon',
    25: 'lamb',
    26: 'frog',
    357: 'meme'
}

numbers_dictionary[255] = 'pickleball'
print(numbers_dictionary)

# only checks keys not values
if 4 in numbers_dictionary:
    del numbers_dictionary[4]

def remove_stuff():
    remove_list = []
    for x in numbers_dictionary:
        print(x, numbers_dictionary[x])
        y_n = input("Do you want to remove this element? ")
        if y_n.lower() in ['y', 'yes']:
            remove_list.append(x)
    
    # This loop prevents the runtime error when you try to delete from a dictionary
    for key in remove_list:
        del numbers_dictionary[key]
        
    print(numbers_dictionary)

"""
dict.keys()
dict.values()
"""

print(numbers_dictionary.values())
print(users.values())

# probably never need this, if you really want
print(users.keys())
# this should never happen
for x in users.keys():
    print(x)

"""
    Everywhere else dictionaries are called: Hash--
    Hash Tables, Hash Maps, Hashes
"""
# EXISTS but you don't need to call this
print(hash('hello'))

"""
    String Slices
        substring that is taken from a particular index to an end index
"""

my_fav_str = 'YellowTurkeyChickenPieRobotFantasticSandwich'
# llow
print(my_fav_str[2:6])
# hickenPieRobotFantasticSandwich
print(my_fav_str[13:20000000000])
# empty string
print(my_fav_str[35:19])
print(my_fav_str[350:1900])

