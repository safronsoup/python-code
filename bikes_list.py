# create a blank list

bikes = []

# add make of bikes to bikes list
bikes.append('cannondale')
bikes.append('schwinn')
bikes.append('cannondale')
bikes.append('cannondale')
print(bikes)

# insert another bike into the list
bikes.insert(0, 'ducati')
print(bikes)

# insert another item into the bikes list
bikes.insert(1, 'mbt')
print(bikes)

# print 2nd element of bikes list
print(bikes[1].upper())

# delete first item in bikes list
del bikes[0]
print(bikes)

# pop and use item from bikes list
a_bike = bikes.pop()
print(a_bike)
print("I owned a " + a_bike.title() + " when I was younger!")

print(bikes)

# remove first occurance of item from bikes lists by name and not location

removed_bike = 'cannondale'
bikes.remove(removed_bike)
print(bikes)
