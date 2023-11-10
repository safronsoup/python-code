# nesting a set of dictionaries in a list or a list of items as a value in a
# dictionary or a dictionary inside a dictionary

print("\n")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# a list of alien dictionaries
aliens = [alien_0, alien_1, alien_2]

# print each item in list "aliens", which are dictionaries
for alien in aliens:
    print(alien)

print("\n")

# an empty alien list
aliens = []

# make 30 green aliens using the range command; range command says how many
# times the for loop will repeat
for alien_number in range(0,30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

# show the first 5 aliens using a slice
for alien in aliens[:5]:
    print(alien)
    print("------------------------------------------------")

print("\n")

# how many aliens have been created?
print("Total number of aliens: " + str(len(aliens)))

print("\n")


# an empty alien list
aliens = []

# make 30 green aliens using the range command; range command says how many
# times the for loop will repeat
for alien_number in range(0,30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

# change aliens [0, 1, 2] to yellow, medium-speed, 10 points
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# change aliens [3 - 7] to yellow, medium-speed, 10 points
for alien in aliens[3:7]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 10 aliens using a slice [0 - 9]
for alien in aliens[:10]:
    print(alien)

print("\n")

# how many aliens have been created?
print("Total number of aliens: " + str(len(aliens)))

print("\n")
