'''whats_my_number.py: Finds the numbers between 1 and 1000 that
match the following conditions:
    - The number has two or more digits.
    - The number is prime.
    - The number does NOT contain a 1 or 7 in it.
    - The sum of all of the digits is less than or equal to 10.
    - The first two digits add up to be odd.
    - The second to last digit is even.
    - The last digit is equal to how many digits are in the number.

Based on https://redd.it/1dbena
'''

import math

def is_prime(x):
    '''Returns whether x is a prime number.'''

    # Numbers less than 2 cannot be prime
    if x < 2:
        return False

    if x == 2:
        return True

    # Could be faster if we only checked against primes. For now,
    # we'll just compare it all numbers less than its square root.
    for y in range(3, int(math.sqrt(x)) + 1):
        if x % y == 0:
            return False

    return True

# List all prime numbers under 1000 containing 2 or more digits
numbers = [str(x) for x in range(10, 1001) if is_prime(x)]

# Limit to numbers not containing 1 or 7
numbers = [x for x in numbers if not any(y in x for y in '17')]

# Limit to numbers whose digits sum to <= 10
numbers = [x for x in numbers if sum(int(y) for y in x) <=10]

# Limit to numbers whose first two digits sum to an odd number
numbers = [x for x in numbers if (int(x[0]) + int(x[1])) % 2 == 1]

# Limit to numbers whose second-to-last digit is even
numbers = [x for x in numbers if int(x[-2]) % 2 == 0]

# Limit to the numbers whose last digit is equal to the number
# of digits in the number
numbers = [int(x) for x in numbers if int(x[-1]) == len(x)]

print(__doc__)
print(numbers)
