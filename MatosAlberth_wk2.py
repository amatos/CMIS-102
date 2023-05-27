# This Python program:
#   Given an initial velocity and angle, calculate how far an object will travel before hitting the ground
# Formula for parabolic motion on the x plane:
# R = (v^2 sin 2θ)/g
# where:
# v = initial velocity
# θ = initial angle in degrees
# g = 9.8m/s^2 on earth at sea level

# Alberth Matos
# 05/26/2023
# CMIS 102

from math import radians, sin

# Defining constant of gravity
GRAVITY = 9.8

def main():
    # Initializing variables
    velocity = 0.0
    angle = 0.0
    range = 0.0

    velocity = float(input('Please provide the initial velocity (in m/s): '))
    angle = float(input('Please provide the initial angle: (in degrees): '))

    # See the formula statement above. range = (v^2 * sin 2θ) / g
    range = ((velocity**2) * sin(2 * radians(angle))) / GRAVITY # math.sin expects radians, we need to convert degrees to rads

    print(f'The object will travel for {range} meters before landing.')

main()