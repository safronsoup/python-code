# number of cars
cars = 100
# number of seats in each car
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# calculates the number of cars not driven
cars_not_driven = cars - drivers
# the number of cars driven equals the number of drivers
cars_driven = drivers
# total amount of passengers that can be taken based on cars driven
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers per number of cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "to carpool today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
