# loop through dictionary
employee_1 = {
    'first_name': 'jen',
    'last_name': 'mckenzie',
    'street_address': '308 Blackball Street',
    'city': 'austin',
    'state': 'tx',
    'zip_code': 78511,
    'home_phone': '888-347-5166',
    }

# for loop to print out each key:value pair
# use method items() to return the key, value in the dictionary
# key and value are just place holders, could be k,v
for key,value in employee_1.items():
    print("\nKey: " + key)
    print("Value: " + str(value).upper())

print("\n")

# loop through all the keys in a dictionary
# use method keys() to return just the key in the dictionary
# looping through key is the default when looping through a dictionary -
# no need to add .keys()
for key in employee_1.keys():
    print(str(key.upper()))

print("\n")

##########################################
# using lists and dictionaries
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# list of friends
friends = ['phil', 'sarah']

# pull the key from the favorite_languages dictionary,
# assign it to variable name, and the print it
for name in favorite_languages.keys():
    print(name.title())

# if the name of the person is also in the friends list, the print their
# programming language; referencing favorite_languages[name] displays
# the value related to the key names
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
    elif name not in friends:
        print(name.title() + ", please take our poll!")

print("\n")
