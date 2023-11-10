# pizza toppings

prompt = "\nWhat kind of pizza toppings do you want?"
prompt += "\nEnter 'quit' when finished with your toppings. \n"

action = True

while action:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("\nI'll add " + message + " to your pizza.")
