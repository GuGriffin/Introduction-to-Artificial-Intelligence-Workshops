a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Define a 3x3 matrix
result1 = 0  # Sum of the main diagonal
result2 = 0  # Sum of the secondary diagonal (excluding overlap with the main diagonal)

for i in range(3):  # Loop through the rows
    for j in range(3):  # Loop through the columns
        if i == j:  # Main diagonal condition
            result1 += a[i][j]
        if i + j == 2 and i != j:  # Secondary diagonal, avoiding overlap
            result2 += a[i][j]

print("The sum of the two diagonals is:", result1 + result2)  # Print the total
