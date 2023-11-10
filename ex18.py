# this one (*args) is like your script with argv; take
# all the arguments to the function, put them in args
# as a list
# def = define a function
# after the : all lines that are indented four spaces will become
# attached to the function
def print_two(*args):
    arg1, arg2, = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# *args is pointless. do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# def with one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
