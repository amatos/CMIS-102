# This Python program:
#   Compute the weekly pay for a newspaper carrier.
#   Pay is (number_of_papers * cost * commission * number of days) + tips

# Alberth Matos
# 05/26/2023
# CMIS 102

# Constants:
NEWSPAPER_COST = 4.55 # Price per newspaper
COMMISSION = 6 # Commission for newspapers.  Number is out of 100, not percent
DEVELOPER = 'Alberth Matos'
DATE = '05/26/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named


def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    # Collect input:
    # num_papers_per_day
    # num_days_delivered
    # weekly_tip
    int num_papers_per_day = 0
    int num_days_delivered = 0
    float weekly_tip = 0.0

    num_papers_per_day = int(input('Please enter the number of papers delivered on the route: '))
    num_days_delivered = int(input('Please provide the number of days newspapers were delivered: '))
    weekly_tip = float(input('Please provide any tips received: '))

    # Variables for calculations
    int total_papers_for_week = 0
    float salary = 0.0
    float total_pay = 0.0

    # Total papers delivered are the number of papers per day times the number of days
    total_papers_for_week = num_papers_per_day * num_days_delivered
    print(f'Total number of papers delivered for the week: {total_papers_for_week}')

    # Since commission is provided as a whole number, we need to convert this to percentage
    salary = total_papers_for_week * NEWSPAPER_COST * (COMMISSION / 100)
    print(f'Salary for the week: {salary:.2f}')

    # Total pay for the week is the salary plus any tips for the week
    total_pay = salary + weekly_tip
    print(f'Total payout for the week: {total_pay:.2f}')


main()