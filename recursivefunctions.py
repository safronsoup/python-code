#!/usr/bin/env python3

import os
os.system("clear")

# recursive functions - a function that invokes itself
# similar to a loop
# can shorten syntax - sometimes a lit
# high potential for infinite looping

# func:
#   1. test (should always be first)
#   2. code to run
#   3. invoke yourself again (should always be last)

# factorial 6! = 6 * 5 * 4 * 3 * 2 * 1

# define factorial function
def factorial(number):
    final = 1
    for i in range(number, 0, -1):
        final = final * i
    return final

# print the answer to the function factorial
# print( factorial(5) )

def factorialRecur(number):
    # test: if we reach the number 1, then we are done
    # print(number)
    if number == 1:
        return number
    else:
        # print(number)
        # this is the code to run and invokes function again
        return number * factorialRecur(number - 1)
        

print( factorialRecur(6) )