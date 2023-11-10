# a list in a dictionary

print("\n")
# store information about a pizza being ordered

pizza = { 'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'],}

# summarize order
print("You orderd a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

# print each item in the toppings list in the pizza dictionary
for topping in pizza['toppings']:
    print("\t" + topping)

print("\n")
