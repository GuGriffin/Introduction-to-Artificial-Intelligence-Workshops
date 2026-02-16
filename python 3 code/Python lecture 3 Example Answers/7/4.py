def is_palindrome(n):
    n = str(n)  # Convert the number to a string
    m = n[::-1]  # Reverse the string
    return n == m  # Check if the number is the same as its reverse

a = int(input('Please enter an integer to check: '))  # Input an integer
result = is_palindrome(a)  # Call the function
print(result)  # Output the result (True if palindrome, False otherwise)
