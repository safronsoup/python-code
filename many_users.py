# dictionary in a dictionary

print("\n")

users = {
    'aeinstein':
        {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton'},
    'mcurie':
        {'first_name': 'marie', 'last_name': 'curie', 'location': 'paris'},
    'jslaven':
        {'first_name': 'jeff', 'last_name': 'lavender', 'location': 'germany'},
}

# Loop through dictionary users and for each key (login), store the value
# (a dictionary) in user_info. Print each key (login) and concatinate the varialbles
# assigned to keys first_name and last_name and store it in a varialble (full_name).
# Store the value (location) in variable (location) and print it as well.
for login, user_info in users.items():
    print("Username: " + login)
    full_name  = user_info['first_name'] + " " + user_info['last_name']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

print("\n")
