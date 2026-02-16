ls = ['Environment variables'] # define a list and assign a value
with open('testfile.txt', 'a') as file: # open an existing file named "testfile.txt" in append mode
file.writelines(ls) # append the string list to the file
