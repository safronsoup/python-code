# sort a list of items
unsorted_list = ['bike', 'car', 'room', 'truck', 'coffee', 'pencil', 'pen', 'zebra']
print("\nThis is an unsorted list.")
print(unsorted_list)

# sort the unsorted_list
unsorted_list.sort()
print("\nThis is a sorted list.")
print(unsorted_list)

# sort list in reverse alphabetical order
unsorted_list = ['bike', 'car', 'room', 'truck', 'coffee', 'pencil', 'pen', 'zebra']
print("\nStart over.")
print(unsorted_list)

unsorted_list.sort(reverse=True)
print("\nThis is a reverse alphabetical sorted list.")
print(unsorted_list)

# print unsorted list, then sort the list, but keep original unsorted_list
unsorted_list = ['bike', 'car', 'room', 'truck', 'coffee', 'pencil', 'pen', 'zebra']
print("\nUnsorted list again.")
print(unsorted_list)

# sorted list
print("\nThis is a sorted list.")
print(sorted(unsorted_list))

# reverse sorted unsorted_list
print("\nThis is a reverse sorted list.")
print(sorted(unsorted_list, reverse=True))

# original unsorted unsorted_list
print("\nThis is the original unsorted list.")
print(unsorted_list)

# print a list in reverse order
big_list = ['dog', 'cat', 'rat', 'elefant', 'giraffe', 'picachu', 'crocadile', 'zebra']
print("\nThis is a new, unsorted list.")
print(big_list)
big_list.reverse()
print("\nThis is an unsorted list printed in reverse order.")
print(big_list)

# show the length of the new big_list
print("\nThe length of the new, unsorted list named big_list is: ")
print(len(big_list))

# show the length of the unsorted_list
print("\nThe length of the first unsorted list named unsorted_list is: ")
print(len(unsorted_list))

# print the last item in big_list
print("\nThe last item in big_list is " + big_list[-1] + ".")
print("\nThe last item in unsorted_list is " + unsorted_list[-1] + ".")
