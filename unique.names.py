#  unique user names

current_users = ['admin', 'stacey', 'jeff', 'naomi', 'dave', 'rob']

new_users = ['thomas', 'Billy']

for user in new_users:
    if user.lower() in current_users:
        print("\nUsername " + user.lower() + " already exist. Select another one.")
    else:
        print("\nUsername " + user.lower() + " is available.")
print("\n")
