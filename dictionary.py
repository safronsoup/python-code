import os
os.system("clear")

# dictionary - a key:value pair
# map to data formats JSON and XML
# ordered - indexed
# dynamically typed (mixed types of variables: string, number, float, etc.)
# mutable (changeable)
# keys are named
# key:value = "name" : "John"
#{
#   "key1" : "value1" ,
#   "key2" : "value2" ,
#   3      : "value3" ,
#   4      : 5.67
# }

student = { 
                "name" : "John", 
                "age" : 18, 
                "GPA" : 3.98
            }

print(student['name'])

studentGrades = { "Ben" : 92, "Diane" : 97, "Sam" : 81 }
print(f"Ben's grade in {studentGrades['Ben']}.")

myCar = { "Make" : "Porsche", "Model" : 911, "Year" : 2021 }
print(myCar['Make'])

# dictionaries in a list
myCars = ( { "Make" : "Porsche", "Model" : 911, "Year" : 2021 },
           { "Make" : "Chevy", "Model" : "Camero", "Year" : 1981 }
        )

print(myCars[0]["Make"], myCars[0]["Year"])
print(myCars[1]["Make"], myCars[1]["Model"])


# list inside of dictonaries
bikes = { "Make" : "Cannondale", "Year" : 2018, "colors" : ("Blue", "Red") }
print(bikes["Make"], bikes["colors"][0])

# list inside a dictionary inside a list
myCars = ( { "Make" : "Porsche", "Model" : 911, "Year" : 2021, "colors" : ("Blue", "Red") },
           { "Make" : "Chevy", "Model" : "Camero", "Year" : 1981, "colors" : ("Silver", "Black") }
        )

print(myCars[0]["Make"], myCars[0]["colors"][0])
print(myCars[1]["Year"], myCars[1]["colors"][1])
