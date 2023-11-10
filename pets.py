# pet dictionaries

bonkers = {'kind': 'calico cat', 'owner': 'billy'}
wiskers = {'kind': 'black cat', 'owner': 'sam'}
spots = {'kind': 'shepard', 'owner': 'willy'}
rolly = {'kind': 'bull dog', 'owner': 'tom'}

pets = [bonkers, wiskers, spots, rolly]

for pet in pets:
    print(pet['owner'].title() + "'s pet is a " + pet['kind'] + ".")
