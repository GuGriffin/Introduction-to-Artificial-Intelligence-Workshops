a = int(input("Please enter the value of a: "))  # Input the value of `a` and convert it to an integer
b = int(input("Please enter the value of b: "))  # Input the value of `b` and convert it to an integer
c = int(input("Please enter the value of c: "))  # Input the value of `c` and convert it to an integer

# Compare the values to determine the maximum
if a > b:  # If `a` is greater than `b`
    if a > c:  # If `a` is also greater than `c`, then `a` is the maximum
        max = a
    else:  # If `c` is greater than `a`, then `c` is the maximum
        max = c
else:  # If `b` is greater than or equal to `a`
    if b > c:  # If `b` is also greater than `c`, then `b` is the maximum
        max = b
    else:  # If `c` is greater than or equal to `b`, then `c` is the maximum
        max = c

print("max =", max)  # Output the maximum value
