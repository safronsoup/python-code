import os
os.system("clear")

# functions reprsent a block of code with an identifer that can be run (invoked) on demand
# by referencing it
# send paramters/arguments to the function
# print(), input() function
# functions often accept 'parameters', values, that customize the way it operates

# functions are built in to the python (standard), part of a 3rd party library, or written by us

# get input from the user

prompt = "Enter your name, then press enter: "

# inside the () is the parameter
#userInput = input("Type your name. ")
userInput =input(prompt)

# two parameters in side the ()
print("The user's name is: ", userInput)
print(f"Your name is {userInput}.")

# positional parameters:
# ordinal = supplied in the proper order
# named = supplied in any order, indicate each value and each parameter

# ordinal parameters followed by named parameters; named parameters can be in any order
print("The user's name is: ", userInput, end=";", sep="cc")
print("The user's name is: ", userInput, sep="cc", end="x")
