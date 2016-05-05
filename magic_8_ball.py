''' magic_8_ball.py: Responds with a random answer to the user's question.

Project found on https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/ '''

import time
import random

answers = (
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes, definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy; try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.')

while True:
    input('What do you wish to know? ')
    print('Thinking...')
    time.sleep(3)
    print(random.choice(answers))
    time.sleep(1)

    if input('Would you like to ask another question? (Y/n) ').lower() == 'n':
        break;
