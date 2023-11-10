from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "\n"
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

# exists returns TRUE if file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# append data to to_file
out_file = open(to_file, 'a').write(indata)
#out_file.write(indata)

print "Alright, all done."

# no need to close files. why??
#out_file.close()
#in_file.close()
