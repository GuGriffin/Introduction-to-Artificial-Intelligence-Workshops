With open('testfile.txt', 'r') as file:    # Open an existing file named "testfile.txt" in read-only mode.
content = file.readlines()        # Read all lines and return a list.
print(content)                    # Output the list.
print('*' * 60)                    # Output 60 asterisks for separation.
for temp in content:                # Iterate through the list.
print(temp)                # Output each element of the list.
