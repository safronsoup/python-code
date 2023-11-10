# using flags in a while loop as one or many conditions to stop a while loop

prompt = "\nTell me something and I will repeat it to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True

# this while loop prints anything the user enters; without the if statement,
# the word 'quit' is printed
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
        print("\nGame over!")
    else:
        print(message)
