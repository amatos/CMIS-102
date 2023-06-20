# This Python program:
#   Calculate the total number of "The Jetsons" episodes that aired
#  This can be derived by getting the number of episodes per season
#  and then adding the values together.
#  A value of 0 episodes per season indicates that the show ended.

# Alberth Matos
# 06/20/2023
# CMIS 102

# Constants:
DEVELOPER = 'Alberth Matos'
DATE = '06/20/2023'
CLASS = 'CMIS 102' # n.b. class (all lowercase) is a reserved named

def main():
    # Class information
    print(f'Developer: {DEVELOPER}')
    print(f'Date: {DATE}')
    print(f'Class: {CLASS}\n')

    print('Jetsons episodes calculator')
    print('We will calculate the total number of episodes of "The Jetsons" by asking the number of episodes per season.')
    print('If there are no more seasons, please enter a value of 0 when prompted.')

    # track season numbers to make the prompt look nicer
    season_number = 1
    episodes = 0

    # Get number of episodes in season, as an integer
    # (There are no half-episodes)
    episodes_in_season = int(input(f'Please enter the total number of episodes in season {season_number}: '))

    # Loop as long as the number of episodes is not 0
    # If the initial value is 0, then no episodes aired.
    # We could simply check if the number of episodes > 0, but I like the idea of negative episodes.
    while episodes_in_season != 0:
        # Keep a running count of episodes by adding the current season's number to the running count
        episodes = episodes + episodes_in_season
        season_number = season_number + 1
        episodes_in_season = int(input(f'Please enter the total number of episodes in season {season_number}: '))
    print(f'The total number of episodes of "The Jetsons" is {str(episodes)}!')


main()