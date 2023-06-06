# This Python program:
#   Given an defined velocity and angle, calculate how far an object will travel before hitting the ground
# based on inputted force of gravity.  Prompt user for value of gravity in terms of 2 numbers and a mathematical
# operand (i.e. addition, subtraction, multiplication, division)
# Formula for parabolic motion on the x plane:
# R = (v^2 sin 2θ)/g
# where:
# v = initial velocity
# θ = initial angle in degrees
# g = 9.8m/s^2 on earth at sea level
# Alberth Matos
# 06/04/2023
# CMIS 102

from math import radians, sin

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/04/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    print('We will calculate the range of parabolic motion for an object at an initial velocity of')
    print('50m/s at an angle of 45 degrees, at your preferred gravity.')
    print('To enter gravity, please provide two numbers and a mathematical operation')
    print('  (i.e. addition, subtraction, multiplication, division)')
    number1 = input('Please enter the first number: ')
    number2 = input('Please enter the second number: ')
    operand = input('Please enter the operand (Options are:  + - * /):  ')

    if operand == '+':
        gravity = float(number1) + float(number2)
    elif operand == '-':
        gravity = float(number1) - float(number2)
    elif operand == '*':
        gravity = float(number1) * float(number2)
    elif operand == '/':
        gravity = float(number1) / float(number2)
    else:
        print('Operand did not match one of: + - * /')
        exit

    velocity = 50
    angle = 45

    # See the formula statement above. range = (v^2 * sin 2θ) / g
    range = ((velocity**2) * sin(2 * radians(angle))) / gravity # math.sin expects radians, we need to convert degrees to rads

    print(f'if gravity is equal to {number1}{operand}{number2}, or {gravity}m/s/s then')
    if gravity < 0:
        print('The object would drift off into space because gravity is less than 0.')
    else:
        print(f'the object will travel for {range} meters before landing.')

main()