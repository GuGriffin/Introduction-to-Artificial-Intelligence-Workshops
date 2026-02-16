for x in range(1, 10):  # Loop with variable `x` ranging from 1 to 9
    for y in range(1, x + 1):  # Loop with variable `y` ranging from 1 to `x + 1`
        print(y, "*", x, "=", x * y, "", end="")  # Print the multiplication expression
    print("")  # Print an empty string to create a newline after each row
