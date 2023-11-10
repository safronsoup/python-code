# sort a dictionary

print("\n")

# return items in a certain order by sorting the keys are they street_address
# returned in the for loop; use the sorted() function to get a copy of
# of the keys in order

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\n")

print("The following languages have been mentioned: ")

# pull each value in the dictionary and print it without checking for repeats
for language in favorite_languages.values():
    print(language.title())

print("\n")

# pull each value in the dictionary and use set() to print each values
# WITHOUT checking for repeats
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")
