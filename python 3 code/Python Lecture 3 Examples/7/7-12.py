def fac(k):  # Define the fac function to calculate the factorial
    i = 2
    t = 1
    while i <= k:
        t *= i
        i = i + 1
    return t  # Return the factorial result

def sum(n):  # Define the sum function to calculate the cumulative sum
    s = 0
    i = 1
    while i <= n:
        s = s + fac(i)  # Call the fac function
        i += 1
    return s  # Return the cumulative sum

print('1!+2!+3!…10! =', sum(10))  # Call the sum function
