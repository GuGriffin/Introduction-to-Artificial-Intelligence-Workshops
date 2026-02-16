def f(n):  # Define recursive function
    if n == 1:  # When n equals 1, return 1
        return 1
    else:  # When n is not 1, return f(n-1) + n
        return f(n - 1) + n

n = int(input('Please enter a positive integer: '))  # Input an integer
print('s = 1 + 2 + … + n =', f(n))  # Call function f and output the result
