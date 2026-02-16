num = 1  # Initialize a global variable

def fun():
    global num  # Declare 'num' as a global variable using the 'global' keyword
    num += 1  # Increment the global variable 'num' by 1
    print('Inside function, num is:', num)

fun()  # Call the function
print('Outside function, num is:', num)  # Print the value of 'num' outside the function
