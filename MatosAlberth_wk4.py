# This Python program:
#   Calculate the number of sprockets in a shipping container, give the number of sprockets per box and boxes
#   per shipping container.

# Alberth Matos
# 06/12/2023
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/12/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named


def calculate_sprockets(sprock_per_box: int, box_per_container:int):
    return (sprock_per_box * box_per_container)

def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    print('Sprocket shipping calculator')
    sprockets = input('Please enter the number of sprockets per box: ')
    while not sprockets.isdigit():
        print(f'{sprockets} is not a valid integer.')
        sprockets = input('Please enter the number of sprockets per box: ')
    boxes = input('Please enter the number of boxes: ')
    while not boxes.isdigit():
        print(f'{boxes} is not a valid integer.')
        boxes = input('Please enter the number of boxes: ')

    total_sprockets = calculate_sprockets(int(sprockets), int(boxes))

    print(f'Each shipping container will hold {total_sprockets} sprockets, consisting of:')
    print(f'{boxes} boxes at {sprockets} sprockets per box')

main()