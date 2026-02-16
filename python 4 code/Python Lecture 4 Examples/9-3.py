With open('testfile.txt', 'r') as file:    # Open an existing file named "testfile.txt" in read-only mode.
line = file.read(10)            # Read the first 10 bytes of the file.
print(line)                # Output the first 10 bytes.
print('*' * 30)                # Output 30 asterisks for separation.
content = file.read()            # Read the remaining content of the file.
print(content)                # Output the remaining content.
