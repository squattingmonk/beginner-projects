''' higher_lower.py: The computer chooses a number from 1 - 100. The user must
    guess the number, and the computer will tell whether the answer is higher
    or lower until the user guesses the correct number. Based on project at
    https://redd.it/19jj9a. '''

import random

def higher_lower():
    guesses = 0
    guess = None
    number = random.randrange(1, 101)
    message = 'No, the number is {0} than that! Guess again: '

    while guess != number:
        if guess == None:
            guess = input('\nOkay, guess the number I\'m thinking of: ')
        else:
            guess = input(message.format('higher' if number > guess else 'lower'))

        try:
            guess = int(guess)
            guesses += 1
        except ValueError:
            print('Whoops! Please enter a single integer.')
            guess = None

    print('Yes, that\'s it! You got the correct number in {0} guesses.'.format(guesses))

if __name__ == '__main__':
    print(__doc__)

    while True:
        higher_lower()
        again = input('Would you like to play again? (Y/n) ')
        if len(again) != 0 and again.strip()[0].lower() == 'n':
            break
