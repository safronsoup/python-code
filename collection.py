import os, fileinput

os.system("clear")

# create an empty dictionary to add student information
studentGrades = {}

# read each line in the csv file
# use the strip() method to strip the new line character \n
# use method split() to split the lines based on a ',' to 
# create a list: [ "Ben", "92" ]; index values [ 0 , 1 ]


for line in fileinput.input("studentgrades.csv"):
    values = line.strip()
    values = values.split(',')

    # for each item in the list, append it to the dictionary as a key and value pair 
    # using the update method
    # convert the values[1] to integers
    studentGrades.update({ values[0] : int(values[1]) })

print(studentGrades)

# get the average student grade
# totalStudents = len(studentGrades)
#print(totalStudents)

# initialize all the grades to 0
allGrades = 0

# for every student in the list, get the grade and sum all of them
for student in studentGrades:
    allGrades += studentGrades[student]

# verify the total value of all the grades
#print(allGrades)

# get the average grade off all the students
# averageGrade = allGrades/totalStudents
averageGrade = allGrades / len(studentGrades)
print(f"The average grade off all {len(studentGrades)} students is: {averageGrade}")