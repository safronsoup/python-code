from sys import argv

script, hobby = argv

print "What is your favorite hobby? ", hobby

color = raw_input("What is your favorite color? ")

print "Your favorite hobby is %r and your favorite color is %r." % (
    hobby, color)
