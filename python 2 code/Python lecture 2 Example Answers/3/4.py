for i in range(10):  # Loop to iterate through rows (0 to 9)
    for j in range(0, 10 - i):  # Loop to print leading spaces
        print(end=" ")
    for k in range(10 - i, 10):  # Loop to print stars
        print("*", end=" ")
    print("")  # Print a newline after each row
