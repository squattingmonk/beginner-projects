'''
die_roller.py: Simulates the rolling of a number of polyhedral dice.

Based on https://redd.it/1j50e7
'''

import re
from random import randint

pattern = re.compile('^([1-9]|[1-9][0-9]|100)(d)([2-9]|[1-9][0-9]|100)$')

while True:
    roll = input('Enter the dice you want to roll (or type "quit"): ')
    if roll == 'quit':
        break

    roll = pattern.match(roll)

    if not roll:
        print('Error: use the format XdY, where X is the number of '
              'dice to roll and Y is the number of sides.\n')
        continue

    dice  = roll.group(1)
    sides = roll.group(3)
    noun  = 'die' if dice == '1' else 'dice'
    print('Rolling', dice, sides + '-sided', noun + '...')

    dice_pad = len(dice)
    side_pad = len(sides)

    total = 0
    dice  = int(dice)
    sides = int(sides)

    for x in range(dice):
        result = randint(1, sides)
        total += result
        print('Roll', str(x + 1).rjust(dice_pad) + ':',
            str(result).rjust(side_pad))

    print('-' * (7 + dice_pad + side_pad))
    print('Total:', str(total).rjust(dice_pad + side_pad))
    print()
