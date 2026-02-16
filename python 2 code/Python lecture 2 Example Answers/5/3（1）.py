result = ""  # Initialize an empty string to store the result
myStr = input("Please enter a string: ")  # Prompt the user to input a string
arr = list(myStr)  # Convert the string into a list of characters
last = arr[-1]  # Get the last character of the list
arr.insert(0, last)  # Insert the last character at the beginning of the list

for new in arr:  # Iterate through the modified list
    result = result + new  # Append each character to the result string

print(result[:-1])  # Print the result string excluding the last character
