
# print a newline character (\n)
print()

# pass in a string literal
print("")

# print a variable
myName = "John"
print(myName)

# concatenate; space after "Hello!" added automatically
print("Hello!",myName)

# conatenate; no space after "Hello!"
print("Hello!" + myName)

# print attempts to convert values passed to it into a string value
age = 43
print("Hello", "Jeff", "you are", age, "years old.")

# error will be produced since the print function tries to operate on a string and integer type;
# print does not know if this is a concatenation or a print
print("Hello", "Jeff", "you are" + age, "years old.")

# be percise about what you pass to the print function; don't rely on the print function to 
# convert it to a string