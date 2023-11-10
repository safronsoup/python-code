import os
os.system("clear")

# escape charaters are used to identify string literals vs. control characters
# "xxx" = string literal; out side the single or double quotes is code

# what if a quote is part of a string literal?
# how can we include non-printable characters?

var1 = 'Jeff "is the man" and eats chocolate'
print(var1)

var2 = "Jeff 'is the man' and can run fast"
print(var2)

# the \ is the escape character; it says the next few characters should be interpreted
# and then inserted into the string literal

var3 = "Jeff\'s 'in the cookie jar' again"
print(var3)

# to print a \ in your string literal
var4 = "Jeff\'s eating chocolate \\again"
print(var4)

# \r is a charage return; unfortunately it moves the cursor back to the beginning of the line
# and prints the next word over the previous word
var5 = "Hello\rThere"
print(var5)

var6 = "Hello\rTh"
print(var6)

# add a new line - charage feed moves the cursor down one line
var7 = "Hello\r\nThere"
print(var7)

# add a tab \t
var8 = "Jeff\tLavender"
print(var8)

# use hex value for tab 0x09
var9 = "Jeff\x09Lavender"
print(var9)