import os

os.system('clear')

# definite iteration: for loop

# for ... then ...
# the for loop requires an iterable object (list, arrays, tuples); one variable with multiple values
# the code will execute for each value of the object
# upon completion, code continues

# for <x> in <y>:
#   <statement(s)>

# keywords: for, in
# variable and iterable (x and y)
# colon (:)
# indentation

# variable x does NOT exist until the for loop starts
# x increases automatically since it is part of an iterable object
# print upto 15 but NOT 15
# range(start,end,index value)
for x in range(10,100,10): 
    print("This is the current value of x: ", str(x))
    print("Now we're going to change x!")

print()
# print("This is outside the while loop.")
print()

# count down from 200 to 0 (but not 0) by an index of 10
for x in range(200,0,-10):
    print("Count down by 10s: ", str(x))

# one variable but multiple values
names = ["Bob", "Sam", "Chris", "JoAnn"]
for name in names:
    print("Name is: ", name)