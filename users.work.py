# users at work

# print("\n")

users = {
    'mmathers':
        {'first_name': 'mark', 'last_name': 'mathers', 'job_title': 'engineer',
        'phone_number': '314.434.1234', 'email': 'mmathers@inc.edu'},
    'sjohnson':
        {'first_name': 'saju', 'last_name': 'johnson', 'job_title': 'accountant',
        'phone_number': '314.434.3492', 'email': 'sjohnson@inc.edu'},
    'jslaven':
        {'first_name': 'jeff', 'last_name': 'lavender', 'job_title': 'ip engineer',
        'phone_number': '314.434.5722', 'email': 'jslaven@inc.edu'},
    'bbob':
        {'first_name': 'billy', 'last_name': 'bob', 'job_title': 'project manager',
        'phone_number': '314.434.8891', 'email': 'bbob@inc.edu'},
}
# print out each username and their information

for name, user_info in users.items():
    first_name = user_info['first_name'].title()
    print("\n" + first_name + " is a " + user_info['job_title'] + ".")
    print("You can reach " + first_name + " at DSN " +
        user_info['phone_number'] + ".")

print("\n")
