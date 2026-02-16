new_str = "This    is     a           python                             book!"  # Create a string with extra spaces
s_str = new_str.split()  # Split the string by any whitespace (spaces, tabs, etc.)
print(s_str)  # Output the result of the split operation
j_str = ' '.join(s_str)  # Join the list of words with a single space between them
print(j_str)  # Output the string after joining the words with a single space
