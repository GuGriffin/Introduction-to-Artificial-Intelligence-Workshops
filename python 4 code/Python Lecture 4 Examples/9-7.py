With open('testfile.txt', 'r') as file:    # Open an existing file named "testfile.txt" in read-only mode.
line = file.read(8)            # Read the first 8 bytes of the file.
print(line)                # Output the first 8 bytes.
p = file.tell()                # Get the current position of the file pointer.
print('Current position:', p)    # Output the current position.
line = file.read(4)            # Read the next 4 bytes of the file.
print(line)                # Output the new data read.
p = file.tell()                # Get the current position of the file pointer.
print('Current position:', p)    # Output the current position.
