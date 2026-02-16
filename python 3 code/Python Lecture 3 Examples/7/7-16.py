def outer():
    num = 1  # Initialize 'num' within the outer function

    def inner():
        nonlocal num  # Declare 'num' as a nonlocal variable, meaning it refers to the 'num' in the outer function
        num = 2  # Modify the 'num' variable in the outer function
        print('In the inner function, num is:', num)

    inner()  # Call the inner function
    print('In the outer function, num is:', num)

outer()  # Call the outer function
