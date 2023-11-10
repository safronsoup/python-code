# movie theater tickets

prompt = "\nTell me your age and I will tell you the price of the movie."
prompt += "\nEnter 'quit' when finished.\n"

active = True

while active:
    message = input(prompt)
    if message == 'quit':
#        break
        active = False
    elif int(message) < 3:
        print("\nChildren under 3 are free.")
    elif (int(message) >= 3) and (int(message) <= 12):
        print("\nThe price of a movie ticket is $10.")
    else:
        print("\nThe price of a movie ticket is $15.")
