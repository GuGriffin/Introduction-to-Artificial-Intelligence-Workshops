a = 15  # Define variable 'a' and assign value
b = 12345678.1234567  # Define variable 'b' and assign value
strs = "I love Python!"  # Define string 'strs' and assign value
# Use the m format specifier to control the number of digits; fill with 0 if needed
print("a=%05d" % a)  # Outputs 'a' with 5 digits, padded with leading zeros
# Use m.n format specifier to control total length and decimal places
print("b=%8.3f" % b)  # Outputs 'b' with 8 characters wide and 3 decimal places
# Use m format specifier to control the width of the string output
print("%17s" % strs)  # Outputs 'strs' with a width of 17 characters, right-aligned
# Use %r to output the string with quotes and special characters if any
print("%17r" % strs)  # Outputs 'strs' with a width of 17 characters, with the representation
# Use -m.n to left-align the string and limit the length to 5 characters
print("%-17.5s" % strs)  # Outputs 'strs' left-aligned, limited to 5 characters
