# testing multiple conditions before making a decision
print("\n")

requested_toppings = ['mushrooms', 'extra cheese']

# three independent tests run each time
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza.")

# alien colors
alien_color = ['green', 'yellow', 'red']
alien = 'blue'

if alien in alien_color:
    print("\nYou just earned 5 points!")

if alien == 'green':
    print("\nYou just earned 5 points!")
else:
    print("\nYou just earned 10 points!")

if alien == 'green':
    print("\nYou just earned 5 points!")
if alien == 'yellow':
    print("\nYou just earned 10 points!")
if alien == 'red':
    print("\nYou just earned 15 points!")

if alien == 'green':
    print("\nYou just earned 5 points!")
elif alien == 'yellow':
    print("\nYou just earned 10 points!")
elif alien == 'red':
    print("\nYou just earned 15 points!")

# your age
age = 62
if age < 2:
    print("\nYou are a baby.")
elif (age >= 2) and (age < 4):
    print("\nYou are a toddler.")
elif (age >= 4) and (age < 13):
    print("\nYou are a kid.")
elif (age >= 13) and (age < 20):
    print("\nYou are a teenager.")
elif (age >= 20) and (age < 65):
    print("\nYou are a adult.")
elif (age >= 65):
    print("\nYou are an elder.")

print("\n")

# conditional for-if; check item in list before making pizza
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']


for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

print("\n")


# cheese pizza please
requested_toppings = []
# when the name of a list is used in an if statement, Pyton
# returns True if the list contains at least ONE item; an empty
# list evaluates to False, therefore go to the else statement.
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want just a cheeze pizza?")

print("\n")
