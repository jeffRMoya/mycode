#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
    Conditionals - Life of Brian guessing game using a while True loop."""

turn = 0
answer = ' '

while turn < 3 and answer != "Brian":
    turn += 1
    answer = input('Finish the movie title,"Monty Python\'s The Life of _____": ').capitalize()

    if answer == 'Brian':
        print('Correct')
    elif turn==3:
        print("Sorry, the answer was Brian.")
    elif answer == 'Shrubbery':
        print("You gave the super secret answer!")
        turn = 3
    else:
        print("Sorry! Try again!")
