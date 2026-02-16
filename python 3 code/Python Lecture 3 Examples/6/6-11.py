data = {
    'England': {
        'London': {
            'Islington': ['', 'Test'],
            'Camden': ['', 'We Love Camden']
        },
        'Manchester': {
            'Salford': ['', ''],
            'Deansgate': ['', ''],
            'Didsbury': ['', '']
        },
        'Birmingham': {},
    },
    'Wales': {
        'Cardiff': {},
        'Swansea': {},
        'Newport': {},
    },
    'Scotland': {
        'Edinburgh': {},
        'Glasgow': {},
        'Aberdeen': {},
    },
    'Northern Ireland': {
        'Belfast': {},
        'Londonderry': {},
    },
}

while True:
    for i in data:  # Print the list of regions
        print(i)
    choice = input("Please select a region (press 'q' to quit): ")
    if choice in data:  # If it's in the region list, enter the city level
        while True:
            for i2 in data[choice]:  # Print the list of cities
                print(i2)
            choice2 = input("Please select a city (press 'q' to quit, 'b' to return to region list): ")
            if choice2 in data[choice]:  # If it's in the city list, enter the district level
                while True:
                    for i3 in data[choice][choice2]:  # Print the list of streets
                        print(i3)
                    choice3 = input("Please select a street (press 'q' to quit, 'b' to return to city list): ")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("\nYou have reached the last level (press 'q' to quit, 'b' to return to street list): ")
                        if choice4 == 'b':
                            continue
                        elif choice4 == 'q':
                            exit()
                    elif choice3 == 'b':  # Return to the city level from the street level
                        break
                    elif choice3 == 'q':
                        exit()
            elif choice2 == 'b':  # Return to the region level from the city level
                break
            elif choice2 == 'q':
                exit()
    elif choice == 'q':
        exit()
