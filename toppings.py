# if statements

print("\n")
requested_toppings = 'mushrooms'

# test requested_toppings
if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

print("\n")

# check of inequality
answer = 17
test_parameter = 55
print("Is " + str(answer) + " equal to " + str(test_parameter) + "?")
if answer != test_parameter:
    print("No, " + str(answer) + " is not equal to " + str(test_parameter) + ".")
else:
    print("Yes, " + str(answer) + " is equal to " + str(test_parameter) + ".")

print("\n")

answer1 = 1
test_parameter1 = 118
print("Is " + str(answer1) + " less than " + str(test_parameter1) + "?")
# test for less than
if answer1 < test_parameter1:
    print("Yes, " + str(answer1) + " is less than " + str(test_parameter1) + ".")
else:
    print("No, " + str(answer1) + " is not less than " + str(test_parameter1) + ".")

print("\n")

answer2 = 1
test_parameter2 = 5999
print("Is " + str(answer2) + " greater than " + str(test_parameter2) + "?")
# test for greater than
if answer2 > test_parameter2:
    print("Yes, " + str(answer2) + " is greater than " + str(test_parameter2) + ".")
else:
    print("No, " + str(answer2) + " is not greater than " + str(test_parameter2) + ".")

print("\n")

# conditional - and or
min_adult_age = 21
max_child_age = 12

adult_age = 22
child_age = 12

if (adult_age >= min_adult_age) and ( child_age <= max_child_age):
    print("The adult gets free alcohol and the child gets free juice.")
else:
    print("NO DRINKS FOR YOU!")

print("\n")

# using "in" to find a value in a list before performing action
users = ['bill', 'naomi', 'corey', 'dave', 'roger', 'rob']
user1 = 'naomi'
user2 = 'jeff'

if 'user1' or 'user2' in users:  # can use condition here to match mutiple users
    print(user1.title() + " and " + user2.title() + ", one of you have alread registered.")

print("\n")

# determing if someone is NOT in a list
bannded_users = ['bill', 'naomi', 'corey', 'dave', 'roger', 'rob']
user = 'naomi'

if user not in bannded_users:
    print(user.title() + ", you are a bannded user and don't have access to the system.")
    print("You will need to submit Form 2875 before gaining access.")
else:
    print(user.title() + ", you have access to the system.")
    print("Click 'Ok' to proceed to the login screen.")

print("\n")

# using if-elif-else statements to evaluate more than one conditional
age = 164

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif (age < 100) and age >= 65:
    price = 5
else:
    price = 0

print("Your age is " + str(age) + ".")
print("Your admission cost is $" + str(price) + ".")

print("\n")
