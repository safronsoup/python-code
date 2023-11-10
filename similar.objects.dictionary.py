# dictionary of similar objects
print("\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', # add comma in case more items will be added later
    }

print(favorite_languages)
print("Sarah's favorite language is " + favorite_languages['sarah'].title() +
    ".")
print("Jen's favorite language is " + favorite_languages['jen'].title() +
    ".")

print("\n")

employee_1 = {
    'first_name': 'jen',
    'last_name': 'mckenzie',
    'street_address': '308 Blackball Street',
    'city': 'austin',
    'state': 'tx',
    'zip_code': 78511,
    'home_phone': '888-347-5166',
    }

#print(employee_1['first_name'].title())
#print(employee_1['last_name'].title())
#print(employee_1['street_address'])
#print(employee_1['city'].title())
#print(employee_1['state'].upper())

employee_2 = {
    'first_name': 'chris',
    'last_name': 'moyhan',
    'street_address': '122 Endless Drive',
    'city': 'oklahoma',
    'state': 'ok',
    'zip_code': 33111,
    'home_phone': '241-918-3133',
    }

print(employee_1)
print("\n")
print(employee_2)
print("\n")

# all_employees = {(employee_1), (employee_2)}
# print(all_employees)
