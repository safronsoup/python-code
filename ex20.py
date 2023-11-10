from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

# seek(#) = start at byte count #
def rewind(f):
    f.seek(0)

# comma after readline() avoids printing the \n at the end of the
# line in the file
def print_a_line(line_count, f):
    print line_count, f.readline(),

# open a file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Let's rewind, kind of link a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
#current_line += current_line
print_a_line(current_line, current_file)

current_line = current_line + 1
#current_line += current_line
print_a_line(current_line, current_file)
