def dec2bin(num):
    l = []  # List to store the binary digits
    if num < 0:  # If the number is negative
        return '-' + dec2bin(abs(num))  # Recursively convert the absolute value and add a negative sign
    while True:
        num, remainder = divmod(num, 2)  # Divide the number by 2 and get the remainder
        l.append(str(remainder))  # Append the remainder (binary digit) to the list
        if num == 0:  # If the quotient is zero, the conversion is done
            return ''.join(l[::-1])  # Join and reverse the list to get the binary number
dec = int(input("Enter a decimal number: "))  # Input a decimal number
print("Binary number is:", dec2bin(dec))
