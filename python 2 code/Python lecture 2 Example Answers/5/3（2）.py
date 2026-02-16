myStr = input("Please enter a string: ")  # Prompt the user to input a string
last = myStr[-1]  # Get the last character of the string
print(last + myStr[:-1])  # Print the last character followed by the rest of the string (excluding the last character)
