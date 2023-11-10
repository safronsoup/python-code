#!/usr/bin/env python3

import os, sys
os.system("clear")

# 'yield' replaces 'return' and creates a sequence of results
# generator function - creates a sequence of results
# - temp suspends the function execution
# - returns to suspend point, remembering 'state; remembers values of locally scoped variables
# - is used to produce iterable results from a function
# iterable results - a collection, sequence, list, tuple, dictionary; something you can loop through
#      using a for loop

# helpful when we can't load up things into memory at once

# use a generator function to read a file that has a lot of data that can't be loaded into memory
#   initially


def myFunc():
    i = 1
    
    print("First")
    print(i)
    i += 1
    
    print("Second")
    print(i)
    i += 1
    
    print("Third")
    # print(i)

    return i

# at this point, the # 3 is not returned
myFunc()

print("Run function again.")

# at this point, the # 3 is returned

x = myFunc()
print(x)

#################################

def myGenFunc():
    i = 1

    print("Letter A")
    # suspend here
    yield i

    print("Letter B")
    i += 1
    # suspend here
    yield i

    print("Letter C")
    i += 1
    # suspend here
    yield i

# result = myGenFunc()
# # return next item from the iterator
# print( next(result) )
# print( next(result) )
# print( next(result) )

# this prints generates a StopIteration
# print( next(result) )

for result in myGenFunc():
    print(result)


#################################

# read a file and print out the results
def csvReader(fileName):
    file = open(fileName)
    # go through the whole file and return each value
    # return file.read()

    # go through the whole file, load it into memory, and split it on new line characters \n
    # split - Return a list of the words in the string, using sep as the delimiter string.
    return file.read().split("\n")


# csv = csvReader("samplecsv.txt")
# print(csv)

print()
print()

# iterate through file and yield the result of each line
def csvReader(fileName):
    for line in open(fileName):
        yield line

# csv = csvReader("samplecsv.txt")

# for result in csv:
    print(result)

#################################

# create inline iterable
# do the work upfront
# list comprehension
listOne = [i  * 2 for i in range(100)]

# get size in Bytes of list, import sys at the top of the program
# print(sys.getsizeof(listOne))

# inline generator function; anonymous lambda function
# this does not execute right away; see the size of listTwo
listTwo = (i * 2 for i in range(100) )
# print(sys.getsizeof(listTwo))

for i in listOne:
    print(i)

# all the work for listTwo is done here everytime it is called
# it does NOT front load the work; take a lot of work and spread it out over time
for i in listTwo:
    print(i)
