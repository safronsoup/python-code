
import os

os.system('clear')

# control structures can be iterated or ended early
# break
# continue
# else (looping)
# pass (do nothing)

for x in range(0,10):
    print("Value of x: ", x)

    # stop for loop if x = 5
    if x == 5:
        break

print("This is the end of my first code block.")

for x in range(0,10):
    print("Value of x: ", x)
    
    # ask user if they want the code to end 
    answer = input("Press y and enter to end this loop. ")
    if answer == "y" or answer == "Y":
        break


x = 10
y = 13

while x < y:
    print("The value of x is: ", x)
    answer = input("Press y to continue this loop. ")
    
    if answer == "y":
        continue # go back to while loop (don't increment x); causes while loop to iterate early
    
    x += 1

print("This is the end of my second code block.")

x = 20
y = 23

while x < y:
    print("The value of x is: ", x)
    answer = input("Press y to stop this loop. ")
    
    if answer == "y":
        break
    
    x += 1
else: # runs at the natural end of the while loop
    print("This is the end of my third code block.")

print("This is tne end of my code.")


# use "pass" when you will add code later:
# if answer == "y":
#   pass