x = 10 

# create three different variables and assign a value to them
x, y, z = 10, 7.5, "Three"

print(x, y, z)
# print(y)
# print(z)

name1 = "Ben"
name2 = "Donna"

name3 = name2
print(name3)

name4 = "Jeff"
name5 = "Tom"
name6 = "Sam"

# right most operation was evaluated first
name6 = name5 = name4 = "Irene"

print(name4)
print(name5)
print(name6)