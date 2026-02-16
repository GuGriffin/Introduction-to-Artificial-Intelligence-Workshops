total = 0  # Global variable total

def sum(arg1, arg2):  # Function to return the sum of two arguments
    total = arg1 + arg2  # Local variable total
    print("Inside function, local variable: ", total)  # Output the value of the local variable total
    return total

sum(10, 20)  # Call the sum function
print("Outside function, global variable: ", total)  # Output the value of the global variable total
