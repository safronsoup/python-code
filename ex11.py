# the comma is so print doesn't end the line with a newline character
print "How old are you?",
age = raw_input() # can add a prompt within the (): ('--> ')
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

# using %s, there are no quotes around age, height, and weight
# using %r, there are quotes around the age, height, and weight
print "So you're %s old, %s tall and %s heavy." % (
    age, height, weight)
print "So you're %r old, %r tall and %r heavy."% (
    age, height, weight)
