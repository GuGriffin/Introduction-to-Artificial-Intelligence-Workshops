import os                        # Import the os module
dir_list = os.listdir('ostest')        # Call the listdir() method to return a list of files in the 'ostest' directory
i = 1                            # Initialize i to 1
os.chdir('ostest')                # Change the current working directory to the 'ostest' directory
for name in dir_list:                # Loop through the list
print(name)                # Print the original file name
new_name = str(i) + name    # Add a number to the beginning of the file name for
