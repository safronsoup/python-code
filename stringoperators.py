# string operators - return a string (text) value
# + is concatenate
# * is repeat
# [] is slice
# [:] is range slice

name1 = "Jeff"
name2 = "Scott"

fullName = name1 + " " + name2
print(fullName)

textValue = "r"

textValue = textValue * 5

print(textValue)

# slice, range slice - to pull out a piece of text
textValue = "RepeatME"

# get first character from the left
textValue = textValue[0]
print(textValue)

# get second character from the left
textValue = "RepeatME"
textValue = textValue[1]
print(textValue)


# get first character from the right
textValue = "RepeatME"
textValue = textValue[-1]
print(textValue)

# get second character from the right
textValue = "RepeatME"
textValue = textValue[-2]
print(textValue)

# range slice - get 4th and 5th character from the left
textValue = "RepeatME"
# RepeatMe
# 01234567 >> used in slice
# 12345678 >> character #
# start at 3 and go UP TO 5; 5 is NOT included
textValue = textValue[3:5]
print(textValue)


# bitwise operators perform binary operations
# AND 0011 & 0101 = 0001
# OR 0011 | 0101 = 01111
# NOT -0011 = 1100
# XOR 0011 ^ 0101 = 0110
# SHIFT RIGHT 101 >> 2 = 1
# SHIFT LEFT 101 << 2 = 10100

print(82//25)