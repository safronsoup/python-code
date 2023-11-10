import os
os.system("clear")

# iterate through dictionary keys with a for loop to get the value you want
# getting keys only
# "in" operator checks the existence of a key
# keys() returns list of keys
# values() returns list of values
# items() returns list of items, as a list of lists: ((k,v) (k,v), (k,v))

studentGrades = { "Ben" : 92, "Diane" : 97, "Sam" : 81 }

# print out the keys
#for item in studentGrades:
#    print(f"Dictionary keys are: {item}")

# print out the values for each key
#for item in studentGrades:
#    print(f"Student grades are: {studentGrades[item]}")

# is the key in the dictionary?
if "Ben" in studentGrades:
    print("It is!")
    # need to use single quotes in the [] because there are already double quotes in the string
    print(f"The grade is {studentGrades['Ben']}.")

# can't treat the below as regular lists; these are special dictionary values lists
# print out, in a list format, the keys from the dictionary
print(studentGrades.keys())
# print out, in a list format, the values from the dictionary
print(studentGrades.values())
# print out, in a list format, the key:value pairs from the dictionary
print(studentGrades.items())

# find a value in the dictionary
if 92 in studentGrades.values():
    print("92 is in the values.")

# this fails
values = studentGrades.values()
# print(values[1])

# cast the dictionary values list into a list, the pull data out of it
values = studentGrades.values()
print(len(values))
valuesList = list(values)
print(valuesList)
print(valuesList[1])

keys = studentGrades.keys()
keysList = list(keys)
print(keysList)
print(keysList[2])

# iterate through they keys from 0 to end (0 to 2, this is 3 indexes) and print out the keys
for i in range(0,len(values)):
    print(studentGrades[keysList[i]])

# convert the dictionary items list into a list
# print out the key:value pair at index x of the itemsList
items = studentGrades.items()
itemsList = list(items)
print(itemsList[2])

# print out the value for a certain key x
print(itemsList[0][0], itemsList[0][1])
print(itemsList[1][0], itemsList[1][1])
print(itemsList[2][0], itemsList[2][1])