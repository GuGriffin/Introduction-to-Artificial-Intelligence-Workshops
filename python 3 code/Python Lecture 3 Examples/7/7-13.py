def f(n):  # Define a recursive function
    if n == 1:  # When n equals 1, return 1
        return 1
    else:  # When n is not 1, return f(n-1) * n
        return f(n-1) * n

n = int(input('Please enter a positive integer: '))  # Input an integer
print(n, 'factorial is:', f(n))  # Call the function f and output the result
