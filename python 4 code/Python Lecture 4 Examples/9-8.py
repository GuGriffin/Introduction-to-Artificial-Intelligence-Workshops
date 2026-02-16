filename = input('Please input the name of the new file:')    #input file name
with open(filename, 'w+') as file:                #create a new file and open it in read-write mode file.write('This is a test! ')                #Write the string to the file
file.seek(10)                            #Move the pointer to the 10th character from the beginning
con = file.read(4)                        #Read 4 characters into con
print(con)                                #Output
