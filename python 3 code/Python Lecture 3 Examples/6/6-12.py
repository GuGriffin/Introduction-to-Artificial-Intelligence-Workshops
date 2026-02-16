data = {
    'England': {
        'London': {
            'Heathrow': ['Heathrow Airport', 'London Eye'],
            'Covent Garden': ['Royal Opera House', 'Covent Garden Market']
        },
        'Manchester': {
            'Salford': ['MediaCityUK', 'Lowry Theatre'],
            'Deansgate': ['Manchester Arena', 'The Shambles']
        }
    },
    'Scotland': {
        'Edinburgh': {
            'Princes Street': ['Edinburgh Castle', 'National Gallery'],
            'Leith': ['Royal Yacht Britannia', 'Ocean Terminal']
        },
        'Glasgow': {
            'Buchanan Street': ['Kelvingrove Art Gallery', 'Buchanan Galleries'],
            'Merchant City': ['Glasgow Cathedral', 'The Sharmanka Kinetic Theatre']
        }
    },
    'Wales': {
        'Cardiff': {
            'Cardiff Bay': ['Wales Millennium Centre', 'Techniquest'],
            'City Centre': ['Cardiff Castle', 'Principality Stadium']
        },
        'Swansea': {
            'Swansea Marina': ['Swansea Waterfront Museum', 'National Waterfront Museum'],
            'Gower Peninsula': ['Rhossili Bay', 'Three Cliffs Bay']
        }
    }
}

while True:
    for i in data:  # Print the first level of the list (regions)
        print(i)
    choice = input("Please select a region (press 'q' to quit):")
    if choice in data:  # If it's in the region list, proceed to the second level (cities)
        while True:
            for i2 in data[choice]:  # Print the second level of the list (cities)
                print(i2)
            choice2 = input("Please select a city (press 'q' to quit, 'b' to return to regions list):")
            if choice2 in data[choice]:  # If it's in the city list, proceed to the third level (areas)
                while True:
                    for i3 in data[choice][choice2]:  # Print the third level of the list (areas)
                        print(i3)
                    choice3 = input("Please select an area (press 'q' to quit, 'b' to return to city list):")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("You have reached the last level (press 'q' to quit, 'b' to return to area list):")
                        if choice4 == 'b':
                            continue
                        elif choice4 == 'q':
                            exit()
                    elif choice3 == 'b':  # Return to the city level from the area level
                        break
                    elif choice3 == 'q':
                        exit()
            elif choice2 == 'b':  # Return to the region level from the city level
                break
            elif choice2 == 'q':
                exit()
    elif choice == 'q':
        exit()
