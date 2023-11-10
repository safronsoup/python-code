# modulo - determines if a number is odd or even

prompt = "\nEnter a number and I'll tell you if it's even or odd: "

# store input as a string
number = input(prompt)
# change number to an interger
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

print("\n")

# rental car request
prompt = "\nWhat kind of rental card would you like, a Subaru or a VW? "
rental_car = input(prompt)

if rental_car == 'Subaru':
    print("\nThe Subaru is in the shop.")
else:
    print("\nThe VW is small and sporty.")

print("\n")

# dinning group number
prompt = "\nHow many people are in your dinning group? "
size = input(prompt)
size = int(size)

if size > 8:
    print("\nThere are more than eight in your dinning group. " +
        "You will have to wait for a table.")
else:
    print("\nCome with me and I can sit you by the window.")

print("\n")

# modulo 10
prompt = "\nType a number and I'll tell you if it is a multiple of 10. "
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print("\n" + str(number) + " is a multiple of 10.")
else:
    print("\n" + str(number) + " is not a multiple of 10.")

print("\n")
