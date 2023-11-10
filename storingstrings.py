# text in python is stored in a series of individual characters
# so interpreter can manage the memory of the variables

# boolean - true/false - single bit used in memory - 0/1
# integer - stored in Bytes (8 bits); 1 Byte can store 256 numbers (0-255); stored in 4 Bytes (2^32)
# float - 8 Bytes of memory (2^64)
# string - store 1 Byte at a time, which stores 1 character; string variable is a pointer to that byte, which
#  is in turn a pointer to another Byte and another Byte, etc., until the end of the string; "stringing"
#  together many characters; a stirng is a collection of individual characters, individual Bytes

# strings are immutable, they can't be changed, they can only be replaced

import os

os.system('clear')

myName = "Jeff"
# print the ID of the variable
print(id(myName))

# look at each character in variable myName and print them out
for letter in myName:
    print(f"{letter}", end="")

print("")

# print third character (index 2) in variable myName - third because it is zero based -
#   start at zero [0 1 2 3]
print(myName[2])

# this is an error and is not allowed
# myName[2] = "q"

# this is a second variable of the same name
myName = "Christopher"
print(id(myName))

# python points to the same space in memory for the values assigned to variables myName and Chris
Chris = "Christopher"
print(id(Chris))