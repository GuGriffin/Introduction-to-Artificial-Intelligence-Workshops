def prime(i):  # Define function to check if i is a prime number
    if i <= 1:  # If i is less than or equal to 1, return 0 (i is not prime)
        return 0
    if i == 2:  # If i is 2, return 1 (i is prime)
        return 1
    for j in range(2, i):  # Check if i is divisible by any number less than i
        if i % j == 0:  # If i can be divided by j with no remainder
            return 0  # i is not prime
        elif i != j + 1:  # If i is not equal to j + 1, continue checking
            continue
        else:
            return 1  # If none of the above, i is prime

n = 0
for i in range(6, 21, 2):  # Loop through even numbers from 6 to 20
    k = 2
    while k <= i / 2:  # Check all numbers up to half of i
        j = i - k
        flag1 = prime(k)  # Check if k is prime
        if flag1:  # If k is prime
            flag2 = prime(j)  # Check if j is prime
            if flag2:  # If both k and j are prime
                print(i, '=', k, '+', j)  # Output the result
                n += 1
        k = k + 1
