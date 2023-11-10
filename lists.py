import os
os.system("clear")

# storing multiple discrete values in a single variable
# x = [ 43, 7, 37, 'bob' ]

# ordered, indexed, starting at 0
# dynamically typed (mixed types: numbers, characters, etc.)
# mutbale (changeable)
# reference value in list by the indexed value

# this way we need many variables
student1Name = "Sam"
student1Age = 21
student1GPA = 3.48

student2Name = "Jill"
student2Age = 19
student2GPA = 3.99

# put all names, age, and GPAs into separate lists
studentName = [ "Sam", "Jill", "Bill", "Tom" ]
studentAge = [ 21, 19, 23, 25 ]
studentGPA = [ 2.89, 3.48, 3.21, 3.99 ]

print(studentName)
print(studentAge)
print(studentGPA)

print(studentName[2])
print(studentAge[1])
print(studentGPA[0])

# for name, age, gpa in studentName, studentAge, studentGPA:
#    print(f"{name} is {age} years old and has a GPA of {gpa}.")

studentName.append("Chris")
studentAge.append(26)
studentGPA.append(2.45)
print(studentName)
print(studentAge)
print(studentGPA)

studentName.remove("Chris")
print(studentName)

x = len(studentName)
print(x)
x -= 1
while x >= 0:
    print(f"{studentName[x]} is {studentAge[x]} years old and has a GPA of {studentGPA[x]}.")
    x -= 1


# immutable ordered list - can't be changed - can't add, delete, or change a value
# tuple uses () - ordered
# # sets use {} - unordered, can't refer to sets by their index, by their ordinal position
# can't print individual items in the set based on their ordinal position; no guarantee you will
# get the items back in same order when you print them

studentTuple = ( "Lori", "Kate", "David" )
print(studentTuple[1])
# can added to tuple
# studentTuple.append("Jeff")

for name in studentTuple:
    print(name)

studentSet = { "Alan", "Steven", "Bridget" }
# can't refer to sets by their index
# print(studentSet[1])

print(studentSet)

for name in studentSet:
        print(name)
