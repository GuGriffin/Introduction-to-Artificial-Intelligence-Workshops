import time  # Import the time module
scale = 10  # The scale variable represents the precision of the progress bar
print("---------- Execution Started ----------")  # Output
for i in range(scale + 1):  # Loop from 0 to 10
    a = "**" * i  # Use "*" to represent the completed portion
    b = ".." * (scale - i)  # Use "." to represent the unfinished portion
    c = (i / scale) * 100  # Calculate the completion percentage and assign it to c
    print("%{:^3.0f}[{}->{}]".format(c, a, b))  # Formatted output
    time.sleep(0.1)  # Pause for 0.1 seconds
print("---------- Execution Ended ----------")  # Output
