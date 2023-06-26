# This Python program:
#   DESCRIPTION

# Alberth Matos
# '06/27/2023'
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/27/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

def count_letter(text:str, letter: str):
    return text.lower().count(letter.lower())


def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    my_string = input('Please enter a string: ')
    vowel_a = count_letter(my_string, 'a')
    vowel_e = count_letter(my_string, 'e')
    vowel_i = count_letter(my_string, 'i')
    vowel_o = count_letter(my_string, 'o')
    vowel_u = count_letter(my_string, 'u')
    initials = count_letter(my_string, 'acm')

    print('\n')
    print(f'Number of A: {vowel_a}')
    print(f'Number of E: {vowel_e}')
    print(f'Number of I: {vowel_i}')
    print(f'Number of O: {vowel_o}')
    print(f'Number of U: {vowel_u}')
    print('\n\n')
    print(f'Occurances of my initials: {initials}')
main()