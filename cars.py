# working with if statements

print("\n")

cars =['Audi', 'bmw', 'subaru', 'toyota']

# for loop with conditional if-else statements
for car in cars:
    if car.lower() == 'tesla': # case sensivity mattes in Python
        print(car.upper())
    else:
        print(car.title())

print("\n")

# for loop with conditional if-else statements
for car in cars:
    if car.lower() == 'bmw': # case sensivity mattes in Python
        print(car.upper())
    else:
        print(car.title())

print("\n")
