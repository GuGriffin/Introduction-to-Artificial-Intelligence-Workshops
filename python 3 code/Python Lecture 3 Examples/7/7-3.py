def demo(s):  # Define a function
    a = 0  # Variable a is used to store the count of uppercase letters
    b = 0  # Variable b is used to store the count of lowercase letters
    for ch in s:  # Loop through each character in the string
        if ch.isupper():  # Check if the character is an uppercase letter
            a += 1  # If it is, increment a
        elif ch.islower():  # Check if the character is a lowercase letter
            b += 1  # If it is, increment b
    return a, b  # Return the counts of uppercase and lowercase letters

s = input('Please enter a string: ')  # Prompt the user for input
c = demo(s)  # Call the function and store the result in c
print(c, type(c))  # Print the result tuple and its type
print('Number of uppercase letters:', c[0], 'Number of lowercase letters:', c[1])  # Print the results
