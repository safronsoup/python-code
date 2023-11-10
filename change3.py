import os
os.system("clear")

changeAmt = input("What is the amount of change? ")
changeAmt = int(changeAmt)

coins = [ 25, 10, 5, 1 ]
currency = [ "Quarters", "Dimes", "Nickels", "Pennies" ] 

# initalize the numbers of each coins
coinCounts = [ 0, 0, 0, 0 ]

for i in range(0, len(coins)):
    coinCounts[i] = changeAmt // coins[i]
    changeAmt = changeAmt - (coinCounts[i] * coins[i])
    print(f"The number of {currency[i]} is: {coinCounts[i]}.")


# print(f"Quarters: {coinCounts[0]}")
# print(f"Dimes: {coinCounts[1]}")
# print(f"Nickels: {coinCounts[2]}")
# print(f"Pennies: {coinCounts[3]}")