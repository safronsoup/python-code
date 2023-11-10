# print ordinal number 1-9 with st, rd, th behind each

ordinal_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in ordinal_numbers:
    if int(number) == 1:
        print(number + "st")
    elif int(number) == 2:
        print(number + "nd")
    elif int(number) == 3:
        print(number + "rd")
    elif int(number) > 3:
        print(number + "th")
