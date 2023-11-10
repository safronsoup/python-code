#motorcycles = []
#motorcycles.append('indian')
#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('ducati')
#print(motorcycles)

#motorcycles.insert(2, 'bmw')
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)

#first_owned = motorcycles.pop(0)
#print('The first motorcycles I owned was a ' + first_owned.title() + '.')
#print(motorcycles)

motorcycles = []
motorcycles.append('indian')
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')
motorcycles.append('bmw')
print(motorcycles)
#motorcycles.remove('ducati')
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me!")

