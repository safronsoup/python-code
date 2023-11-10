#!/usr/bin/env python3

import os
os.system("clear")

# variable scope - where or where not a variable is accessible from
# variables are only accessible w/in their 'scope' - global, local (defined by functions)

# variables defined in a function (either as parameters or in the code) are "only" accessible
# w/in that function

# variables defined outside of a function are known as global variables

# global variable
myName = "Chris"

# print(myName)

# this function will reference the global variable myName
def myFunc():
    print(myName)
    
# myFunc()

def myColor(color):
    print(color)
    
# myColor("red")
# this will produce an error since "color" is not defined globally
# print(color)


def myOtherName(color):
    myName = "Kitty Kat"
    print(color)
    # print local variable myName, which is assigned "Kitty Kat"
    print(myName)

# print "blue" using local variable inside the function myName
# myOtherName("blue")
# print global variable myName, which is assigned "Chris"
# print(myName)


# make a variable global in scope
def myOtherName(color):
    global myName
    myName = "Sambat"
    print(color)
    # print local variable myName, which is assigned "Kitty Kat"
    print(myName)

# invoke function print "blue" using local variable color inside the function myOtherName()
# myOtherName("blue")

# print global variable myName, which is assigned "Sambat" within the myOtherName function
# over writes the "Chris" value for myName
# print(myName)



# make a variable global in scope; nested function
def myOtherName(color):
    
    myName = "Thomas"
    
    print(myName)

    def nestedFunc():
        print(color)
    
    # invoke function; can't reference this function outside the myOtherName() parent function
    nestedFunc()


# invoke function to print "blue" using local variable color inside the nested function nestedFunc()
myOtherName("blue")

# print local variable myName, which is assigned "Thomas" within the myOtherName() function
# prints the global variable myName = "Chris"
print(myName)