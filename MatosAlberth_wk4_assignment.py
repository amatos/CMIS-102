# This Python program:
#   This program calculates the cost of a house cleaning service.
# Inputs are:
# Types of cleaning: floors, windows, dusting
# Number of bedrooms, large, medium or small.
# Number of bathrooms
# Number of "other" rooms, large medium or small
#
# Room size definitions:
# Small - 100 sq_ft
# medium - 225 sq_ft
# large - >225 sq_ft

# Alberth Matos
# 06/06/2023
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/13/2023'
CLASS = 'CMIS 102'  # n.b. class (all lowercase) is a reserved named

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
    cost_total_kitchen = 0
    cost_total_windows = 0
    cost_total_bathrooms = 0

    # Get house information
    print('Welcome to the price calculator')
    print('Please enter all values as integers unless otherwise noted.\n')

    # Call get_rooms to get the count of rooms.  get_rooms requires a string to label the type of room and
    # always returns an int
    print('Please enter the number of bedrooms.')
    bedrooms = get_rooms('bedrooms')
    bedrooms_list = get_room_size('bedrooms', bedrooms)
    bedrooms_list = dust_rooms('bedrooms', bedrooms_list)
    print('Please enter the number of bathrooms')
    bathrooms = get_rooms('bathrooms')
    print('Is there a kitchen that needs to be cleaned?')
    # If one of the other rooms is a kitchen, find out.  We charge a flat rate for kitchens
    clean_kitchen = kitchen()
    print('Please enter the number of other rooms (living room, dining room, etc)')
    other_rooms = get_rooms('other rooms')
    other_rooms_list = get_room_size('other rooms', other_rooms)
    other_rooms_list = dust_rooms('other rooms', other_rooms_list)

    window_count = get_windows()

    cost_small_rooms, cost_medium_rooms, cost_large_rooms, cost_dusted_rooms = cost_by_room(bedrooms_list,
                                                                                            other_rooms_list)
    count_small_rooms, count_medium_rooms, count_large_rooms, count_dusted_rooms = count_total_rooms(bedrooms_list,
                                                                                                     other_rooms_list)

    # Add everything up
    # Flat charge for a kitchen
    if clean_kitchen:
        cost_total_kitchen = KITCHEN

    # Flat charge per window
    if int(window_count) > 0:
        cost_total_windows = int(window_count) * WINDOW

    # Flat charge per bathroom
    if int(bathrooms) > 0:
        cost_total_bathrooms = int(bathrooms) * BATHROOM

    # Add up total cost for all the work
    total = cost_small_rooms + cost_medium_rooms + cost_large_rooms + cost_dusted_rooms + cost_total_kitchen \
            + cost_total_bathrooms + cost_total_windows

    # Print out a summary
    print('Summary:\n_______')
    print(f'Subtotal for small rooms: {count_small_rooms} @ {cost_small_rooms}')
    print(f'Subtotal for medium rooms: {count_medium_rooms} @ {cost_medium_rooms}')
    print(f'Subtotal for large rooms: {count_large_rooms} @ {cost_large_rooms}')
    print(f'Total rooms that need to be dusted: {count_dusted_rooms} @ {cost_dusted_rooms}')
    if clean_kitchen:
        print(f'Subtotal for cleaning the kitchen: {cost_total_kitchen}')
    if int(window_count) > 0:
        print(f'Subtotal for window cleaning: {window_count} @ {cost_total_windows}')
    if int(bathrooms) > 0:
        print(f'Subtotal for window cleaning: {bathrooms} @ {cost_total_bathrooms}')
    print('-'*24)
    print(f'Total: ${total}')


def get_room_size(room_type: str, room_count: int):
    room_sizes = {}
    if room_count > 0:
        for x in range(int(room_count)):
            room_sq_ft = input(f'Please enter the rough square footage of {room_type} number {x + 1}: ')
            while not room_sq_ft.isdigit():
                print(f'{room_sq_ft} is not a valid integer.')
                room_sq_ft = input(f'Please enter the rough square footage of {room_type} number {x + 1}: ')
            room_sizes[x] = room_sq_ft
    return room_sizes


