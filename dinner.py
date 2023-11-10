# people i would invite to dinner

people = [ 'warren buffet', 'mom', 'abraham lincoln', 'mark shurman' ]

invitation = people[0].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[1].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[2].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[3].title() + ", would you like to have dinner with me?"
print(invitation)

cant_make_it = people[2].title() + " can't make it to dinner."
print(cant_make_it)
print("\n")

removed_from_list = people.pop(2)
# print(people)
substitute_guest = 'yasuke'
people.append(substitute_guest)

invitation = people[0].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[1].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[2].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[3].title() + ", would you like to have dinner with me?"
print(invitation)
print("\n")

update = "We found a bigger dinner table!"
print(update)
print("\n")

# add new people to people list
people.insert(0, 'bruce lee')
people.insert(2, 'tom jones')
people.append('sade')

# print(people)

invitation = people[0].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[1].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[2].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[3].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[4].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[5].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[6].title() + ", would you like to have dinner with me?"
print(invitation)

print("\n")

# only 2 people can have dinner with me
print("Sorry, but I can only invite two poeple to dinner!")
print("\n")

guest = people.pop()
removed_guest = "Sorry, " + guest.title() + ", I can only invite two people to dinner."
print(removed_guest)

guest = people.pop()
removed_guest = "Sorry, " + guest.title() + ", I can only invite two people to dinner."
print(removed_guest)

guest = people.pop()
removed_guest = "Sorry, " + guest.title() + ", I can only invite two people to dinner."
print(removed_guest)

guest = people.pop()
removed_guest = "Sorry, " + guest.title() + ", I can only invite two people to dinner."
print(removed_guest)

guest = people.pop()
removed_guest = "Sorry, " + guest.title() + ", I can only invite two people to dinner."
print(removed_guest)
print("\n")

# print(people)

invitation = people[0].title() + ", would you like to have dinner with me?"
print(invitation)

invitation = people[1].title() + ", would you like to have dinner with me?"
print(invitation)

print("\n")

print("Dinner has been cancelled.")
del people[0]
del people[0]
print(people)

print("\n")
