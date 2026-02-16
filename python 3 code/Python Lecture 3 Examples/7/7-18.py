import test  # Import the test module

a = float(input('Enter the first number: '))  # Input the value of a
b = float(input('Enter the second number: '))  # Input the value of b

c = test.minimal(a, b)  # Call the function to assign the smaller value to c

print('The smaller value is:', c)  # Output the value of c
