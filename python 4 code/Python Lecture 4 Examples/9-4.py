With open('testfile.txt', 'r') as file:    # Open an existing file named "testfile.txt" in read-only mode.
line = file.readline()        # Read one line.
print(line)                # Output the line.
print('*' * 30)                # Output 30 asterisks for separation.
line = file.readline(10)        # Read the next line's first 10 characters.
print(line)                # Output the line.
