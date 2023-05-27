def Main():
    Name = 'Dracy'
    print('Name:', Name)
    print('CMIS 102/6381\tDate:5/26/23')

    #Display welcome message

    print('\nWelcome to the square footage calculator!')
    print('This program will calculate the square footage of a room')

    #Prompt user to enter legnth and width of room and get user responses

    length = int(input('\nWhat is the legnth of the room?:'))

    width = int(input('What is the width of the room?'))

    #Calculate squareFootage
    squareFootage = length * width

    #Display squareFootage
    print('\nThe square footage is:', squareFootage)

    # Prompt user for height
    height = int(input('What is the height of the room?: '))
    # Calculate volume of the room
    volume = length * width * height
    print(f'The volume of the room is: {volume}')
Main()
