def getMax():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    # Compare the three numbers to find the maximum
    if num1 >= num2 and num1 >= num3:
        return "The maximum value is: " + str(num1)
    elif num2 >= num1 and num2 >= num3:
        return "The maximum value is: " + str(num2)
    else:
        return "The maximum value is: " + str(num3)


maxValue = getMax()
print(maxValue)
