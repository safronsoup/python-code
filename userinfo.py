# Ask a user their name and age and tell some things about themselves.
userName = input("What is your name? ")
userAge = input("How old are you? ")
userAgeInt = int(userAge)

print("Hello, there " + userName + ".")

userAgeTenTime = userAgeInt * 10

# print(type(userAgeTenTime))

# Need to convert userAgeTTime to a string value to be able to print it out.
print("Your age times ten is " + str(userAgeTenTime) + ".")

# Use a conditional to determine if user is old enough to vote.
if ( userAgeInt >= 18 ):
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote!")

userName1 = input("What is your name? ")
print("Hello " + userName1 + ".")