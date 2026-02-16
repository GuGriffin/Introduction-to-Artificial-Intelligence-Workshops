for cock in range(0, 20 + 1):  # The range of "roosters"  is from 0 to 20
    for hen in range(0, 33 + 1):  # The range of "hens"  is from 0 to 33
        for biddy in range(3, 99 + 1):  # The range of "chicks"  is from 3 to 99
            if (5 * cock + 3 * hen + biddy / 3) == 100:  # Check if the total cost equals 100
                if (cock + hen + biddy) == 100:  # Check if the total number of chickens equals 100
                    if biddy % 3 == 0:  # Check if the number of chicks is divisible by 3
                        print("Roosters:", cock, "Hens:", hen, "Chicks:", biddy)  # Output the solution