def get_rooms(room_type: str):
    rooms = input(f'Number of {room_type}: ')
    # Check if inputted value is an int.  Loop until an integer is entered.
    while not rooms.isdigit():
        print(f'{rooms} is not a valid integer.')
        rooms = input(f'Please enter the number of {room_type}: ')
    rooms = int(rooms)
    return rooms


def dust_rooms(room_type: str, rooms: dict):
    for room in rooms:
        # We charge a flat fee _per room_ to dust, so we only care if we need to dust or not.
        dust_room = input(f'Do we dust {room_type} {room + 1}? (y or n) ')
        while dust_room not in ('Y', 'y', 'n', 'N'):
            print('Please enter either Y or N.')
            dust_room = input(f'Do we dust {room_type} {room + 1}? (y or n) ')
        if dust_room.lower() in 'y':
            rooms[room] = (rooms[room], True)
        else:
            rooms[room] = (rooms[room], False)
    return rooms


def kitchen():
    clean_kitchen = input(f'Do we clean a kitchen? (y or n) ')
    while clean_kitchen not in ('Y', 'y', 'n', 'N'):
        print('Please enter either Y or N.')
        clean_kitchen = input(f'Do we clean a kitchen? (y or n) ')
    if clean_kitchen.lower() in 'y':
        return True
    else:
        return False


def get_windows():
    window_count = input('Please enter the total number of windows to be cleaned: ')
    while not window_count.isdigit():
        print(f'{window_count} is not a valid integer.')
        window_count = input('Please enter the number of windows to be cleaned: ')
    return window_count


def cost_by_room(bedrooms: dict, other_rooms: dict):
    small_bedrooms, medium_bedrooms, large_bedrooms, dusted_bedrooms = count_rooms(bedrooms)
    small_other_rooms, medium_other_rooms, large_other_rooms, dusted_other_rooms = count_rooms(other_rooms)
    small_rooms = (small_bedrooms + small_other_rooms) * SMALL
    medium_rooms = (medium_bedrooms + medium_other_rooms) * MEDIUM
    large_rooms = (large_bedrooms + large_other_rooms) * LARGE
    dusted_rooms = (dusted_bedrooms + dusted_other_rooms) * DUST
    return small_rooms, medium_rooms, large_rooms, dusted_rooms


def count_total_rooms(bedrooms: dict, other_rooms: dict):
    small_bedrooms, medium_bedrooms, large_bedrooms, dusted_bedrooms = count_rooms(bedrooms)
    small_other_rooms, medium_other_rooms, large_other_rooms, dusted_other_rooms = count_rooms(other_rooms)
    small_rooms = small_bedrooms + small_other_rooms
    medium_rooms = medium_bedrooms + medium_other_rooms
    large_rooms = large_bedrooms + large_other_rooms
    dusted_rooms = dusted_bedrooms + dusted_other_rooms
    return small_rooms, medium_rooms, large_rooms, dusted_rooms


def count_rooms(rooms: dict):
    total_small_rooms = 0
    total_medium_rooms = 0
    total_large_rooms = 0
    total_dusted = 0
    for room in rooms:
        size = rooms[room][0]
        dust = rooms[room][1]
        if int(size) <= SMALL_ROOM:
            total_small_rooms = total_small_rooms + 1
        elif (int(size) > SMALL_ROOM) and (int(size) <= MEDIUM_ROOM):
            total_medium_rooms = total_medium_rooms + 1
        else:
            total_large_rooms = total_large_rooms + 1
        if dust:
            total_dusted = total_dusted + 1
    total_small_rooms = total_small_rooms
    total_medium_rooms = total_medium_rooms
    total_large_rooms = total_large_rooms
    total_dusted = total_dusted
    return total_small_rooms, total_medium_rooms, total_large_rooms, total_dusted


main()
