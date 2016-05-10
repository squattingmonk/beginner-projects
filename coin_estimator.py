''' coin_estimator.py: Estimates how many coin wrappers the user will need to roll the given weight of each coin. Project found on https://www.redd.it/1idqw1 '''

from collections import namedtuple

Coin = namedtuple('Coin', ['name', 'grams', 'wrapper', 'value'])
messages = []

for coin in (('pennies',  132, 50, 0.01),
             ('nickels',  199, 40, 0.05),
             ('dimes',    113, 50, 0.10),
             ('quarters', 226, 40, 0.25)):
    coin = Coin(*coin)
    while True:
        try:
            weight = float(input('Enter the weight in grams of the {0}: \t'.format(coin.name)))
        except ValueError:
            print('Error: numbers only, please!')
        else:
            break

    wrappers = format(weight / coin.grams, ',.2f')
    amount = format(weight / coin.grams * coin.wrapper * coin.value, ',.2f')
    messages.append('You have {0} rolls (about ${1}) of {2}.'.format(wrappers, amount, coin.name))

print('')

for message in messages:
    print(message)
