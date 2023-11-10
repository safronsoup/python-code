# favorite places

favorite_places = {
    'tom': ['blue ridge mountains', 'carolina beach', 'home'],
    'bev': ['myrtle beach', 'northern va', 'europe'],
    'jeff': ['biscarose', 'sevilla', 'amsterdam']
}

# person is the key, place is the value (a list of items)
for person, place in favorite_places.items():
    print("\n" + person.title() + " like to visit: ")
# go through each location in each list (place) and print it out
    for location in place:
        print(location.title())
