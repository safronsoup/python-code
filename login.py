# login greetings to users

# list of users
users = ['admin', 'stacey', 'jeff', 'naomi', 'dave', 'rob']

# empty list of  users
# users = []

user = 'admin'
if users:
    for user in users:
        if user == 'admin':
            print("\nHello " + user + ", would like a status report?")
        else:
            print("\nHello " + user.title() + ", thank you for loggin in again.")
else:
    print("\nWe need to find some users!")
