# How much change is give?
changeAmt = 39784

# Use floor division
# How many quarters are given back?

quarters = changeAmt // 25

print(str(quarters) + " quarter(s) are given back.")

# changeAmt = changeAmt - (quarters * 25)
changeAmt -= (quarters * 25)

# How many dimes are given back?

dimes = changeAmt // 10

print(str(dimes) + " dime(s) are given back.")

# changeAmt = changeAmt - (dimes * 10)
changeAmt -= (dimes * 10)

# How many nickels are given back?

nickels = changeAmt // 5

print(str(nickels) + " nickel(s) are given back.")

# changeAmt = changeAmt - (nickels * 5)
changeAmt -= (nickels * 5)
# print(changeAmt)

# How many pennies are given back?

pennies = changeAmt // 1
changeAmt -= (pennies * 1)

print(str(pennies) + " penny/pennies are given back.")

if changeAmt == 0:
    print("You have given the correct change back.")
else:
    print("You haven't given the correct change back.")