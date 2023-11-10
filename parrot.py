# user quits when he wants

prompt = "\nTell me something and I will repeat it to you: "
prompt += "\nEnter 'quit' to end the program. "

# initalize message with an empty string so phyton has something to check
# the first time it reaches the while loop
message = ""

# this while loop prints anything the user enters. without the if statement,
# the word 'quit' is printed
while message != 'quit':
    message = input(prompt)
#   doesn't allow the word 'quit' to be printed
    if message != 'quit':
        print(message)
