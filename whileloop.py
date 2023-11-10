import os

os.system('clear')

# repetative code is bad
# loops repeat blocks of code multiple times and reduce opportunities for bugs

# indefinite iterator: a while loop
# uses relational operators to test an expression
# a true result cause the code to execute, then RETURN to the while,
# otherwise, execution skip past the loop block

# while <conditional statement> then <looping code to execute>

x = input("At what number do you want to start the countdown? ")

# convert string to integer
x = int(x)

# make a test to see if a character is entered and abort
# if type(x) == str:
#    print("You entered a sting value.")
#    print("Run the program again and enter an integer value.")

if x <= 0:
    print("The countdown can't start at a zero or a negative number. Enter a positive value.")
else:
    while x > 0:
        print(f"Count down: {x}".format(x))
        # count down to ensure while statement will become false
        # x = x - 1
        x -= 1
        # print(x)   
        if x == 0:
            print("Blast off!")

print()
print("This is outside the while loop.")
print()