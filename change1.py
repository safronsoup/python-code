
print()

changeAmt = input("How much change is returned? ")
changeAmt = int(changeAmt)

# How much change is give?
# changeAmt = 84

# print("The change is {}.".format(changeAmt))
print()

# Use floor division
# How many quarters are given back?

quarters = changeAmt // 25

# print(str(quarters) + " quarter(s) are given back.")
# print(quarters, "quarter(s) is/are given back.")

# changeAmt = changeAmt - (quarters * 25)
changeAmt -= (quarters * 25)

# How many dimes are given back?

dimes = changeAmt // 10

# print(str(dimes) + " dime(s) are given back.")
# print(dimes, "dime(s) are given back.")
# print("%s, dime(s) is/are given back." % dimes)

# changeAmt = changeAmt - (dimes * 10)
changeAmt -= (dimes * 10)

# How many nickels are given back?

nickels = changeAmt // 5

# print(str(nickels) + " nickel(s) are given back.")
# print(nickels, "nickel(s) is/are given back.")
# print("{0} nickel(s) is/are given back.".format(nickels))

# changeAmt = changeAmt - (nickels * 5)
changeAmt -= (nickels * 5)
# print(changeAmt)

# How many pennies are given back?

pennies = changeAmt // 1
changeAmt -= (pennies * 1)

# print(str(pennies) + " penny/pennies are given back.")
# print(pennies, "penny/pennies are given back.")
print("The change is: {0} Q, {1} D, {2} N, and {3} P.".format(quarters, dimes, nickels, pennies))
print()

# f-format
message = (
    f"{quarters} quarter(s), "
    f"{dimes} dime(s), "
    f"{nickels} nickel(s), "
    f"{pennies} penny/pennies are returned."
)

print(message)
print()

if changeAmt == 0:
    print("You have given the correct change back.")
    print()
else:
    print("You haven't given the correct change back.")
    print()