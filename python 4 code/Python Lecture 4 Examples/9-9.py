With open('seek.txt', 'rb') as file:  #create a new file and open it in read-write mode
file.seek(-2, 2)  #position the file pointer to the second-to-last character
con = file.read(1)  #read 1 character into con
print(con)  #output
