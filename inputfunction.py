# input() - collects data from an interactive user
# single parameter - the prompt
# returns all data as a string (text)

# assign input from user to a variable; add text literal inside parentheses
# userInput = input("What is your age? ")

# print(userInput)

promptName = "What is your name? "
nameInput = input(promptName)
# print(nameInput)

promptAge = "What is your age? "
ageInput = input(promptAge)

# must cast ageInput, which is of string type, to an integer type
# agePlusTen = int(ageInput) + 10
addToAge = 10
agePlusTen = int(ageInput) + addToAge

# must cast agePlusTen to a string type so print() can concatenate
# allInputs = nameInput + ", in 10 years, you will be " + str(agePlusTen) + " years old."

addToAgeStr = str(addToAge)
agePlusTenStr = str(agePlusTen)
stringONe = ", in "
stringTwo = " years, you will be "
stringThree = " years old."

tellHowOld = nameInput + stringONe + addToAgeStr + stringTwo + agePlusTenStr + stringThree

print(tellHowOld)