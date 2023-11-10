# movie theater tickets

prompt = "\nTell me your age and I will tell you the price of the movie."
prompt += "\nEnter 'quit' when finished.\n"

message = input(prompt)

while message != 'quit':
    if int(message) < 3:
        print("\nChildren under 3 are free.")
        message = input(prompt)
    elif (int(message) >= 3) and (int(message) <= 12):
        print("\nThe price of a movie ticket is $10.")
        message = input(prompt)
    else:
        print("\nThe price of a movie ticket is $15.")
        message = input(prompt)
