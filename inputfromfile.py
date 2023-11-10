# inputting from a file methods
# - use open() with mode = r (read)
# - hand file(s) over from command-line (sys.argv)

# 3rd party modules or libraries 
import fileinput

# create a reference to the fileinput input function; use the input() in fileinput, not the input() build
# into the python standard library

# for each line in the file that is read, print the data in the line variable until EOF

# add end = '' because in the file we read, names.txt, there is a new line character at the end of each line
# and we don't want to print that out
for line in fileinput.input():
    print(line, end="")


# execute code: python3 inputfromfile.py <name of input file>