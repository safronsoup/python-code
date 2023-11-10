# continue

current_number = 0

while current_number < 10:
    current_number += 1

# if modulo of 2 == 0 then ingonre (continue) the rest of the loop and
# return to the while statement
    if current_number % 2 == 0:
        continue

# print odd numbers
    print(current_number)
