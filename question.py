# asking for input

print("\n")

name = input("Please enter your name: ")
print("\nHello " + name.title() + "!")

print("\n")

# making the prompt several lines long
prompt = "If you tell use who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello " + name.title() + "!")

print("\n")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride.")
else:
    print("\nGrow up some more and watch from the sidelines!")

print("\n")
