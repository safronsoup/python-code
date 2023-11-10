#!/usr/bin/env python3
import os, time
os.system("clear")

# define your own code as a function THEN invoke it whenever you would like

# def <function name>():
# indent function code block
# can accept parameters
# both positional and named parameters/values
# can set default values
# functions may or may not reutn values


# define function
def GreetUser():
    if time.localtime().tm_hour < 12:
        print("Good morning user!")
    else:
        print("Good afternoon user!")

# call function
GreetUser()


# define function and pass a parameter/variable (name)
def GreetUser2(name):
    if time.localtime().tm_hour < 12:
        print(f"Good morning {name}!")
    else:
        print(f"Good afternoon {name}!")

GreetUser2("Jeff")


# value is a zero-based index, so -1 in value[pos - 1] means start a zero index
# can set pos to a default value by: isVowel(value, pos=1); it will be invoked if a value for pos is
# NOT supplied
def isVowel(value, pos=1):
    if len(value) < pos:
            print("String too short.")
    elif value[pos - 1] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        print(f"The value in position {pos} IS a vowel.")
    else:
        print(f"The value in position {pos} is NOT a vowel.")


# two parameters passed when pos is NOT assigned a default value in def isVowel(value, pos)
# parameters must be in the same order as what is defined in the def
isVowel("Jeffrey", 2)

# one parameters passed when pos IS assigned a default value in def isVowel(value)
# parameters must be in the same order as what is defined in the def
isVowel("Jeffrey")

# named parameters do not need to be in the same order as what is defined in the def
isVowel(pos=3, value="Sammy")



# returning values to the called def
def isVowel2(value, pos=1):
    if len(value) < pos:
            return "String too short."
    elif value[pos - 1] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        return f"The value in position {pos} IS a vowel."
    else:
        return f"The value in position {pos} is NOT a vowel."

# print( isVowel2(value="Jeffrey", pos=6) )

result = isVowel2(value="Jeffrey", pos=6)
print(result)