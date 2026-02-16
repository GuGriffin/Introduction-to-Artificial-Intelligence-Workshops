i = 2
while i < 100:  # Loop through numbers from 2 to 99
    j = 2
    while j <= i / j:  # Check divisors up to the square root of the current number
        if not (i % j):  # If `i` is divisible by `j`
            break  # Exit the inner loop, `i` is not a prime number
        j = j + 1
    if j > i / j:  # If no divisors are found, `i` is a prime number
        print(i, "is a prime number")
    i = i + 1
