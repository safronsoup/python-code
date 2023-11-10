# slices continued

# copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\n\t My favorite foods are:")
print(my_foods)

print("\n\t My friend's favorite foods are:")
print(friend_foods)

print("\n")

# append food to each list
my_foods.append("cannoli")
friend_foods.append("ice cream")

# use a for loop to print all items in a list
for food in my_foods[:]:
    print("\t My favorite foods are: " + food)

for food in friend_foods[:]:
    print("\t My friend's favorite foods are: " + food)

print("\n")
