n = 1  # Create a variable `n` and assign it a value of 1
S = 0  # Create a variable `S` and assign it a value of 0

while True:  # Infinite loop
    S += n  # Add the value of `n` to `S` (sum up the numbers)
    if S > 10000:  # If `S` becomes greater than 10000
        break  # Exit the loop
    n += 1  # Increment `n` by 1

print("The largest integer n is", n - 1, ", such that 1 + 2 + 3 + ... + n <= 10000.")  # Output the value of `n - 1`
