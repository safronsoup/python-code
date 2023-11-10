#!/usr/bin/env python3

import os, dis
os.system("clear")

# lambda function - a cleaner way to write a function
# less verbose, can be defined inline for immediate execution
# simple "unnamed" functions
# short, uncluttered syntax
# no statement
# limited to a SINGLE expressions
# can be executed as defined (IIFE) - immediately invoked function execution

# assign function to a variable
doubleIt = lambda x: x*2

# pass value to the lambda function and print the answer
print(doubleIt(5))

# traditional function
def doubleItFunc(x):
    return x*2

print(doubleItFunc(3))

print(doubleIt)
print(doubleItFunc)

# show commands inside functions; no different in byte code inside both functions
print(dis.dis(doubleIt))
print(dis.dis(doubleItFunc))

my_list = [1,5,4,6,8,11,3,12,47,101,203,999,1000,772,397]

# filter my_list; create a lambda function within filter()
# filter() grabs every value out of my_list and, one-by-one, apply them to the lambda x function
# and check to see if the number is even (modulo 2)
# filter() will throw out any operation where the lambda function returns a false
newListEven = filter( lambda x: (x%2 == 0), my_list )

# select odd number from my_list
newListOdd = filter( lambda x: (x%2 == 1), my_list )

# cast newList as a list
newListEven = list(newListEven)
newListOdd = list(newListOdd)

# print lists
print(newListEven)
print(newListOdd)