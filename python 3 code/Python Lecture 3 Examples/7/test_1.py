def minimal(x, y):  # Define a function to compute the smaller value between x and y
    if x > y:  # If x is greater than y, return y
        return y
    else:  # Otherwise, return x
        return x

# Used for testing
if __name__ == '__main__':  # Check if the script is being run directly
    r = minimal(2, 3)  # Call the minimal function with arguments 2 and 3
    print('The smaller value between 2 and 3 is:', r)  # Output the result
