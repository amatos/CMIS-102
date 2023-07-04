# This Python program:
#   Create a Python program that populates an array variable (containing at least five elements) within a loop using
#   input supplied by the user. It should then perform some modification to each element of the array using a second
#   loop, and then display the modified array in a third loop. Note that there should be only one array, but three loops.

# Alberth Matos
# 07/04/2023
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '07/04/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

def build_array():
    # Initialize empty list
    my_array = []
    number_elements = input('Please enter the number different types of gems (integers only, please): ')
    # If number_elements isn't a digit, loop until we get a digit.
    while not number_elements.isdigit():
        print(f'Please enter a digit.  {number_elements} is not a digit.')
        number_elements = input('Please enter the number different types of gems (integers only, please): ')
    # loop through the entered number, asking for the name of each gem
    for counter in range(int(number_elements)):
        # Humans usually count from 1, so add 1 to the counter value when it is printed
        gem = input(f'Please enter gem stone {counter + 1}: ')
        # Append the value to the list.
        my_array.append(gem)
    print('\n')
    return my_array

def get_count_of_items(my_array):
    # Input the quantity of each item in the array, modifying the list item with a dictionary containing:
    #   gem: <gem type>, qty: <quantity>
    # Enumerate the array, pull out the index (as counter) and element (as element).  Then modify the list
    # using the index to add a dictionary containing the capitalized gem name and the quantity.
    for counter, element in enumerate(my_array):
        number_of_element = input(f'Please enter the number of {element.capitalize()}s: ')
        while not number_of_element.isdigit():
            number_of_element = input(f'Please enter an integer for the number of {element.capitalize()}')
        my_array[counter] = {'gem': element.capitalize(), 'qty': int(number_of_element)}
    print('\n')
    # and return the modified array
    return my_array

def return_qty(dictionary):
    # Helper function to return the quantity
    return dictionary['qty']

def print_array(my_array):
    # Sort the array, keyed to the quantity of the given gem.  Sort will be from least to greatest.
    my_array.sort(key=return_qty)
    # Iterate through the array, pull the quantity and gem type, and print it out.
    for element in my_array:
        quantity = element['qty']
        gem = element['gem']
        print(f'You have {quantity} {gem}s')


def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    gem_array = build_array()
    gem_array = get_count_of_items(gem_array)
    print_array(gem_array)
main()