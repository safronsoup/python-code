# conditionals are written as:
# if <conditional statement> then <code to execute> else <code to execute>
# the if statement uses relational operators to test an expression
# a true result causes the then to execute
# a false result causes the else to exectue

# < less
# > greater
# <= less than or equal to
# >= greater than or equal to
# != not equal to

# if <boolean expresion>:
#   <statement(s)>
# else:
#   <statemetn(s)>

# keywords (if, else)
# colon (:)
# indentation

x = 100
y = 100

if x > y:
    print("X is greater than Y.")
    print("Goodbye.")
else:
    print("Y is greater than X.")
    print("You knew that.")

print("This line is always printed.")

isThisTrue = False
isThisFalse = True

if isThisTrue:
    print("This is true.")
else:
    print("This is false.")


if x > y:
    print("X is greater than Y.")
    print("Goodbye.")
elif x < y:
    print("Y is greater than X.")
    print("You knew that.")
else:
    print("X equals Y.")