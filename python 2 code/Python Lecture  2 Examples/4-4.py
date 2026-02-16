a = 15  # Define variable 'a' and assign value
b = 12345678.1234567  # Define variable 'b' and assign value
strs = "I love Python!"  # Define string 'strs' and assign value
# Use the format method to output 'a' with 5 digits, padded with leading zeros
print("a={0:05}".format(a))  # Outputs 'a' as a 5-digit number, padded with 0s
# Output 'b' with thousand separators and 3 decimal places
print("b={0:,.3f}".format(b))  # Outputs 'b' with thousands separator and 3 decimal places
# Center 'strs' within 30 characters, filling with '*' symbols
print("{0:*^30}".format(strs))  # Outputs 'strs' centered within 30 characters, with '*' padding
