def minimal(x, y):  # Define a function to find the minimum of two values
    if x > y:  # If x is greater than y
        return y  # Return y (the smaller value)
    else:  # Otherwise, x is smaller or equal to y
        return x  # Return x (the smaller value)

a = float(input('Enter the first number: '))  # Prompt the user for the first number
b = float(input('Enter the second number: '))  # Prompt the user for the second number

c = minimal(a, b)  # Call the function with a and b, and assign the result to c

print('The smaller value is:', c)  # Print the smaller value
