# how does a computer store text values?
# each character is one Byte in length
# each character is assigned a numeric value
# ASCII defines one Byte of data to store characters

import os
os.system('clear')

print(ord("A"))
print(ord("j"))

# Unicode - 1980s - 6 Bytes per character
# first (left) Byte is the same to match the ASCII code, then use five more Bytes
# code

# Python defaults to UTF-8
# 01000010 = A but in Unicode there will be an additional 5x 00000000 > a lot of dead space
# UTF-8 is the math that is used to store the values of each character
# if the character can fit inside one Byte, do it, then string together other Bytes if needed
