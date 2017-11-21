'''factors.py: Returns a list of all the factors of a given number.
Based on https://redd.it/1a0d82
'''

number = None
while number is None:
    try:
        number = int(input('Enter a number to factor: '))
        if number <= 0:
            number = None
            raise ValueError
    except ValueError:
        print('Error: please enter a non-zero positive integer.')

factors = [x for x in range(1, number + 1) if number % x == 0]
print(factors)
