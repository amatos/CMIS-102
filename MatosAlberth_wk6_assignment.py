# This Python program:
#   Password validation program.
# Get a password from the user
# Validate that the password is more than 8 and less than 1024 characters
# Validate that the password does not include a space
# Validate that the password contains at least one digit
# Validate that the password contains at least one alphabetic character

# Alberth Matos
# 06/27/2023
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/27/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

def validate_length(password: str):
    # Check if the length of the password is equal or greater than 8 and equal or less than 1024
    if (len(password) >= 8) and (len(password) <= 1024):
        # If so, the password is valid.
        return True
    else:
        # If not, it's invalid.
        return False

def validate_required_alphanums(password: str):
    # Initialize the count of alpha characters, digits, and a check boolean.
    alphas = 0
    nums = 0
    is_ok = False
    # Iterate through each character and count if it is a digit or alpha.  If so, increment a counter for each.
    for my_char in password:
        if my_char.isdigit():
            nums = nums + 1
        if my_char.isalpha():
            alphas = alphas + 1
    # If both alphas are at least 1 and nums are at least 1, set the check boolean to true.
    if (alphas > 0) and (nums > 0):
        is_ok = True
    # Return the check bool, count of alphas and count of nums
    return is_ok, alphas, nums

def validate_prohibited(password: str):
    # Check the number of ' ' characters in password.  If the count is at least 1, then fail the password.
    # Otherwise, pass the password.
    if password.count(' ') > 0:
        # ' ' is an invalid password.
        return False
    else:
        return True

def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    # Initialize check variables
    good_len = False
    good_alphanum = False
    good_prohibited = False

    # Display the password requirements to the user
    print('Password requirements:')
    print(' - Must be at least 8 characters long.')
    print(' - Cannot be more than 1024 characters.')
    print(' - Cannot contain a space.')
    print(' - Must contain at least 1 digit.')
    print(' - Must contain at least one letter from A to Z.')
    my_password = input('Please enter a password: ')
    print('\n\n')

    # Validate if the password is of the right length
    if validate_length(my_password):
        print('Success!  The password contains sufficient characters')
        good_len = True
    else:
        print(f'Unsuccessful.  Your password is not acceptable.  It has {len(my_password)} characters, but must be between 8 and 1024 characters long.')

    # Validate if the password contains at least one digit or alpha character.
    is_ok, alphas, nums = validate_required_alphanums(my_password)
    if is_ok:
        good_alphanum = True
        print('Success!  The password contains both a digit and an alphabetical character.')
    else:
        if alphas == 0:
            print('Unsuccessful.  Your password does not contain any alphabetical characters.')
        if nums == 0:
            print('Unsuccessful.  Your password does not contain any digits.')

    # Validate that there are no prohibited characters
    if validate_prohibited(my_password):
        good_prohibited = True
        print('Success!  Your password does not contain any of the prohibited characters (\' \')')
    else:
        print('Unsuccessful.  Your password is invalid.  It contains at least one space (\' \'), which is prohibited.')

    # Print the final summary.
    if good_len and good_alphanum and good_prohibited:
        print('Summary:  This is a good password.')
    else:

        print('Summary:  This password does not meet the requirements.')

main()