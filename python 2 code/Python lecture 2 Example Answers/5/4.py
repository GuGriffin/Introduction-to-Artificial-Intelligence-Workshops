arr = [12, 3, 62, 7, 91, 67, 27, 45, 6]  # Define the list
non_primes = []  # List to hold non-prime numbers

for element in arr:
    tag = True  # Assume the number is prime
    # Prime numbers are greater than 1
    if element > 1:
        # Check for factors
        for i in range(2, int(element ** 0.5) + 1):  # Check up to the square root of the number
            if element % i == 0:
                tag = False
                break
    else:
        tag = False  # Numbers less than or equal to 1 are not prime

    if not tag:
        non_primes.append(element)  # Add non-prime numbers to the list

print(non_primes)  # Print the list of non-prime numbers
