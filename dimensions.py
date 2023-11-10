# working with tuples - an immutable list - a list that does not change

dimensions = (200,50,25,65,45,67,91,2,1,9,58,33,22)
print(dimensions[0])
print(dimensions[1])

print("\n")

# loop through items in tuple
for dimension in dimensions:
    print(dimension)

print("\n")

# change item in tuples
dimensions = (200,50,25,65,45,67,91,2,1,9,58,33,100)

# loop through items in tuple
for dimension in dimensions:
    print(dimension)
