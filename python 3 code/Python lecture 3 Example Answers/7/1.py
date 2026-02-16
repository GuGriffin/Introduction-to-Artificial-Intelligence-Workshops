def demo(m, n):  # Calculate GCD and LCM
    p = m * n  # Multiply the two numbers to find LCM
    while m % n != 0:  # Use Euclidean algorithm to find GCD
        m, n = n, m % n  # Swap m and n
    return (n, p // n)  # Return GCD (n) and LCM (product divided by GCD)

a = int(input('Enter the first integer: '))  # Prompt user for the first integer
b = int(input('Enter the second integer: '))  # Prompt user for the second integer
c = demo(a, b)  # Call the demo function to get GCD and LCM
print(c)  # Print the result as a tuple (GCD, LCM)
