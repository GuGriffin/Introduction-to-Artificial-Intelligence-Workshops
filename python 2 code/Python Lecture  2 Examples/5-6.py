x = ['123', 'abc', 'xyz', 'abc', 'python']  # Create a list x with values
while 'abc' in x:  # Loop until 'abc' is no longer in the list
    x.remove('abc')  # Remove the first occurrence of 'abc' from the list
print(x)  # Print the updated list
