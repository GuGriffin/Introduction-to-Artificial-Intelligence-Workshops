X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]  # Define matrix X
Y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]   # Define matrix Y
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Define an empty result matrix of the same size

# Iterate through the rows of matrix X
for i in range(len(X)):
    # Iterate through the columns of matrix X
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]  # Add corresponding elements of X and Y and store in result

# Output the result matrix
for r in result:
    print(r)
