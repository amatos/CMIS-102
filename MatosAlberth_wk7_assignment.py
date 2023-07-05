# This Python program:
#   This week's assignment involves writing a Python program to collect all the data of a road trip and calculate
#   each person's share of the cost. Prompt the user for each of the following:
#
# The number of people on the trip.
# The number of days of the trip.
# For each day of the trip:
# Cost of food.
# Cost of gas.
# The food and gas costs should be stored in two separate arrays. Calculate and display each of the following:
#
# the total cost of each category;
# the total cost of the trip; and
# each person's share of the total cost.

# Alberth Matos
# '07/04/2023'
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '07/04/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

def get_nr_people():
    # Get number of people.  Since people are whole numbers, we only accept integers
    people = input('Please enter the number of people (integer, please): ')
    while not people.isdigit():
        print(f'{people} is not a valid entry.')
        people = input('Please enter an integer for the number of people: ')
    return int(people)

def get_nr_days():
    # Get number of days.  We only care about whole days, so we accept only integers
    days = input('Please enter the number of days (integer, please): ')
    while not days.isdigit():
        print(f'{days} is not a valid entry.')
        days = input('Please enter an integer for the number of days: ')
    return int(days)

def get_total_food(nr_days:int):
    # Build a list of food expenditures per day
    day_food = []
    for day in range(nr_days):
        # Since most people count from 1, we add 1 to the day value when printing.
        day_food.append(input(f'What was the food cost for day {day + 1}: '))
    return day_food


def get_total_gas(nr_days:int):
    # build a list of fuel expenditures per day
    day_gas = []
    for day in range(nr_days):
        # Since most people count from 1, we add 1 to the day value when printing.
        day_gas.append(input(f'What was the fuel cost for day {day + 1}: '))
    return day_gas

def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    # initialize variables
    people = 0          # an int
    days = 0            # an int
    daily_food = []     # a list
    daily_gas = []      # a list
    total_gas = 0.0     # a float
    total_food = 0.0    # a float

    people = get_nr_people()
    days = get_nr_days()
    daily_food = get_total_food(days)
    daily_gas = get_total_gas(days)

    # Add up the total food and gas values by adding each day's expenditure to a running total
    for day in range(days):
        total_food = total_food + float(daily_food[day])
        total_gas = total_gas + float(daily_gas[day])

    # And, output the calculated information:
    print(f'\n\nFor the {people} person trip of {days} days, you spent a total of:')
    print('Food: ${:0,.2f}'.format(total_food))
    print('Fuel: ${:0,.2f}'.format(total_gas))
    print('\nPer person, this comes out to:')
    print('Food: ${:0,.2f}'.format(total_food / people))
    print('Fuel: ${:0,.2f}'.format(total_gas / people))

main()