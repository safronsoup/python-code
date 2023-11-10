# string (text) formatting methods:
# %-formatting = not recommended; verbose, ugly
# str.format() = superseded by f-strings
# f-strings = formattted string literals

print()

name = "Jeff"
age  = 53

# string formatting
print("string formatting")
print("Hello", name, ", you are", age, "years old.")
print("Hello " + name + ", you are " + str(age) + " years old.")
print()

# % formatting
# take value in variable, name, and insert it into where the (first) %s is located.
print("% formatting")
print("Hello, %s" % name)

# take value in variables names and age in the tuple and insert it into where the 
# first and second %s is located. No need to convert integer age into a string.
print("Hello %s, you are %s years old." % (name, age))
print()

# str.format() - run function format agaist string inside the print() statement
print("str.format() function")
print("Hello {}, you are {} years old.".format(name, age))

# {1} is age and {0} is name
print("Hello {1}, you are {0} years old.".format(name, age))
print("Hello {0}, you are {1} years old.".format(name, age))
print()

# f-stings, introduced in 3.6
# f tells python to interpret the string as a statements/variables
print("f-string")
print(f"Hello {name}, you are {age} years old.")

# add an expression into the string
print(f"Hello {name}, in ten years, you'll be {age + 10} years old.")
print()

# message format
message = (
    f"Hello {name}, "
    f"you are {age} years old. "
    f"In ten years, you'll be {age + 10} years old."
)
print(message)
print()