i = 0
j = 0
while i < 9:  # Outer loop for rows (1 to 9)
    i += 1
    while j < 9:  # Inner loop for columns (1 to 9)
        j += 1
        print(j, "x", i, "=", i * j, " ", end="")  # Print the multiplication result
        if i == j:  # Break the inner loop when row equals column
            j = 0  # Reset `j` for the next row
            print("")  # Print a newline
            break
