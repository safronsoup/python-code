# print a range of numbers - one-off behavior - prints 1-9

# print 1-9
for value in range(1,10):
    print(value)

print("\n")

# print 1-10
for value in range(1,11):
    print(value)

print("\n")

# create a list of numbers using the range function
numbers = list(range(1,6))
print("This is a list of numbers: ", numbers)
print("\n")

# create a list of even numbers from 2-10
even_numbers = list(range(2,11,2))
print("This is a list of even numbers: ", even_numbers)
print("\n")

# create a list of odd numbers from 1-9
odd_numbers = list(range(1,10,2))
print("This is a list of odd numbers: ", odd_numbers)
print("\n")

# create a list of squared numbers from 1-10
# create an empty list to store squared numbers
squared_values = []

# for loop to square the values in range 1-10
for value in range(1,11):
    square = value**2
    squared_values.append(square)

# print the squared values in the list
print("These are the squared values between 1-10: ", squared_values)
print("\n")

# create a list of squared numbers from 1-9
# create an empty list to store squared odd_numbers
odd_squared_values = []

# for loop to square the odd values in range 1-9
for value in range(1,11,2):
    odd_square = value**2
    odd_squared_values.append(odd_square)

# print the odd squared values in the list
print("These are the odd squared values between 1-10: ", odd_squared_values)
print("\n")
print("This is the minimum odd value in the list: ", min(odd_squared_values))
print("This is the maximum odd value in the list: ", max(odd_squared_values))
print("This is the sum of the odd value in the list: ", sum(odd_squared_values))
print("\n")

# list comprehensions - combine for loop and creation of new elements into one line
squared_numbers = [value**2 for value in range(1,11)]
print(squared_numbers)

odd_squared_numbers = [value**2 for value in range(1,11,2)]
print(odd_squared_numbers)

even_squared_numbers = [value**2 for value in range(2,11,2)]
print(even_squared_numbers)

# using a list comprehension to sum numbers 1 - 1000000
sum_one_million = [sum(range(1,1000000))]
print(sum_one_million)

# print numbers 1 - 500000; remember to increase range by one
fht = list(range(1,500001))
#print(fht)
print(min(fht))
print(max(fht))

# list of integers in multiples of 3
mult_three = list(range(3,31,3))
print("List numbers between 1-30 inclusive in multiples of three: ", mult_three)

# cube numbers x^3 using a list comprehension
cubed_numbers = [value**3 for value in range(1,11)]
print("Cubed numbers from 1-10 using a list comprehension:", cubed_numbers)

# cube numbers using a for loop
three_squared = []
for value in range(1,11):
    three_squared.append(value**3)
print("Cubed numbers from 1-10 using a for loop:", three_squared)

print("\n")

# let's practice using slices
# print out the first three elements in the list - last number in [#:#] is one
# higher than what you need
colors = ['red', 'blue', 'green', 'black', 'purple', 'orange']
print(colors)
print("Print the first three colors in list colors: ", colors[0:3])
print("Print items 3-5 colors in list colors: ", colors[2:5])

# start slice at the beginning of the List (0,1,2)
print("Print the first three items in list colors: ", colors[:3])

# start slice at the item 3 of the List (3 to end) (0,1,2, ... 2 is the third item)
print("Print from the third item to the end of list in list colors: ", colors[2:])

# start slice at the right side and print three items
print("Print from the right three in list colors: ", colors[-3:])
print("\n")

# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
