With open('testfile.txt', 'r') as file1, open('copy.txt', 'w') as file2:  # open two files
file2.write(file1.read())  # write the content read from 'testfile.txt' to 'copy.txt'
