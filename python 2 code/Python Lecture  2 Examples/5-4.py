list_1 = [1, 2, 3]  # Create list_1 and assign values
list_2 = [4, 5, 6]  # Create list_2 and assign values
list_3 = [7, 8, 9]  # Create list_3 and assign values
# Append list_2 as a single element (a sublist) to list_1
list_1.append(list_2)
print(list_1)  # Output the modified list_1
# Extend list_2 by adding elements of list_3 to it
list_2.extend(list_3)
print(list_2)  # Output the modified list_2


