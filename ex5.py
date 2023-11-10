name = 'Jeff'
age = 45 #not a line
height = 76 # inches
weight = 158 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s harir." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print "%s is %d inches which is %f centimeters tall." % (name, height, height * 2.54)
print "%s is %d pounds which is %f kilograms." % (name, weight, weight * 0.453592)
print "Print %r no matter what." %  name 
