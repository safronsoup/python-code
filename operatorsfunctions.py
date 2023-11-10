import os
os.system("clear")

# operator  description
# +         concatenation
# *         repetition
# []        slice (a text string is stored as a string of individual characters)
# [:]       range slice [2:4]
#  in       membership
# not in    non-membership
# r         raw string
# f         f-string formatting
# 




name1 = "Jeff"
name2 = "Lavender"

bothNames = name1 + name2
print(bothNames)

bothNames = name1 + " " + name2
print(bothNames)

# repetition
value = name1 * 3
print(value)

# []        slice (a text string is stored as a string of individual characters); 0 base operator
print(name1[2])

# [:]       range slice [2:4]; starting and ending (but NOT including index)
# lavender
# 01234567
# prints index number 3, 4, 5
print(name2[3:6])

# membership - not in
if "ff" in name2:
    print("It is in the string.")
else:
    print("It is not in the string.")

lookFor = "en"
if lookFor not in name2:
    print(f"The string {lookFor} is not in the {name1}.")
else:
    print(f"The string {lookFor} is in {name2}")

# raw string
print("Hello\r\nThere")

# ignore the escape characters; print the raw data between the quotes, as is
print(r"Hello\r\nThere")
print(r"Hello, there 'Bob'.")

# String FUNCTIONS
# operator  description
# upper()   upper-case all letters
# lower()   lower-case all letters
# capitalize()  upper-case first letter
# split()   creates a list object by word
# join()    joins a list object into a string
# ord()     converrst to the unicode value (decimal)
# chr()     converts to text (from decimal)
# len()     character count

# variable.functionname() = run function against variable

name1 = "jeff"
name2 = "thomas"
name3 = "BILLYBOB"

print(name1.upper())
print(name2.capitalize())
print(name3.lower())

# create a list of objects from the string
name4 = "Jeff is exercising today."
splitName4 = name4.split()
print(splitName4)

# print the items in the list; lists are zero based
print(splitName4[0])
print(splitName4[1])
print(splitName4[2])
print(splitName4[3])

# print the length of the item in index 2 of the list
print(len(splitName4[2]))

print(chr(656))
print(ord("A"))