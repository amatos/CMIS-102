# This Python program:
# Write a function that uses student name as argument. The function should display the student name and prompt the
# user for three grades for the student: one for the discussion, one for the quiz, and one for the programming
# assignment. The function should calculate the weighted average grade using the following formula and return the
# calculated average
#
# Main program defines a list of 4 students, that are fed into the function.
# Print out the highest scoring student, along wish the student's grade.

# wtAvgGrade = discussion_grade * 0.15 + quiz_grade * 0.35 + assignment_grade * 0.5

# Alberth Matos
# 06/20/2023
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/20/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

def student_average_grade(name: str):
    print(f'\n\nEvaluating student {name}\n')
    discussion_grade = input('Please enter the discussion grade: ')
    while not discussion_grade.isdigit():
        # We check for a numerical value and loop until we get one.
        print('Invalid value.  Please enter a numerical value.')
        discussion_grade = input('Please enter the discussion grade: ')
    quiz_grade = input('Please enter the quiz grade: ')
    while not quiz_grade.isdigit():
        # We check for a numerical value and loop until we get one.
        print('Invalid value.  Please enter a numerical value.')
        quiz_grade = input('Please enter the quiz grade: ')
    assignment_grade = input('Please enter the assignment grade: ')
    while not assignment_grade.isdigit():
        # We check for a numerical value and loop until we get one.
        print('Invalid value.  Please enter a numerical value.')
        assignment_grade = input('Please enter the assignment grade: ')

    # For this calculation, we explicitly cast each of the values above to floats
    weighted_average = (float(discussion_grade) * 0.15) + (float(quiz_grade) * 0.35) + (float(assignment_grade) * 0.5)

    return weighted_average


def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    students = ['Alexandra Arbeiterin', 'Billy Bob', 'Charles Cane', 'Danielle Deux']

    highest = None
    highest_student = ''
    for student in students:
        average = student_average_grade(name=student)
        if highest == None or highest < average:
            highest_student = student
            highest = average
    print(f'The student with the highest grade is {highest_student}, with a score of {str(highest)}')


main()