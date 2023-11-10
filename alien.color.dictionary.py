# using dictionaries

alien_o = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

print("\nThe alien's color is " + alien_o['color'] + ".")
# points is an interger so turn it into a string to print it out
print("\nThe alien's point value is "+ str(alien_o['points']) + ".")
print(alien_o)

print("\n")

# define empty dictionary
alien_one={}

# add items to the dictionary
alien_one['color'] = 'red'
alien_one['points'] = '10'

print(alien_one)

print("\n")

# Change the value in the dictionary.
alien_o['color'] = 'black'

print("The color of alien_o is now " + alien_o['color'] + ".")

print("\n")

# Move the alien at a medium speed.

alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("alien_o's original position is " + str(alien_o['x_position']) + ","
    + str(alien_o['y_position']) + ".")

if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position of the alien is:
alien_o['x_position'] = alien_o['x_position'] + x_increment
print("New x-position: " + str(alien_o['x_position']))

print("\n")

# remove (delete) a key:value from a dictionary

alien_two = {'color': 'black', 'points': 100}
print(alien_two)

del alien_two['points']
print(alien_two)

print("\n")
