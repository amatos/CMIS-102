# This Python program:
#   This program calculates the cost of a house cleaning service.
# Inputs are:
# Types of cleaning: floors, windows, dusting
# Number of bedrooms, large, medium or small.
# Number of bathrooms
# Number of "other" rooms, large medium or small
#
# Room size definitions:
# Small - 100 sqft
# medium - 225 sqft
# large - >225 sqft

# Alberth Matos
# 06/06/2023
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/06/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

# Constants for cost
SMALL = 50
MEDIUM = 75
LARGE = 100
BATHROOM = 35
KITCHEN = 100
WINDOW = 5
DUST = 5

# Constants for sizes
# We only account for small and medium rooms, because anything that
#  isn't small or medium must therefore be large.
SMALL_ROOM = 100
MEDIUM_ROOM = 150

def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    # Zero all the values
    bathrooms = ''
    bedrooms = ''
    clean_kitchen = False
    cost_total_dusted = 0
    cost_total_kitchen = 0
    cost_total_large_rooms = 0
    cost_total_medium_rooms = 0
    cost_total_small_rooms = 0
    cost_total_windows = 0
    is_kitchen = ''
    other_rooms = ''
    room_dust = ''
    room_sqft = ''
    rooms = list()
    subtotal = 0
    total_dusted = 0
    total_large_rooms = 0
    total_medium_rooms = 0
    total_small_rooms = 0
    window_count = ''

    # Get house information
    print('Welcome to the price calculator')
    print('Please enter all values as integers unless otherwise noted.\n')

    bedrooms = input('Please enter the number of bedrooms : ')
    # Check if inputted value is an int.  Loop until an integer is enterred.
    while not bedrooms.isdigit():
        print(f'{bedrooms} is not a valid integer.')
        bedrooms = input('Please enter the number of bedrooms: ')
    bedrooms = int(bedrooms)

    bathrooms = input('Please enter the number of bathrooms, including half-baths: ')
    # Check if inputted value is an int.  Loop until an integer is enterred.
    while not bathrooms.isdigit():
        print(f'{bathrooms} is not a valid integer.')
        bathrooms = input('PLease enter the number of bathrooms: ')
    bathrooms = int(bathrooms)

    other_rooms = input('Please enter the number of other rooms (kitchen, living room, etc): ')
    # Check if inputted value is an int.  Loop until an integer is enterred.
    while not other_rooms.isdigit():
        print(f'{other_rooms} is not a valid integer.')
        other_rooms = input('Please enter the number of other_rooms: ')
    other_rooms = int(other_rooms)

    # Build a structure to contain the square footage of a bedroom, and whether we are dusting it.


    # This really should be a separate function since I do this twice.
    if bedrooms > 0:
        for x in range(int(bedrooms)):
            room_sqft = input(f'Please enter the rough square footage of bedroom number {x + 1}: ')
            while not room_sqft.isdigit():
                print(f'{room_sqft} is not a valid integer.')
                room_sqft = input('Please enter the number of bathrooms: ')
            # We charge a flat fee _per room_ to dust, so we only care if we need to dust or not.
            room_dust = input(f'Do we dust room {x + 1}? (y or n) ')
            while room_dust not in ('Y','y','n','N'):
                print('Please enter either Y or N.')
                room_dust = input(f'Do we dust room {x + 1}? (y or n) ')
            if room_dust.lower() in 'y':
                room_dust = True
            else:
                room_dust = False
            rooms.append((room_sqft, room_dust))

    # If one of the other rooms is a kitchen, find out.  We charge a flat rate for kitchens
    clean_kitchen = False
    if other_rooms > 0:
        is_kitchen = input('Is one of the remaining rooms a kitchen? ')
        while is_kitchen not in ('Y','y','n','N'):
            print('Please enter either Y or N.')
            is_kitchen = input(f'Is one of the remaining rooms a kitchen?? (y or n) ')
        if is_kitchen.lower() == 'y':
            clean_kitchen = True
            # To make the next section easier, subtract 1 from the other_room count
            # _if_ we are cleaning a kitchen. Since we charge a flat fee for kitchens,
            # we don't need to ask the size and whether it needs to be dusted.
            other_rooms = other_rooms - 1
        # Go through the rest of the other_rooms, if any, and get the size and whether it needs to be dusted.
        if other_rooms > 0:
            print('For the remaining questions in this section, please do not include the kitchen.')
            for x in range(int(other_rooms)):
                room_sqft = input(f'Please enter the rough square footage of room number {x + 1}: ')
                while not room_sqft.isdigit():
                    print(f'{room_sqft} is not a valid integer.')
                    room_sqft = input('PLease enter the number of bathrooms: ')
                # We charge a flat fee _per room_ to dust, so we only care if we need to dust or not.
                room_dust = input(f'Do we dust room {x + 1}? (y or n) ')
                while room_dust not in ('Y','y','n','N'):
                    print('Please enter either Y or N.')
                    room_dust = input(f'Do we dust room {x + 1}? (y or n) ')
                if room_dust.lower() in 'y':
                    room_dust = True
                else:
                    room_dust = False
                rooms.append((room_sqft, room_dust))

    # Get count of windows.  We charge a flat fee for windows
    print('For the remaining questions, please consider all of the rooms.')
    window_count = input('Please enter the total number of windows to be cleaned: ')
    while not window_count.isdigit():
        print(f'{window_count} is not a valid integer.')
        window_count = input('Please enter the number of windows to be cleaned: ')

    # Go through all of the rooms, get their sizes, and whether they are to be dusted
    for room in rooms:
        size, dust = room
        if int(size) <= SMALL_ROOM:
            total_small_rooms = total_small_rooms + 1
        elif (int(size) > SMALL_ROOM ) and (int(size) <= MEDIUM_ROOM):
            total_medium_rooms = total_medium_rooms + 1
        else:
            total_large_rooms = total_large_rooms + 1
        if dust:
            total_dusted = total_dusted + 1

    # Add everything up
    # Total number of small rooms * 50/room
    cost_total_small_rooms = int(total_small_rooms) * SMALL
    # Total number of medium rooms * 75/room
    cost_total_medium_rooms = int(total_medium_rooms) * MEDIUM
    # Total number of large rooms * 100/room
    cost_total_large_rooms = int(total_large_rooms) * LARGE
    # Flat $5 cost to dust a room
    cost_total_dusted = int(total_dusted) * DUST
    # Flat $100 charge to clean a kitchen
    if clean_kitchen:
        cost_total_kitchen = int(KITCHEN)
    # Flat $5 charge per window
    cost_total_windows = int(window_count) * WINDOW
    subtotal = cost_total_windows + cost_total_dusted  + cost_total_kitchen + cost_total_large_rooms + cost_total_medium_rooms + cost_total_small_rooms

    # Print out a summary
    print('Summary:\n_______')
    print(f'Total for small rooms: {total_small_rooms} @ {cost_total_small_rooms}')
    print(f'Total for medium rooms: {total_medium_rooms} @ {cost_total_medium_rooms}')
    print(f'Total for large rooms: {total_large_rooms} @ {cost_total_large_rooms}')
    print(f'Total rooms that need to be dusted: {total_dusted} @ {cost_total_dusted}')
    if clean_kitchen:
        print(f'Total for cleaning the kitchen: {cost_total_kitchen}')
    if int(window_count) > 0:
        print(f'Total for window cleaning: {window_count} @ {cost_total_windows}')
    print('-'*24)
    print(f'Total: ${subtotal}')




main()