def changeme(mylist):
    "Modify the passed list"
    mylist.append([1, 2, 3, 4])  # Add [1, 2, 3, 4] to the list
    print("Value inside the function: ", mylist)
    return

mylist = [10, 20, 30]  # Initialize a list with values
changeme(mylist)  # Call the function and pass the list to it
print("Value outside the function: ", mylist)  # Print the list after function execution
